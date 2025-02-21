"""
The file to test the hashes made 
"""
import pytest
import hash_utils
import fakeredis
from redis_helper_kit import * 
from unittest.mock import MagicMock, patch


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



@patch("redis_helper_kit.create_redis_client")  # Mock Redis client
@patch("redis_helper_kit.redis_crud_operations.Helper_fun")  # Mock Helper_fun class
def test_generate_unique_hash(mock_helper_fun, mock_redis_client):
    """Test generate_unique_hash to ensure unique hashes are added to Redis."""

    # Mock Redis set length operations
    mock_redis = MagicMock()
    mock_redis.scard.side_effect = [0, 1, 2, 3, 4, 5]  # Simulate growing set
    mock_redis_client.return_value = mock_redis  # Mock Redis client return

    # Mock Helper_fun behavior
    mock_helper = MagicMock()
    mock_helper.check_hash_exist.return_value = False  # Simulate hash doesn't exist
    mock_helper.add_value_to_set.side_effect = lambda x: None  # Simulate adding

    mock_helper_fun.return_value = mock_helper  # Mock Helper_fun return

    # Run the function
    hash_utils.generate_unique_hash("test_hash", "test_set", "localhost", 5, 10, 5)

    # Validate Redis operations
    assert mock_redis.scard.call_count > 1  # Ensure it checked Redis set multiple times
    assert mock_helper.add_value_to_set.call_count == 5  # 5 unique hashes should be added
    assert mock_helper.check_hash_exist.call_count >= 5  # Ensure it checked for duplicates

    print("Test Passed: Unique hashes are generated correctly.")



