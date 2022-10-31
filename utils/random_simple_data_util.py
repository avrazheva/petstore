import random
import string


def generate_random_string(length: int = 5):
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def generate_random_digit(min: int = 0, max: int = 10000):
    return random.randint(min, max)


def generate_random_image_url(ext: str = "jpg"):
    return f"https:/some_image_site/{generate_random_string()}.{ext}"
