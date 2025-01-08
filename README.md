# domain-driven-design-example

```
.
├── application                 # Exposes domain logic
│   └── book
│       ├── command.py          # Schemas for things we want to do
│       ├── event.py            # Schemas for events
│       ├── event_bus.py        # Manages events
│       ├── query.py            # Schemas for things we want to ask
│       ├── service.py          # Interacts with domain
│       └── use_case.py         # Executes commands and queries
├── domain
│   └── book
│       ├── entity.py           # The dataclasses of things we track
│       ├── event.py            # Schemas for events
│       ├── repository.py       # Abstract repository
│       └── value_object.py     # dataclases of things we don't track
├── infrastructure
│   └── book
│       ├── event_handler.py    # Functions to handle events from the domain
│       └── repository.py       # Implements the repository (SQLite3, In-memeory, etc)
└── interface
    └── main.py                 # Where we compose our service (CLI, API, etc)
```