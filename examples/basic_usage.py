"""
The file to demostrate the basic usage of hash-make kit
"""

import redis
import hash_utils
from redis_helper_kit import * 


def hash_test():
        
        #make the instance of helper function
        helper_fun = redis_crud_operations.Helper_fun( host_name = "localhost")
        
        helper_fun.delete_db("primary_set")
        helper_fun.delete_db("secondary_set")
        
        hash_utils.generate_unique_hash("primary_set","secondary_set","localhost",5,10,100)

        # Connect to Redis server
        #client = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Retrieve and print all values in the set
        values = list(helper_fun.get_all_set_val(set_name = "primary_set"))

        pop_val = helper_fun.pop_set_val(set_name = "primary_set")
        print("Popped value:", pop_val)


        for val in values:

            print("Value in the set:", val)

        
        values2 = list(helper_fun.get_all_set_val(set_name = "secondary_set"))

        for val in values2:

            print("Value in the set2:", val)

        print("Length of primary set:", helper_fun.get_set_len(set_name = "primary_set"))
        print("Length of secondary set:", helper_fun.get_set_len(set_name = "secondary_set"))
 
        #helper_fun = redis_crud_operations.Helper_fun("test_hash","test_set","localhost")

        #for _ in range(10):

        #    val = helper_fun.pop_set_val()

        #    print(val)


print(hash_test())
