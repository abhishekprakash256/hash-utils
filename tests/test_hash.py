"""
Unit tests for hash generation and Redis set operations.
"""

import pytest
import hash_utils
import fakeredis
from redis_helper_kit import redis_crud_operations

# Constants for test parameters
LOW, HIGH, TIMES = 5, 10, 200  
HASH_SET_KEY = "test_set"

@pytest.fixture
def fake_redis_client():
    """Fixture to create a shared FakeRedis client."""
    server = fakeredis.FakeServer()
    return fakeredis.FakeStrictRedis(server=server)


def test_hash_maker():
    """
    Test the random hash generator function:
    - Ensures generated hashes have the correct length.
    - Ensures hashes contain only alphanumeric characters.
    """
    for _ in range(TIMES):
        gen_hash = hash_utils.generate_random_hash(LOW, HIGH)

        assert LOW <= len(gen_hash) <= HIGH, f"Hash length {len(gen_hash)} out of bounds"
        assert gen_hash.isalnum(), f"Invalid character found in hash: {gen_hash}"


def test_hash_generator(fake_redis_client):
    """
    Test the hash generator function with Redis set operations:
    1. Generate 100 hashes and store them in a Redis set.
    2. Pop 10 values from the set.
    3. Verify that 90 values remain.
    4. Generate another 100 hashes.
    5. Ensure the total count resets to 100.
    """

    # Step 1: Generate and store 100 unique hashes in Redis
    hash_utils.generate_unique_hash("test_hash", HASH_SET_KEY, None, 5, 10, 100, redis_client=fake_redis_client)

    # Step 2: Create a helper instance
    helper_fun = redis_crud_operations.Helper_fun("test_hash", HASH_SET_KEY, None, fake_redis_client)

    # Step 3: Pop 10 values from the set
    for _ in range(10):
        helper_fun.pop_set_val()

    # Step 4: Validate remaining count is 90
    assert fake_redis_client.scard(HASH_SET_KEY) == 90, "Expected 90 hashes remaining after popping 10"

    # Step 5: Generate another 100 hashes
    hash_utils.generate_unique_hash("test_hash", HASH_SET_KEY, None, 5, 10, 100, redis_client=fake_redis_client)

    # Step 6: Validate the total count is reset to 100
    assert fake_redis_client.scard(HASH_SET_KEY) == 100, "Expected hash set count to be 100 after regeneration"
