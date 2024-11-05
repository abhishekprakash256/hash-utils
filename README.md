
# Hash Utils

This project contains utility functions to generate random and unique hashes. It includes a Redis integration to store unique hashes and manage a predefined quantity of unique hashes within a Redis set.

## Files

### `hash_maker.py`

This file contains the function to generate random hashes of a specified length.

#### Functions

- **`generate_random_hash(low, high)`**:
  - Generates a random alphanumeric hash.
  - Parameters:
    - `low` (int): Minimum length of the hash.
    - `high` (int): Maximum length of the hash.
  - Returns:
    - A randomly generated hash as a string.

  Example usage:
  ```python
  from hash_maker import generate_random_hash

  # Generate a random hash between lengths 5 and 10
  random_hash = generate_random_hash(5, 10)
  print(random_hash)
  ```

### `unique_hash_generator.py`

This file provides a function to generate unique hashes that are stored in a Redis set to ensure no duplicates. The function checks Redis to maintain a specified number of unique hashes in a prebuilt set.

#### Dependencies

- Requires the `redis_helper_kit` package to interact with Redis, specifically `redis_crud_operations` and `create_redis_client`.

#### Functions

- **`generate_unique_hash(hash_name, set_name, host_name, low, high, hash_qty)`**:
  - Generates unique hashes and maintains them in a Redis set.
  - Parameters:
    - `hash_name` (str): The name of the Redis hash.
    - `set_name` (str): The name of the Redis set.
    - `host_name` (str): The Redis server hostname.
    - `low` (int): Minimum length for generated hashes.
    - `high` (int): Maximum length for generated hashes.
    - `hash_qty` (int): Desired quantity of unique hashes in Redis.
  - Uses helper functions from `redis_helper_kit` to interact with Redis, checking for hash existence and adding values to the set.

  Example usage:
  ```python
  from unique_hash_generator import generate_unique_hash

  # Generate unique hashes in Redis
  generate_unique_hash("my_hash", "my_set", "localhost", 5, 10, 100)
  ```

## Requirements

This project requires the following Python packages:

- `redis`
- `redis_helper_kit` (available from [GitHub](https://github.com/abhishekprakash256/redis-helper-kit.git))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install the Redis helper kit:
   ```bash
   pip install git+https://github.com/abhishekprakash256/redis-helper-kit.git
   ```

## Usage

To generate unique hashes and store them in Redis, run:

```python
from unique_hash_generator import generate_unique_hash

# Example configuration
generate_unique_hash("hash_name", "set_name", "localhost", 5, 10, 50)
```

This will generate unique hashes between 5 and 10 characters and store them in Redis under the specified set name until there are 50 unique hashes stored.

## License

This project is licensed under the MIT License.

