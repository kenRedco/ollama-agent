# backend/guardrails.py
from email_validator import validate_email, EmailNotValidError

def is_allowed_email(email: str) -> bool:
    try:
        v = validate_email(email)
        domain = v["domain"]
        # block disposable domains, simple check list
        blocked = ["mailinator.com", "trashmail.com", "tempmail.com"]
        return domain not in blocked
    except EmailNotValidError:
        return False
