from typing import Callable, Dict, List, Type

import domain.book.event


class EventBus:
    def __init__(self):
        self.handlers: Dict[Type[domain.book.event.DomainEvent], List[Callable]] = {}

    def subscribe(
        self, event_type: Type[domain.book.event.DomainEvent], handler: Callable
    ):
        """Subscribe a handler to an event type."""
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    def publish(self, event: domain.book.event.DomainEvent):
        """Publish an event to all subscribed handlers."""
        if type(event) in self.handlers:
            for handler in self.handlers[type(event)]:
                handler(event)
