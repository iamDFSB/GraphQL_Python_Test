from typing import List
import strawberry

from model_function import create_user, catch_users, upgrade_user, remove_user
from models import User, ErrorMessageUser


@strawberry.type
class Query:
    get_user: List[User] = strawberry.field(resolver=catch_users)


@strawberry.type
class Mutation:
    add_user: User  = strawberry.mutation(resolver=create_user)
    delete_user: User = strawberry.mutation(resolver=remove_user)
    update_user: User = strawberry.mutation(resolver=upgrade_user)



schema = strawberry.Schema(query=Query, mutation=Mutation)

