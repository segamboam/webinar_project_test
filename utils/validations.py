# utils/validations.py
import re

def is_valid_email(email: str) -> bool:
    """
    Valida si el correo electrónico tiene el formato correcto.

    :param email: Correo electrónico a verificar.
    :return: True si el correo es válido, False si no lo es.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None
