import os
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class PromptEnhancer(ABC):
    """
    Abstract base class for prompt enhancers.
    This design pattern allows for easy switching between different API providers.
    """
    
    @abstractmethod
    def enhance_prompt(self, user_prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Enhance the user prompt using the AI model.
        
        Args:
            user_prompt (str): The input prompt from the user
            system_prompt (Optional[str]): System instructions to guide the model
            
        Returns:
            str: The enhanced prompt
        """
        pass
    
    @abstractmethod
    def get_config(self) -> Dict[str, Any]:
        """
        Get the current configuration of the enhancer.
        
        Returns:
            Dict[str, Any]: Configuration dictionary
        """
        pass
    
    @abstractmethod
    def set_config(self, config: Dict[str, Any]) -> None:
        """
        Update the configuration of the enhancer.
        
        Args:
            config (Dict[str, Any]): New configuration values
        """
        pass
