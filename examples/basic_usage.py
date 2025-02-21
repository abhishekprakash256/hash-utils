"""
The file to demostrate the basic usage of hash-make kit
"""

import redis
import hash_utils
from redis_helper_kit import * 


def hash_test():
        
        hash_utils.generate_unique_hash("test_hash","test_set","localhost",5,10,100)

        # Connect to Redis server
        client = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Set name
        redis_set_name = "test_set"  # Replace with your actual set name

        # Retrieve and print all values in the set
        values = client.smembers(redis_set_name)
        decoded_values = [val.decode('utf-8') for val in values]
        print("Values in the set:", decoded_values)


        helper_fun = redis_crud_operations.Helper_fun("test_hash","test_set","localhost")

        for _ in range(10):

            val = helper_fun.pop_set_val()

            print(val)


print(hash_test())
