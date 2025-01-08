from dataclasses import dataclass


@dataclass(frozen=True)
class ISBN:
    value: str
