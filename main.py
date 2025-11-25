import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions,call_function
from config import *


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for _ in range(20):

        try:
            result = generate_content(client, messages, verbose)
            #  It's finished only if no candidate contains a function call and response.text is non-empty. In that case, print the final response and break out of the loop; otherwise continue the loop
            if result[0]:
                print(result[1])
                break
        except Exception as e:
            print(e)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    
    for candidate in response.candidates:
        messages.append(candidate.content)



    if not response.function_calls:
        if response.text: 
            return True, response.text
        else:
            return False, ""
    function_responses = []
    for function_call_part in response.function_calls:
        # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        function_call_result = call_function(function_call_part,verbose)
        if (
            not function_call_result.parts #
            or not function_call_result.parts[0].function_response
        ):
            raise Exception('Fatal: empty function call results ')
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")   
        
        function_responses.append(function_call_result.parts[0])
    
    messages.append(types.Content(role="user", parts=function_responses))
    return False, ""

if __name__ == "__main__":
    main()
