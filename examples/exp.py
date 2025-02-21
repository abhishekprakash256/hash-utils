import fakeredis
from redis_helper_kit import * 
import hash_utils


server = fakeredis.FakeServer()

r1 = fakeredis.FakeStrictRedis(server=server)
r1.sadd("myset", "a", "b", "c")
print(r1.scard("myset"))


hash_utils.generate_unique_hash("test_hash","test_set","localhost",5,10,100,r1)

# Connect to Redis server
client = r1

# Set name
redis_set_name = "test_set"  # Replace with your actual set name

# Retrieve and print all values in the set
values = client.smembers(redis_set_name)
decoded_values = [val.decode('utf-8') for val in values]
print("Values in the set:", decoded_values)


helper_fun = redis_crud_operations.Helper_fun("test_hash","test_set","localhost",r1)

for _ in range(10):

    val = helper_fun.pop_set_val()

    print(val)


