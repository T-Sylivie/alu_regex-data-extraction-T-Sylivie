from data_extractor import RegexDataExtractor

# Create extractor instance
extractor = RegexDataExtractor()

# Sample text
text = """
Contact: john@example.com, call (123) 456-7890
Website: https://example.com
Payment: $19.99 with card 1234-5678-9012-3456
"""

# Extract all data types
results = extractor.extract_all(text)
print(results)

# Extract specific data type
emails = extractor.extract_emails(text)
urls = extractor.extract_urls(text)
