import os
from typing import Optional, Dict, Any
# from enhancer_factory import EnhancerFactory
from modules.magic_prompt.enhancer_factory import EnhancerFactory

class PromptEnhancerService:
    """
    Main service class for enhancing prompts.
    Provides a simple interface for the API service to use.
    """
    
    def __init__(self, provider: str = "openai", config: Optional[Dict[str, Any]] = None):
        """
        Initialize the prompt enhancer service.
        
        Args:
            provider (str): The provider to use, defaults to 'openai'
            config (Optional[Dict[str, Any]]): Additional configuration for the enhancer
        """
        self.enhancer = EnhancerFactory.create_enhancer(provider)
        
        if config:
            self.enhancer.set_config(config)
    
    def enhance(self, user_prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Enhance a user prompt.
        
        Args:
            user_prompt (str): The user's input prompt
            system_prompt (Optional[str]): System instructions for the model
            
        Returns:
            str: The enhanced prompt
        """
        return self.enhancer.enhance_prompt(user_prompt, system_prompt)
    
    def update_config(self, config: Dict[str, Any]) -> None:
        """
        Update the configuration of the underlying enhancer.
        
        Args:
            config (Dict[str, Any]): New configuration values
        """
        self.enhancer.set_config(config)
        
    def get_config(self) -> Dict[str, Any]:
        """
        Get the current configuration.
        
        Returns:
            Dict[str, Any]: Current configuration
        """
        return self.enhancer.get_config()
