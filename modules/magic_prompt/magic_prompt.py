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
    # service = PromptEnhancerService(
    #     provider="openai",
    #     config={
    #         "temperature": 0.8,
    #         "max_tokens": 1500
    #     }
    # )

    service = PromptEnhancerService(
        provider="openai",
        config={
            "model": "gpt-4.1-nano",
            "temperature": 0.8,
            "max_tokens": 1500
        }
    )
    
    # Example user prompt
    # global user_prompt
    
    
    # Example system prompt
    system_prompt = """
    You are a creative brand designer assistant. 
    Your job is to take short, vague, or unclear user inputs and turn them into rich, detailed descriptions suitable for a logo generation AI model. 
    Add context, symbolism, style suggestions, and make the prompt vivid. 
    Do not provide multiple ideas, suggestions, or commentary. Output only one final enhanced prompt — no explanations, lists, or greetings.
    """
    
    # Enhance the prompt
    current= time.time()
    enhanced_prompt = service.enhance(prompt, system_prompt)
    now = time.time()
    print(now-current)
    # Print results
    print("Original Prompt:")
    print(prompt)
    print("\nEnhanced Prompt:")
    print(enhanced_prompt)
    return enhanced_prompt

def create_magic_prompt(base_propmt:str):
    global user_prompt
    user_prompt = base_propmt
    return main()



if __name__ == "__main__":
    main()
