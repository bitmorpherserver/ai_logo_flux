# Example usage of the PromptEnhancerService
import time
import os
from dotenv import load_dotenv
from modules.magic_prompt.prompt_enhancer_service import PromptEnhancerService
user_prompt=""
def main(prompt: str):
    # Load environment variables
    load_dotenv()
    
    # Create the service
    service = PromptEnhancerService(
        provider="openai",
        config={
            "temperature": 0.8,
            "max_tokens": 1500
        }
    )
    
    # Example user prompt
    # global user_prompt
    
    
    # Example system prompt
    system_prompt = """
    You are a prompt editor for a logo generation AI. When given a base prompt describing a logo design and user instructions specifying requested changes, your task is to apply ONLY the explicit edits stated by the user.
-Make the specified changes accurately, without altering unrelated parts of the base prompt.
-Retain the original tone, structure, and intent.
-Do not add extra suggestions or ideas.
-Output only the final, fully edited prompt without any explanations, lists, or greetings.
You will always receive:
-the base prompt
-the user’s change instructions
    """
    
    # Enhance the prompt
    current= time.time()
    enhanced_prompt = service.enhance(prompt, system_prompt)
    now = time.time()
    print(now-current)
    # Print results
    # print("Original Prompt:")
    # print(prompt)
    print("\nEnhanced Prompt:")
    print(enhanced_prompt)
    return enhanced_prompt

def create_magic_prompt(base_propmt:str):
    global user_prompt
    user_prompt = base_propmt
    return main()



if __name__ == "__main__":
    main()
