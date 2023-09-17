from django.core.exceptions import ValidationError
import string


def capitalLetterValidator(text):
    if not text[0] in string.ascii_uppercase:
        raise ValidationError
    else:
        return 0
