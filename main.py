from dataclasses import dataclass

@dataclass(frozen=True)
class User:
  first_name: str
  last_name: str
  second_name: str | None = None


def awesome_function():
  return 'I am the best one'



def create_user(first_name: str, last_name: str) -> User:
  return User(first_name, last_name)
