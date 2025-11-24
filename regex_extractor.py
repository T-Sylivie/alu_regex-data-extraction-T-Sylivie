import re

class DataExtractor:
    
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'https?://(?:www\.)?[A-Za-z0-9-]+(?:\.[A-Za-z]{2,})+(?:/[^\s]*)?',
            'phone': r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
            'credit_card': r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',
            'time_24h': r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9]\b',
            'time_12h': r'\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?(?:AM|PM|am|pm)\b',
            'html_tag': r'<[^>]+>',
            'hashtag': r'#[A-Za-z0-9_]+',
            'currency': r'\$\d{1,3}(?:,\d{3})*\.\d{2}\b|\$\d+\.\d{2}\b'
        }
    
    def extract_emails(self, text):
        return re.findall(self.patterns['email'], text)
    
    def extract_urls(self, text):
        return re.findall(self.patterns['url'], text)
    
    def extract_phone_numbers(self, text):
        return re.findall(self.patterns['phone'], text)
    
    def extract_credit_cards(self, text):
        return re.findall(self.patterns['credit_card'], text)
    
    def extract_time(self, text):
        time_24h = re.findall(self.patterns['time_24h'], text)
        time_12h = re.findall(self.patterns['time_12h'], text)
        return {
            '24h_format': time_24h,
            '12h_format': time_12h
        }
    
    def extract_html_tags(self, text):
        return re.findall(self.patterns['html_tag'], text)
    
    def extract_hashtags(self, text):
        return re.findall(self.patterns['hashtag'], text)
    
    def extract_currency(self, text):
        return re.findall(self.patterns['currency'], text)
    
    def extract_all(self, text):
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'credit_cards': self.extract_credit_cards(text),
            'time': self.extract_time(text),
            'html_tags': self.extract_html_tags(text),
            'hashtags': self.extract_hashtags(text),
            'currency': self.extract_currency(text)
        }
