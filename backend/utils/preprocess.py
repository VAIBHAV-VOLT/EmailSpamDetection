#!/usr/bin/env python3
"""
Text Preprocessing and Cleaning Utilities
Handles email text cleaning, normalization, and extraction.
"""

import re
from urllib.parse import urlparse


def clean_text(text):
    """
    Clean and normalize email text.
    
    :param text: Raw email text
    :return: Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove HTML tags (basic)
    text = re.sub(r'<[^>]+>', '', text)
    
    return text.strip()


def extract_urls(text):
    """
    Extract URLs from email body text.
    
    :param text: Email body text
    :return: List of URL dictionaries
    """
    if not text:
        return []
    
    # Pattern to detect URLs
    url_pattern = r'(https?://[^\s<>"\'()]+|www\.[^\s<>"\'()]+)'
    found_urls = re.findall(url_pattern, text)
    
    urls = []
    for url in found_urls:
        # Normalize URLs like www.example.com
        if not url.startswith("http"):
            url = "http://" + url
        
        try:
            parsed = urlparse(url)
            urls.append({
                "full_url": url,
                "domain": parsed.netloc,
                "path": parsed.path,
                "scheme": parsed.scheme
            })
        except:
            continue
    
    return urls


def extract_email_addresses(text):
    """
    Extract email addresses from text.
    
    :param text: Text to search
    :return: List of email addresses
    """
    if not text:
        return []
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    return list(set(emails))


def extract_domain(email_header):
    """
    Extract domain from an email address or email header.
    
    :param email_header: Email address (e.g., "user@example.com")
    :return: Domain name or None
    """
    if not email_header:
        return None
    
    # Remove angle brackets if present
    email_header = email_header.replace('<', '').replace('>', '').strip()
    
    if "@" in email_header:
        return email_header.split("@")[-1].lower().strip()
    
    return None


def normalize_subject(subject):
    """
    Normalize email subject line.
    
    :param subject: Raw subject
    :return: Normalized subject
    """
    if not subject:
        return ""
    
    # Remove Re:, Fwd: prefixes
    subject = re.sub(r'^(Re:|Fwd:|re:|fwd:)\s*', '', subject)
    
    return subject.strip()


def extract_suspicious_keywords(text):
    """
    Extract potentially suspicious keywords from email text.
    
    :param text: Email body text
    :return: List of suspicious keywords found
    """
    if not text:
        return []
    
    # Common phishing keywords
    suspicious_keywords = [
        'verify', 'confirm', 'urgent', 'immediate', 'action required',
        'click here', 'update', 'reset', 'password', 'account', 'suspended',
        'locked', 'unusual activity', 'confirm identity', 'provide information',
        're-enter', 'validate', 'authenticate', 'limited time', 'act now',
        'expire', 'claim', 'reward', 'winner', 'congratulations'
    ]
    
    text_lower = text.lower()
    found_keywords = []
    
    for keyword in suspicious_keywords:
        if keyword.lower() in text_lower:
            found_keywords.append(keyword)
    
    return list(set(found_keywords))


def tokenize_text(text):
    """
    Split text into tokens (words).
    
    :param text: Text to tokenize
    :return: List of tokens
    """
    if not text:
        return []
    
    # Simple whitespace tokenization
    tokens = text.split()
    
    return [token.lower() for token in tokens]


def truncate_text(text, max_length=512):
    """
    Truncate text to maximum length (for model processing).
    
    :param text: Text to truncate
    :param max_length: Maximum length
    :return: Truncated text
    """
    if not text:
        return ""
    
    if len(text) > max_length:
        return text[:max_length]
    
    return text
