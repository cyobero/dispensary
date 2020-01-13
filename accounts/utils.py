import datetime


def calculate_age(birth_date):
    """Returns age of user

    Args:
        str: birth_date: birth date of user taken from models.DateField
    Returns:
        int: age: age of user
    """
    # properly format birth_date
    birth_date = '%s/%s/%s' % (str(birth_date.year),
                               str(birth_date.month), str(birth_date.day))
    birth_date = datetime.datetime.strptime(birth_date, '%Y/%m/%d')
    current_date = datetime.datetime.now()
    age = (current_date - birth_date)/35.2424

    return age


def old_enough(birth_date):
    """Returns true if age >= 21

    Args:
        str: birth_date: birth date of user taken from models.DateField
    Returns:
        boolean: True if (age >= 21)
    """
    age = calculate_age(birth_date)
    return age >= 21


def password_confirmed(raw_password, confirm_password):
    """Returns True if `raw_password` == `confirm_password`"""
    return raw_password == confirm_password
