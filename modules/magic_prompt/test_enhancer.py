import unittest
from unittest.mock import patch, MagicMock
from prompt_enhancer_service import PromptEnhancerService

class TestPromptEnhancerService(unittest.TestCase):
    
    @patch('enhancer_factory.EnhancerFactory.create_enhancer')
    def test_enhance(self, mock_create_enhancer):
        # Setup mock enhancer
        mock_enhancer = MagicMock()
        mock_enhancer.enhance_prompt.return_value = "Enhanced prompt"
        mock_create_enhancer.return_value = mock_enhancer
        
        # Create service
        service = PromptEnhancerService()
        
        # Test enhance method
        result = service.enhance("Original prompt", "System instructions")
        
        # Assertions
        self.assertEqual(result, "Enhanced prompt")
        mock_enhancer.enhance_prompt.assert_called_once_with("Original prompt", "System instructions")
    
    @patch('enhancer_factory.EnhancerFactory.create_enhancer')
    def test_update_config(self, mock_create_enhancer):
        # Setup mock enhancer
        mock_enhancer = MagicMock()
        mock_create_enhancer.return_value = mock_enhancer
        
        # Create service
        service = PromptEnhancerService()
        
        # Test update_config method
        new_config = {"temperature": 0.9}
        service.update_config(new_config)
        
        # Assertions
        mock_enhancer.set_config.assert_called_once_with(new_config)
    
    @patch('enhancer_factory.EnhancerFactory.create_enhancer')
    def test_get_config(self, mock_create_enhancer):
        # Setup mock enhancer
        mock_enhancer = MagicMock()
        mock_enhancer.get_config.return_value = {"model": "gpt-4o", "temperature": 0.7}
        mock_create_enhancer.return_value = mock_enhancer
        
        # Create service
        service = PromptEnhancerService()
        
        # Test get_config method
        result = service.get_config()
        
        # Assertions
        self.assertEqual(result, {"model": "gpt-4o", "temperature": 0.7})
        mock_enhancer.get_config.assert_called_once()

if __name__ == "__main__":
    unittest.main()
