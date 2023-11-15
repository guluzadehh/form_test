Сначала надо создать виртуальную среду для Python:

    python3 -m venv env

Далее, активируем эту среду:

    source env/bin/activate

Теперь, надо скачать нужные библиотеки:

    pip3 install -r requirements.txt

После успешной установки, надо будет запустить сервер:
    uvicorn app.main:app --reload

Ее вручную можно проверить переходя по ссылке: http://localhost:8000/docs.

Чтобы запустить тестовые запросы, надо запустить команду:

    python3 test_requests.py