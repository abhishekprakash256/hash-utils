"""
The file to test the hashes made 
"""
import pytest
import hash_utils
import fakeredis
from redis_helper_kit import * 




def test_hash_maker():
    """
    The function to test the hash maker    
    """
    low, high, times = 5, 10, 200  

    for _ in range(times):

        gen_hash = hash_utils.generate_random_hash(low, high)

        assert low <= len(gen_hash) <= high

        # Check characters (alphanumeric only)
        assert all(c.isalnum() for c in gen_hash), f"Invalid character in hash: {gen_hash}"





