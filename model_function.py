import json
from typing import List
from models import User, User, Messages


def catch_users() -> List[User]:
    contents = []
    with open('users.json') as file:
        content_str = file.read()
        contents = json.loads(content_str)

    user_list = [
        User(id=user["id"], name=user["name"], age=user["age"], message=Messages.SUCCESS.value[0])
        for user in contents
    ]

    return user_list


def create_user(name: str, age: int) -> User | User:
    if age >= 100:
        return User(
            id=0,
            name=name,
            age=age,
            message=Messages.ERROR_AGE_HIGH.value[0]
        )

    users = []
    with open('users.json') as file:
        content_str = file.read()
        users = json.loads(content_str)

    qtd = len(users)
    new_user = {
        "id": qtd + 1,
        "name": name,
        "age": age
    }

    users.append(new_user)

    with open('users.json', 'w') as file:
        json_users = json.dumps(users, indent=3)
        file.write(json_users)

    user_formatted = User(
        id=new_user["id"],
        name=new_user["name"],
        age=new_user["age"],
        message=Messages.SUCCESS.value[0]
    )

    return user_formatted

def remove_user(id: int) -> User | User:
    users = []
    with open('users.json') as file:
        content_str = file.read()
        users = json.loads(content_str)

    qtd = len(users) - 1

    if id > qtd or id < 0:
        return User(
            id=id,
            name="",
            age=0,
            message=Messages.ERROR_OUT_OF_RANGE.value[0]
        )

    user_removed = users[id]

    users.pop(id)

    users = [
        {
            "id": index,
            "name": user["name"],
            "age": user["age"]
        }
        for index, user in enumerate(users)
    ]

    with open('users.json', 'w') as file:
        json_users = json.dumps(users, indent=3)
        file.write(json_users)

    user_formatted = User(
        id=user_removed["id"],
        name=user_removed["name"],
        age=user_removed["age"],
        message=Messages.SUCCESS.value[0]
    )

    return user_formatted


def upgrade_user(id: int, name: str, age: int) -> User | User:
    if age >= 100:
        return User(
            id=id,
            name=name,
            age=age,
            message=Messages.ERROR_AGE_HIGH.value[0]
        )

    users = []
    with open('users.json') as file:
        content_str = file.read()
        users = json.loads(content_str)

    qtd = len(users) - 1

    user_updated = {
        "id": id,
        "name": name,
        "age": age
    }

    if id > qtd or id < 0:
        return User(
            id=id,
            name=name,
            age=age,
            message=Messages.ERROR_OUT_OF_RANGE.value[0]
        )

    users[id] = user_updated

    with open('users.json', 'w') as file:
        json_users = json.dumps(users, indent=3)
        file.write(json_users)

    user_formatted = User(id=id, name=name, age=age, message=Messages.SUCCESS.value[0])

    return user_formatted