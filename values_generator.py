import random
from database.models import Role
from random_date import birthdate


def values_gen(session):
    rand_date = birthdate()
    min_role_id = session.execute('SELECT id FROM roles ORDER BY id LIMIT 1')
    max_role_id = session.execute('SELECT id FROM roles ORDER BY id DESC LIMIT 1')
    rand_role = random.randint(min_role_id.scalar(), max_role_id.scalar())
    # Костыль, так как sqlite не позволяет использовать BIGINT в качестве первичного ключа с автоинкрементом
    last_id = session.execute('SELECT id FROM users ORDER BY rowid DESC LIMIT 1')
    if last_id is None:
        new_id = 10000
    else:
        new_id = last_id.scalar() + 1

    return new_id, rand_date, rand_role
