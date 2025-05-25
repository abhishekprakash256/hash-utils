from redis_helper_kit import * 
from unique_hash_generator import generate_unique_hash



def hash_test():
        
        generate_unique_hash("primary_set","secondary_set","localhost",5,10,100)

        # Connect to Redis server
        #client = redis.StrictRedis(host='localhost', port=6379, db=0)

        #make the instance of helper function
        helper_fun = redis_crud_operations.Helper_fun( host_name = "localhost")

        # Retrieve and print all values in the set
        values = list(helper_fun.get_all_set_val(set_name = "primary_set"))

        pop_val = helper_fun.pop_set_val(set_name = "primary_set")
        print("Popped value:", pop_val)
    
        length = helper_fun.get_set_len(set_name = "primary_set")
        print(length)
        
        for val in values:

            print("Value in the set:", val)