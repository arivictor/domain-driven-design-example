# domain-driven-design-example

my_app/
  ├── src/
  │   ├── domain/
  │   │   ├── domain1/
  │   │   │   ├── entities.py
  │   │   │   ├── services.py
  │   │   │   └── value_objects.py
  │   │   ├── domain2/
  │   │   │   ├── entities.py
  │   │   │   ├── services.py
  │   │   │   └── value_objects.py
  │   │   └── __init__.py
  │   ├── application/
  │   │   ├── domain1/
  │   │   │   ├── commands.py
  │   │   │   ├── queries.py
  │   │   │   └── use_cases.py
  │   │   ├── domain2/
  │   │   │   ├── commands.py
  │   │   │   ├── queries.py
  │   │   │   └── use_cases.py
  │   │   └── __init__.py
  │   ├── infrastructure/
  │   │   ├── database/
  │   │   │   ├── repositories.py
  │   │   │   └── models.py
  │   │   ├── messaging/
  │   │   │   └── celery_app.py
  │   │   ├── external_apis/
  │   │   ├── config.py
  │   │   └── __init__.py
  │   ├── interfaces/
  │   │   ├── http_api/
  │   │   │   ├── fastapi_app.py
  │   │   │   └── routers/
  │   │   ├── cli/
  │   │   └── __init__.py
  │   └── __init__.py
  ├── workers/
  │   ├── celery_tasks.py
  │   └── __init__.py
  ├── tests/
  │   ├── unit/
  │   ├── integration/
  │   └── __init__.py
  ├── requirements.txt
  └── README.md