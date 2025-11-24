from regex_extractor import DataExtractor

def display_results(category, results):
    print(f"\n{'='*50}")
    print(f"{category}")
    print(f"{'='*50}")
    if isinstance(results, dict):
        for key, value in results.items():
            print(f"{key}: {value}")
    elif isinstance(results, list):
        for item in results:
            print(f"  - {item}")
    else:
        print(results)

def run_tests():
    extractor = DataExtractor()
    
    test_data = """
    Contact us at user@example.com or firstname.lastname@company.co.uk
    Visit our website: https://www.example.com or https://subdomain.example.org/page
    Call us: (123) 456-7890, 123-456-7890, or 123.456.7890
    Payment: 1234 5678 9012 3456 or 1234-5678-9012-3456
    Meeting time: 14:30 or 2:30 PM
    HTML: <p>Paragraph</p> <div class="example">Content</div>
    Follow #example and #ThisIsAHashtag
    Prices: $19.99 and $1,234.56
    """
    
    print("REGEX DATA EXTRACTION TEST RESULTS")
    print("="*50)
    
    display_results("EMAIL ADDRESSES", extractor.extract_emails(test_data))
    display_results("URLS", extractor.extract_urls(test_data))
    display_results("PHONE NUMBERS", extractor.extract_phone_numbers(test_data))
    display_results("CREDIT CARDS", extractor.extract_credit_cards(test_data))
    display_results("TIME FORMATS", extractor.extract_time(test_data))
    display_results("HTML TAGS", extractor.extract_html_tags(test_data))
    display_results("HASHTAGS", extractor.extract_hashtags(test_data))
    display_results("CURRENCY", extractor.extract_currency(test_data))

def test_edge_cases():
    extractor = DataExtractor()
    
    print("\n\nEDGE CASE TESTING")
    print("="*50)
    
    edge_cases = {
        'Invalid Email': 'notanemail@',
        'Incomplete URL': 'http:/incomplete',
        'Wrong Phone Format': '12-345-6789',
        'Invalid Credit Card': '1234 5678 9012',
        'Mixed Time': 'Meeting at 25:00 or 13:70 PM',
        'Malformed HTML': '<div>No closing tag',
        'Invalid Hashtag': '# spaced hashtag',
        'Wrong Currency': '$1234.5'
    }
    
    for case_name, test_string in edge_cases.items():
        print(f"\nTest: {case_name}")
        print(f"Input: {test_string}")
        results = extractor.extract_all(test_string)
        has_match = any(v for v in results.values() if v and v != {'24h_format': [], '12h_format': []})
        print(f"Match Found: {has_match}")

if __name__ == "__main__":
    run_tests()
    test_edge_cases()
