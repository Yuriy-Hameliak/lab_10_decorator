import time
import functools

# --------------------------------------
# 1. Explanation of Decorators in Python
# --------------------------------------
"""
Decorators in Python are functions that modify the behavior of another function or method.
They are often used to:
- Add functionality without modifying the original function's code.
- Log function execution, manage access (e.g., authentication/authorization), or retry logic.

A decorator is implemented as a higher-order function that takes a function as input and returns a new function.
"""

# --------------------------------------
# 2. Implementation of @square Decorator
# --------------------------------------
def square(func):
    """
    A decorator that squares the result of a function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return wrapper

@square
def add(a, b):
    """Adds two numbers."""
    return a + b

# Testing @square decorator
print("Square Decorator Test:")
print("add(2, 3) squared:", add(2, 3))  # Output: 25

# -------------------------------------------------------
# 3. Authentication vs. Authorization and Decorators
# -------------------------------------------------------
"""
Authentication:
- Verifies the identity of a user (e.g., login with username/password).

Authorization:
- Determines whether a user has permissions to access a specific resource.

Decorators are important in web frameworks (e.g., Flask, Django) for handling these tasks:
- Authentication: Check if the user is logged in.
- Authorization: Verify if the user has permission to access a resource.
"""

# Example: Authentication/Authorization Decorators
def authenticated(func):
    """A decorator that checks if a user is authenticated."""
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise PermissionError("User not authenticated")
        return func(user, *args, **kwargs)
    return wrapper

def authorized(role):
    """A decorator that checks if a user has the required role."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError(f"User not authorized for role {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@authenticated
@authorized("admin")
def view_admin_dashboard(user):
    """Example function for admin dashboard access."""
    return "Admin Dashboard Access Granted"

# Testing Authentication and Authorization
try:
    user = {"is_authenticated": True, "role": "admin"}
    print("\nAuthentication/Authorization Test:")
    print(view_admin_dashboard(user))  # Success
except PermissionError as e:
    print(e)

# --------------------------------------
# 4. Implementation of @retry Decorator
# --------------------------------------
def retry(retries=3, delay=2):
    """
    A decorator that retries a function call if it raises an exception.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying... ({attempts + 1}/{retries}) due to error: {e}")
                    attempts += 1
                    time.sleep(delay)
            raise RuntimeError(f"Function failed after {retries} attempts")
        return wrapper
    return decorator

@retry(retries=3, delay=1)
def unstable_function():
    """Simulates an unstable function that fails randomly."""
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

# Testing @retry decorator
print("\nRetry Decorator Test:")
try:
    print(unstable_function())
except RuntimeError as e:
    print(e)
