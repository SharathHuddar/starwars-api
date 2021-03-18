from starwars_service import InvalidUsage


def assert_true(condition, message='Bad Request'):
    if not condition:
        raise InvalidUsage(message=message)