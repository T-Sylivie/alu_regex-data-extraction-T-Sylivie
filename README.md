This project is a Python-based data extraction tool built for the ALU Regex Onboarding Hackathon. It uses Regular Expressions (regex) to identify and extract eight types of data from text:

Email addresses

URLs

Phone numbers

Credit card numbers

Times (12-hour and 24-hour formats)

HTML tags

Hashtags

Currency amounts

The repository contains a main extraction class (regex_extractor.py), test cases, a requirements file, and the README itself.

To use the tool, you create a DataExtractor object and call its methods to extract specific patterns from any text string. The README includes example usage, detailed regex patterns for each data type, and edge cases handled (e.g., malformed emails, invalid times, or inconsistent phone formatting).

The project also includes comprehensive test cases (test_extraction.py) that demonstrate and validate all extraction methods.

Finally, the README documents each method in the DataExtractor class, provides installation steps, and credits the ALU Hackathon context.
