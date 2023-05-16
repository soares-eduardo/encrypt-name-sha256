import hashlib

first_name = "Jessica"
number = 0

def has_30_leading_zeros(hash_value):
    if hash_value.startswith('0' * 7):
        return True
    return False


def calculate_hash_value(name_and_number):
    hash_object = hashlib.sha256(name_and_number.encode('utf-8'))
    hash_value = hash_object.hexdigest()
    return hash_value


while True:
    name_and_number = first_name + str(number)
    hash_value = calculate_hash_value(name_and_number)
    has_30_zeros = has_30_leading_zeros(hash_value)

    if has_30_zeros:
        print(hash_value)
        print(name_and_number)
        break
    else:
        number += 1
