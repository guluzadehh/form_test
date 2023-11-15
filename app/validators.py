from email_validator import validate_email, EmailNotValidError
import phonenumbers
from dateutil import parser

def is_valid_email(value: str) -> bool:
	try:
		validate_email(value, test_environment=True)
	except EmailNotValidError:
		return False

	return True
	
def is_valid_phone(value: str) -> bool:
	try:
		phone = phonenumbers.parse(value, "ru")
	except phonenumbers.NumberParseException:
		return False
	
	return phonenumbers.is_valid_number(phone)

def is_valid_date(value: str) -> bool:
	try:
		parser.parse(value)
	except ValueError:
		return False
	
	return True