from dataclasses import dataclass


@dataclass(frozen=True)
class User:
	name: str
	email: str
	hashed_password: str
