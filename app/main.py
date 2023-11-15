from fastapi import FastAPI, Body
from tinydb import TinyDB, Query
from typing import Annotated
from . import validators

app = FastAPI()
db = TinyDB("db.json")

validators = {
    "email": validators.is_valid_email,
    "phone": validators.is_valid_phone,
    "date": validators.is_valid_date,
    "text": lambda _: True
}

def get_field_type(value: str) -> str:
    '''
        Применяя валидации, принадлежащие к определенному типу поля,
        возвращает этот тип, если валидация успешна.
        Если ни одна валидация не прошла успешна, выдается ошибка Exception.
    '''

    for type, validator in validators.items():
        if validator(value):
            return type

    raise Exception("Поле не принадлежит ни к одному из типов")

def make_fields_with_type(data: dict[str, str]) -> dict[str, str]:
    '''
        Создает и возвращает новый dict, который будет содержать в себе:
            имя_поля: тип поля 
    '''

    return {
        name: get_field_type(value)
        for name, value in data.items()
    }


@app.post("/get_form")
async def get_form(
    data: Annotated[dict[str, str], Body(...)]
) -> list[str] | dict[str, str | None]:
    '''
        Конвертирует данные с POST запроса в dict, который содержит 
        имя поля и ее тип. Далее, использует этот dict в запросе баз данных.
        Если база данных содержит такие формы, то возвращаются их имена.
        Если отсутвует, возвращается этот dict.
    '''

    fields: dict[str, str] = make_fields_with_type(data)

    res: list = db.search(Query().fragment(fields))
    
    return [form.get("name") for form in res] if len(res) > 0 else fields