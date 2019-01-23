import string
import random
from django.core.exceptions import ObjectDoesNotExist

def get_db_distinct(queryset, field, func, **params):
    """
    Checks if a field / value pair exists in database
    and continues generating values until it finds
    a one that does not exist
    func is the function that generates values and
    params is the parameters that function takes
    """
    while True:
        try:
            value = func(**params)
            queryset.get(**{field: value})
        except ObjectDoesNotExist:
            break
    return value

def random_string(**kwargs):
    """
    By default generates a random string of 10 chars composed
    of digits and ascii lowercase letters. String length and pool can
    be override by using kwargs. Pool must be a list of strings
    """
    n = kwargs.get('length', 10)
    pool = kwargs.get('pool') or string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(pool) for _ in range(n))
