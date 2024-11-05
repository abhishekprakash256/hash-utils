
# Design Document for Hash Utils Project

## Project Overview

The **Hash Utils** project is designed to generate and manage unique random hashes using Python. It integrates with Redis to maintain a set of unique hashes, ensuring no duplicates and maintaining a specified quantity of pre-generated hashes.

## Objectives

- To provide utility functions for generating random and unique hashes.
- To leverage Redis as a storage layer for efficiently managing and retrieving unique hashes.
- To create reusable and scalable code that can be easily extended or integrated with other systems.

## Architecture

The project is organized into the following main components:

### Components

1. **`hash_maker.py`**
   - Responsible for generating random alphanumeric hashes of specified lengths.
   - Standalone function to generate hashes based on given parameters, making it reusable across different services.

2. **`unique_hash_generator.py`**
   - Manages the generation of unique hashes and stores them in Redis.
   - Includes functions for:
     - Checking the existence of hashes.
     - Adding unique hashes to a Redis set.
     - Pre-filling the Redis set with a specified quantity of unique hashes.

3. **Redis Helper Package (`redis_helper_kit`)**
   - External dependency that simplifies Redis CRUD operations.
   - Provides helper functions like `check_hash_exist`, `add_value_to_set`, and `create_redis_client`.
   - Stored on GitHub for version control and easy installation across different environments.

### Redis

The project uses Redis as a fast, in-memory database to store unique hashes in a set structure. The Redis set allows for automatic deduplication, simplifying the hash management.

## Data Flow

1. **Random Hash Generation (`hash_maker.py`)**
   - Generates random hashes on request, using alphanumeric characters.
   - Returns a hash of the specified length range (from `low` to `high`).

2. **Unique Hash Generation and Storage (`unique_hash_generator.py`)**
   - Calls `generate_random_hash` to create a hash.
   - Checks the Redis set to see if the hash exists using `redis_helper_kit`.
   - Adds the hash to the Redis set if it does not already exist.
   - Continues the process until the Redis set reaches the specified quantity of unique hashes (`hash_qty`).

## Dependencies

- **Python packages**:
  - `redis`: Python client for interacting with the Redis server.
  - `redis_helper_kit`: Custom Redis helper package hosted on GitHub for simplified Redis operations.

### Installation

To install `redis_helper_kit`:
```bash
pip install git+https://github.com/abhishekprakash256/redis-helper-kit.git
```

To install other dependencies:
```bash
pip install -r requirements.txt
```

## Design Decisions

- **Redis as a Storage Solution**: Chosen for its speed and efficiency with in-memory data, as well as its ability to automatically deduplicate entries in sets, making it ideal for managing unique hashes.
  
- **Modularization**: The project is divided into small, focused modules (`hash_maker.py`, `unique_hash_generator.py`) to enhance code readability, maintainability, and reusability.

- **Redis Helper Kit**: The decision to use an external helper package allows for easier Redis interaction, abstracting low-level CRUD operations. This helps in keeping the main project code cleaner and focused on core functionality.

## Example Usage

1. **Random Hash Generation**:
   ```python
   from hash_maker import generate_random_hash
   random_hash = generate_random_hash(5, 10)
   print(random_hash)
   ```

2. **Unique Hash Generation and Storage in Redis**:
   ```python
   from unique_hash_generator import generate_unique_hash
   generate_unique_hash("hash_name", "set_name", "localhost", 5, 10, 100)
   ```


## Conclusion

The **Hash Utils** project is designed to be a reusable and efficient solution for generating and managing unique hashes with Redis. With modular code, external dependencies, and Redis integration, the system is both flexible and scalable for use in larger applications or deployments.