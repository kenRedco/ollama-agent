# backend/tools/email_tool.py
import smtplib, ssl
from email.message import EmailMessage
from langchain.tools import Tool
from config import EMAIL_ADDRESS, EMAIL_APP_PASSWORD, DRY_RUN

def send_email_smtp(to: str, subject: str, body: str) -> str:
    if DRY_RUN:
        return f"[DRY RUN] Would send email to {to} with subject '{subject}'."
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context)
            server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
            server.send_message(msg)
        return f"EMAIL_SENT {to}"
    except Exception as e:
        return f"EMAIL_FAILED: {str(e)}"

email_tool = Tool(
    name="send_email",
    func=send_email_smtp,
    description="Send an email. Inputs: 'to, subject, body' as a single string or CSV. Returns status."
)
