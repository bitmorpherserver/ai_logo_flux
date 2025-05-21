from dotenv import load_dotenv
from typing import Dict, Any, List, Optional, Type
from modules.magic_prompt.prompt_enhancer import PromptEnhancer
from modules.magic_prompt.openai_enhancer import OpenAIPromptEnhancer

class EnhancerFactory:
    """
    Factory class for creating prompt enhancers.
    This allows for easy switching between different enhancer implementations.
    """
    
    _enhancers: Dict[str, Type[PromptEnhancer]] = {
        "openai": OpenAIPromptEnhancer
    }
    
    @classmethod
    def register_enhancer(cls, name: str, enhancer_class: Type[PromptEnhancer]) -> None:
        """
        Register a new enhancer implementation.
        
        Args:
            name (str): The name to register the enhancer under
            enhancer_class (Type[PromptEnhancer]): The enhancer class
        """
        cls._enhancers[name] = enhancer_class
    
    @classmethod
    def create_enhancer(cls, provider: str = "openai", **kwargs) -> PromptEnhancer:
        """
        Create a new enhancer instance.
        
        Args:
            provider (str): The provider to use, defaults to 'openai'
            **kwargs: Additional arguments to pass to the enhancer constructor
            
        Returns:
            PromptEnhancer: The created enhancer
        """
        if provider not in cls._enhancers:
            raise ValueError(f"Unknown provider: {provider}")
        
        # Load environment variables
        load_dotenv()
        
        # Create and return the enhancer
        return cls._enhancers[provider](**kwargs)
