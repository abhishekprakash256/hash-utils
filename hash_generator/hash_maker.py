"""
The file to make hashes 

"""

import random 

def generate_random_hash(low,high):
    """
    The function to generates a random hash of the given length.
    """

    random_length = random.randint(low, high)
    hash = ""
    for i in range(random_length):
        hash += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return hash


