from pprint import pprint

from utils import get_users_in_state, get_entities_data

users = get_users_in_state("Louisiana")
print(get_entities_data("todos"))
pprint(users)
