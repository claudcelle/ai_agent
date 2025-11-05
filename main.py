import os
from dotenv import load_dotenv
from google.genai import types
from google import genai
import sys

from config import *


def main():
       
    try:
        prompt = sys.argv[1]
    except Exception as e: 
        print(e)
        sys.exit(1) 
    
    if "--verbose" in sys.argv:
        print(f'User prompt: {prompt}')  
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    # print(api_key[-5:])

    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    response = client.models.generate_content(
        model= MODEL,
        contents = prompt,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
        )
    print(response.text)
    
    if "--verbose" in sys.argv:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
     


if __name__ == "__main__":
    main()
