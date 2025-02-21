
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

## Start the docker container 

```bash
docker pull redis

docker run -d --name redis --network my_network -p 6379:6379 redis:latest
```

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

## Run the example file 

```bash
 python3 -m examples.basic_usage

```
Run this in root dir

## Usage

To generate unique hashes and store them in Redis, run:

```python
from unique_hash_generator import generate_unique_hash

# Example configuration
generate_unique_hash("hash_name", "set_name", "localhost", 5, 10, 50)
```

This will generate unique hashes between 5 and 10 characters and store them in Redis under the specified set name until there are 50 unique hashes stored.

## **1. Development & Branching Strategy**
This project follows a **structured Git workflow** with three main branch categories:  

### **🔹 `main` (Production)**
- The most **stable** branch containing **production-ready** code.  
- Only **tested and reviewed** changes are merged here.  
- **Deployment to production happens from `main`**.

### **🔹 `test` (Staging/Testing)**
- Used for **integration testing** before merging into `main`.  
- Acts as a **buffer** between `feature` branches and `main`.  
- **Continuous Integration (CI)** runs automated tests on this branch.  

### **🔹 `feature/*` (Feature Development)**
- Used for **new features, bug fixes, or improvements**.  
- **Naming Convention:**  
  - `feature/<feature-name>` (e.g., `feature/authentication`, `feature/api-refactor`)  
  - `bugfix/<bug-name>` (e.g., `bugfix/payment-error`)  
- Merged into `test` after development is complete.  

---

## **2. Git Workflow: Step-by-Step Guide**
### **🔹 Step 1: Creating a New Feature Branch**
Every new feature or bug fix starts from the latest `test` branch.

```bash
git checkout test
git pull origin test  # Ensure latest updates
git checkout -b feature/new-feature  # Create a new branch
```

Work on your feature, commit changes, and push to remote:

```bash
git add .
git commit -m "Added new feature: X"
git push origin feature/new-feature
```

---

### **🔹 Step 2: Merging Feature Branch into `test`**
Once development is complete, **create a Pull Request (PR)** from `feature/new-feature` → `test`.

- ✅ Ensure **all tests pass** before merging.
- ✅ Conduct **code reviews** for quality control.

If everything is fine, **merge into `test`**:

```bash
git checkout test
git pull origin test
git merge feature/new-feature
git push origin test
```

After merging, delete the feature branch:

```bash
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

### **🔹 Step 3: Merging `test` into `main`**
After multiple features are tested in `test`, merge into `main` for release.

```bash
git checkout main
git pull origin main
git merge test
git push origin main
```

🚀 **Deploy the `main` branch to production after merging!**

---

## **5. Best Practices for Git Workflow**
✅ **Keep `main` clean** → Never push directly to `main`; always merge from `test`.  
✅ **Frequent sync** → Regularly update `feature` branches from `test` to prevent merge conflicts.  
✅ **Use descriptive branch names** → Example: `feature/user-auth`, `bugfix/payment-error`.  
✅ **Delete merged branches** → Keep the repository clean by removing feature branches after merging.  
✅ **Code reviews & CI/CD** → Run automated tests on `test` before merging into `main`.  

---

## **3. Example Git Workflow**
```bash
# Create and work on a feature branch
git checkout test
git pull origin test
git checkout -b feature/new-api

# Work on code...
git add .
git commit -m "Implemented new API feature"
git push origin feature/new-api

# Merge into test after review
git checkout test
git pull origin test
git merge feature/new-api
git push origin test

# Merge tested code into main
git checkout main
git pull origin main
git merge test
git push origin main
```

---

## **4. Running Tests with Pytest**
To run **unit tests** locally:
```bash
pytest --maxfail=5 --disable-warnings -v
```
- **`--maxfail=5`** → Stops execution after **5 failures**.  
- **`--disable-warnings`** → Suppresses warnings for cleaner output.  
- **`-v`** → Enables **verbose output** for better debugging.  

---

## **5. Automated Testing with GitHub Actions**
The project uses **GitHub Actions** to run tests on every push or pull request.

### **📌 GitHub Actions Workflow (`.github/workflows/ci.yml`)**
```yaml
name: Run Pytest

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
      - test
      - "feature/**"

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'  # Change to match your project

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run pytest
        run: pytest -v
```

🚀 **Now, every commit gets tested automatically!**  

---

## **6. Deployment Strategy**
- **Staging (`test`)**: Run CI/CD tests before merging to `main`.  
- **Production (`main`)**: After merging from `test`, deploy the latest stable code.  

---

### **📌 Summary**
✅ **Structured Git workflow** with `main`, `test`, and `feature` branches.  
✅ **Automated testing** with `pytest` and GitHub Actions.  
✅ **Best practices** for feature development, merging, and deployment.  
✅ **Easy setup** with Redis (bare-metal or Docker)


