"""
The file to generate the unique hash that check in redis hash and pre build a set of unique hashes 
"""

from redis_helper_kit import *
from .hash_maker import generate_random_hash



def generate_unique_hash(primary_set , secondary_set , host_name, low, high, hash_qty , redis_client = None):
    """
    The fucntion to make the unique hash by check the hash and filling the redis set as well
    Also maintains a prebuild amount of hash in the redis set as per hash_qty

    primary set : is the set that store the value freshly produced
    secondary_set : the set has the value that are actully used in the server
    """

    #print("in the generate unique hash function")

    if redis_client:

        helper_fun = redis_crud_operations.Helper_fun(redis_client = redis_client)
    
    else:
        #make the instance of the helper function
        helper_fun = redis_crud_operations.Helper_fun(host_name = host_name)
    
    #get the set length 
    set_len = helper_fun.get_set_len(primary_set)

    #print("set length is ", set_len)

    #check the length of the redis set
    while set_len < hash_qty:

        hash_val = generate_random_hash(low,high)

        #print("in")

        if not helper_fun.check_set_exist(hash_val, secondary_set):

            #print("in")
            
            #add the hash to redis set 
            helper_fun.add_value_to_set(hash_val , set_name = primary_set)
        
        set_len = helper_fun.get_set_len(primary_set)