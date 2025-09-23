import unittest
import re
from data_extractor import RegexDataExtractor

class TestRegexDataExtractor(unittest.TestCase):
    """
    Comprehensive test suite for RegexDataExtractor class.
    """
    
    def setUp(self):
        """Set up the extractor instance before each test."""
        self.extractor = RegexDataExtractor()
    
    def test_extract_emails(self):
        """Test email extraction with various formats."""
        test_cases = [
            {
                'input': 'Contact: john@example.com, jane.doe@company.co.uk',
                'expected': ['john@example.com', 'jane.doe@company.co.uk'],
                'description': 'Basic email extraction'
            },
            {
                'input': 'Invalid emails: user@, @domain.com, no@tld',
                'expected': [],
                'description': 'Invalid emails should not be extracted'
            },
            {
                'input': 'Multiple emails: test1@gmail.com, test2@yahoo.com, test3@company.org',
                'expected': ['test1@gmail.com', 'test2@yahoo.com', 'test3@company.org'],
                'description': 'Multiple valid emails'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_emails(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_urls(self):
        """Test URL extraction with various formats."""
        test_cases = [
            {
                'input': 'Visit https://www.example.com and http://sub.domain.org/path',
                'expected': ['https://www.example.com', 'http://sub.domain.org/path'],
                'description': 'Basic URL extraction'
            },
            {
                'input': 'Invalid: http://, https://, www.example.com',
                'expected': [],
                'description': 'Incomplete URLs should not be extracted'
            },
            {
                'input': 'Complex URL: https://example.com/path?query=value&param=2',
                'expected': ['https://example.com/path?query=value&param=2'],
                'description': 'URL with query parameters'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_urls(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_phone_numbers(self):
        """Test phone number extraction with various formats."""
        test_cases = [
            {
                'input': 'Call (123) 456-7890 or 123-456-7890 or 123.456.7890',
                'expected': ['(123) 456-7890', '123-456-7890', '123.456.7890'],
                'description': 'Multiple phone number formats'
            },
            {
                'input': 'Short numbers: 123-4567, 123.4567',
                'expected': [],
                'description': 'Short numbers should not be extracted'
            },
            {
                'input': 'International: +1-123-456-7890, but not extracted',
                'expected': [],
                'description': 'International format not supported'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_phone_numbers(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_credit_cards(self):
        """Test credit card number extraction."""
        test_cases = [
            {
                'input': 'Cards: 1234 5678 9012 3456 and 1234-5678-9012-3456',
                'expected': ['1234 5678 9012 3456', '1234-5678-9012-3456'],
                'description': 'Credit card with spaces and dashes'
            },
            {
                'input': 'Invalid: 1234-5678, 1234567890123456',
                'expected': [],
                'description': 'Invalid card numbers should not be extracted'
            },
            {
                'input': 'Edge: 1234-5678-9012-3456 and 1234 5678 9012 3456 are valid',
                'expected': ['1234-5678-9012-3456', '1234 5678 9012 3456'],
                'description': 'Multiple valid card formats'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_credit_cards(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_hashtags(self):
        """Test hashtag extraction."""
        test_cases = [
            {
                'input': 'Trending: #python #MachineLearning #ThisIsAHashtag',
                'expected': ['#python', '#MachineLearning', '#ThisIsAHashtag'],
                'description': 'Basic hashtag extraction'
            },
            {
                'input': 'No hashtags: just regular text here',
                'expected': [],
                'description': 'Text without hashtags'
            },
            {
                'input': 'Edge: #123 #test_hashtag #multiple#hashtags',
                'expected': ['#123', '#test_hashtag', '#multiple', '#hashtags'],
                'description': 'Various hashtag formats'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_hashtags(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_times(self):
        """Test time extraction in 12-hour and 24-hour formats."""
        test_cases = [
            {
                'input': '24-hour: 14:30, 09:45, 23:59. 12-hour: 2:30 PM, 11:45 AM',
                'expected': ['14:30', '09:45', '23:59', '2:30 PM', '11:45 AM'],
                'description': 'Mixed time formats'
            },
            {
                'input': 'Invalid: 25:00, 13:60, 12:75 PM',
                'expected': [],
                'description': 'Invalid times should not be extracted'
            },
            {
                'input': 'Case: 2:30 pm, 11:45 am, 9:00 PM',
                'expected': ['2:30 pm', '11:45 am', '9:00 PM'],
                'description': 'Case insensitive AM/PM'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_times(case['input'])
                self.assertEqual(sorted(result), sorted(case['expected']))
    
    def test_extract_html_tags(self):
        """Test HTML tag extraction."""
        test_cases = [
            {
                'input': '<p>Hello</p> <div class="test">Content</div> <img src="image.jpg">',
                'expected': ['<p>', '</p>', '<div class="test">', '</div>', '<img src="image.jpg">'],
                'description': 'Various HTML tags'
            },
            {
                'input': 'No tags: just plain text here',
                'expected': [],
                'description': 'Text without HTML tags'
            },
            {
                'input': 'Self-closing: <br/> <hr /> <img src="test.jpg" />',
                'expected': ['<br/>', '<hr />', '<img src="test.jpg" />'],
                'description': 'Self-closing tags'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_html_tags(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_currency(self):
        """Test currency amount extraction."""
        test_cases = [
            {
                'input': 'Prices: $19.99, $1,234.56, $50',
                'expected': ['$19.99', '$1,234.56', '$50'],
                'description': 'Various currency formats'
            },
            {
                'input': 'Invalid: $1234.5.67, $, $abc',
                'expected': [],
                'description': 'Invalid currency formats'
            },
            {
                'input': 'Edge: $1,000,000.00, $0.99, $999',
                'expected': ['$1,000,000.00', '$0.99', '$999'],
                'description': 'Edge case currency amounts'
            }
        ]
        
        for case in test_cases:
            with self.subTest(case=case['description']):
                result = self.extractor.extract_currency(case['input'])
                self.assertEqual(result, case['expected'])
    
    def test_extract_all_comprehensive(self):
        """Test comprehensive extraction of all data types."""
        comprehensive_text = """
        Contact: john@example.com, (123) 456-7890
        Website: https://example.com
        Payment: 1234-5678-9012-3456, $199.99
        Social: #test #hashtag
        Time: 14:30 meeting at 2:30 PM
        HTML: <p>Test</p> <div>content</div>
        """
        
        result = self.extractor.extract_all(comprehensive_text)
        
        # Verify each data type
        self.assertIn('john@example.com', result['emails'])
        self.assertIn('(123) 456-7890', result['phone_numbers'])
        self.assertIn('https://example.com', result['urls'])
        self.assertIn('1234-5678-9012-3456', result['credit_cards'])
        self.assertIn('$199.99', result['currency'])
        self.assertIn('#test', result['hashtags'])
        self.assertIn('#hashtag', result['hashtags'])
        self.assertIn('14:30', result['times'])
        self.assertIn('2:30 PM', result['times'])
        self.assertIn('<p>', result['html_tags'])
        self.assertIn('</p>', result['html_tags'])
    
    def test_edge_cases(self):
        """Test various edge cases."""
        edge_case_text = """
        Edge cases:
        - Email in middle: text john@example.com text
        - Phone with text: call me at (123) 456-7890 now
        - URL in sentence: visit https://example.com/page for more
        - Hashtag with numbers: #2024 #test123
        - Currency in context: price is $19.99 each
        - Time ranges: 9:00 AM to 5:00 PM
        - HTML attributes: <input type="text" value="test">
        """
        
        result = self.extractor.extract_all(edge_case_text)
        
        # Should extract correctly even in context
        self.assertIn('john@example.com', result['emails'])
        self.assertIn('(123) 456-7890', result['phone_numbers'])
        self.assertIn('https://example.com/page', result['urls'])
        self.assertIn('#2024', result['hashtags'])
        self.assertIn('#test123', result['hashtags'])
        self.assertIn('$19.99', result['currency'])
        self.assertIn('9:00 AM', result['times'])
        self.assertIn('5:00 PM', result['times'])
        self.assertIn('<input type="text" value="test">', result['html_tags'])

    def test_empty_input(self):
        """Test extraction with empty input."""
        result = self.extractor.extract_all("")
        
        for data_type, items in result.items():
            self.assertEqual(items, [], f"{data_type} should be empty for empty input")
    
    def test_no_matches(self):
        """Test text with no extractable data."""
        no_data_text = "This is just regular text without any special data patterns."
        result = self.extractor.extract_all(no_data_text)
        
        for data_type, items in result.items():
            self.assertEqual(items, [], f"{data_type} should be empty for text without patterns")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
