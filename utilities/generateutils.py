import logging as logger
import random
import string

Generated_text = None


def generate_string(company_prefix=None):
    logger.info('Generate random string')
    if not company_prefix:
        company_prefix = 'Pharmateksol'

    random_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    company_name = company_prefix + ' ' + random_string
    random_info = {'company_name': company_name}
    return random_info


def generate_random_text():
    global Generated_text
    random_info = generate_string()
    logger.info(random_info)
    Generated_text = random_info['generated_text']  # Assign value to global variable
    return Generated_text


def generate_random_userName(user_name_prefix=None):
    logger.info('Generate random user name')
    if not user_name_prefix:
        user_name_prefix = 'testuser'
    random_string_length = 5
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_string_length))
    full_name = user_name_prefix + ' ' + random_string
    random_full_name = {'full_name': full_name}
    print(full_name)
    return random_full_name
