import os
from dotenv import load_dotenv
from google import genai
import sys


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
    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                   contents = prompt)
    print(response.text)
    
    if "--verbose" in sys.argv:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
     


if __name__ == "__main__":
    main()
