#import hash_utils

#hash_utils.generate_unique_hash("test_hash","test_set","localhost",5,10,100)

import redis

# Connect to Redis server
client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Set name
redis_set_name = "test_set"  # Replace with your actual set name

# Retrieve and print all values in the set
values = client.smembers(redis_set_name)
decoded_values = [val.decode('utf-8') for val in values]
print("Values in the set:", decoded_values)

from redis_helper_kit import * 

helper_fun = redis_crud_operations.Helper_fun("test_hash","test_set","localhost")

