# kadr.project — Жұман Аян фотостудиясы

Django арқылы ашылатын лендинг (залдар, бағалар, брондау формасы).

## Жергілікті компьютерде іске қосу

```bash
cd kadr.project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Содан кейін браузерде ашыңыз: http://127.0.0.1:8000/

## Құрылымы

```
kadr.project/
├── manage.py
├── requirements.txt
├── kadrproject/        # Django баптаулары (settings, urls, wsgi/asgi)
└── landing/            # Лендинг қосымшасы
    ├── views.py        # index() — басты бетті шығарады
    ├── urls.py
    └── templates/landing/index.html   # HTML5 + CSS3 лендинг
```

## GitHub-қа жүктеу

Репозиторийге осы `kadr.project` қалтасының ішіндегісін толығымен қосыңыз
(`.gitignore` файлы `venv/` мен `__pycache__/`-ды қоспайды).
