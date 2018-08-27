#random name
#random email
#random button?
import random
import string

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_email(length):
    return get_random_name(length) + '@' + get_random_domain(domains)