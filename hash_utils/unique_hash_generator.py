"""
The file to generate the unique hash that check in redis hash and pre build a set of unique hashes 
"""

from redis_helper_kit import *
from .hash_maker import generate_random_hash



def generate_unique_hash(hash_name,set_name,host_name,low,high,hash_qty , redis_client = None):
    """
    The fucntion to make the unique hash by check the hash and filling the redis set as well
    Also maintains a prebuild amount of hash in the redis set as per hash_qty
    """

    #make the instance of the helper function
    helper_fun = redis_crud_operations.Helper_fun(hash_name,set_name,host_name , redis_client)
    
    #make client on condn
    if redis_client:
        redis_client = redis_client
    else:
        redis_client = create_redis_client(host_name)


    #get the set length 
    set_len = redis_client.scard(set_name)

    #check the length of the redis set
    while set_len < hash_qty:

        hash_val = generate_random_hash(low,high)

        if not helper_fun.check_hash_exist(hash_val):
            
            #add the hash to redis set 
            helper_fun.add_value_to_set(hash_val)
        
        set_len = redis_client.scard(set_name)


