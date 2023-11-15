import json
import requests

BASE_URL = "http://localhost:8000/get_form"

def show_forms(fields: list[dict[str, str]]):
	for field in fields:
		print("\n\nФормы с полями:")

		for name, value in field.items():
			print(f"\t{ name }: { value }")

		res = requests.post(BASE_URL, json=field, headers={'Accept': 'application/json'})

		print("\n", res.json())

def main():
	with open("db.json", "r") as db_file:
		data = db_file.readline()
		data = json.dumps(json.loads(data)["_default"], indent=2)
		print(data)

	show_forms([
		{
			"email_field": "user@test.com"
		},
		{
			"lead_email": "user12@test.com",
		},
		{
			"email_field": "not_email"
		},
		{
			"email_field": "user@test.com",
			"phone_field": "+7 928 166 31 34"
		},
		{
			"email_field": "user@test.com",
			"phone_field": "+7 928 166 31 wr"
		},
		{
			"phone_number_field": "+7 928 166 31 34",
		},
		{
			"created_at": "20.04.2012",
		},
		{
			"main_text": "Some text",
			"date_field": "20.04.2012",
		},
		{
			"email_field": "user@test.com",
			"created_at": "2022-07-24"
		},
		{
			"date_field": "not a date"
		},
		{
			"text_field": "Some text"
		}
	])

main()