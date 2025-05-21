import os
from typing import Dict, Any, Optional, List
import openai
# from prompt_enhancer import PromptEnhancer
from modules.magic_prompt.prompt_enhancer import PromptEnhancer

class OpenAIPromptEnhancer(PromptEnhancer):
    """
    Implementation of PromptEnhancer that uses OpenAI's API for prompt enhancement.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        """
        Initialize the OpenAI prompt enhancer.
        
        Args:
            api_key (Optional[str]): OpenAI API key. If not provided, will try to get from environment
            model (str): Model to use, defaults to gpt-4o
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set as OPENAI_API_KEY environment variable")
        
        self.client = openai.OpenAI(api_key=self.api_key)
        self.config = {
            "model": model,
            "temperature": 0.7,
            "max_tokens": 1000,
            "top_p": 1.0,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0
        }
    
    def enhance_prompt(self, user_prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Enhance the user prompt using OpenAI's GPT-4o model.
        
        Args:
            user_prompt (str): The input prompt from the user
            system_prompt (Optional[str]): System instructions for the model
            
        Returns:
            str: The enhanced prompt
        """
        messages: List[Dict[str, str]] = []
        
        # Add system prompt if provided
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        else:
            # Default system prompt for enhancing user prompts
            messages.append({
                "role": "system", 
                "content": "Your task is to enhance and improve the user's prompt to make it more detailed, clearer, and more effective for generating high-quality responses."
            })
        
        # Add user prompt
        messages.append({"role": "user", "content": user_prompt})
        
        try:
            response = self.client.chat.completions.create(
                model=self.config["model"],
                messages=messages,
                temperature=self.config["temperature"],
                max_tokens=self.config["max_tokens"],
                top_p=self.config["top_p"],
                frequency_penalty=self.config["frequency_penalty"],
                presence_penalty=self.config["presence_penalty"]
            )
            
            # Get the enhanced prompt from the response
            enhanced_prompt = response.choices[0].message.content
            return enhanced_prompt
        
        except Exception as e:
            raise Exception(f"Error enhancing prompt with OpenAI: {str(e)}")

    def get_config(self) -> Dict[str, Any]:
        """
        Get the current configuration of the enhancer.
        
        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        return self.config.copy()
    
    def set_config(self, config: Dict[str, Any]) -> None:
        """
        Update the configuration of the enhancer.
        
        Args:
            config (Dict[str, Any]): New configuration values
        """
        for key, value in config.items():
            if key in self.config:
                self.config[key] = value
