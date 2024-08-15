# validation.py

import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_valid_mobile_number(mobile_number):
    return mobile_number.isdigit() and len(mobile_number) == 10

def is_valid_pdf(file):
    return file.lower().endswith('.pdf')
