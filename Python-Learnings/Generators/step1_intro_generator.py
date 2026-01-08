"""
STEP 1: INTRODUCTION TO GENERATORS
==================================

What is a Generator?
--------------------
A generator is a special type of iterator that generates values on-the-fly
using the 'yield' keyword instead of 'return'. Unlike regular functions that
return a value and terminate, generators can pause execution and resume later.

Key Concepts:
1. Generators are lazy - they don't compute values until needed
2. They use 'yield' instead of 'return'
3. They maintain their state between calls
4. They are memory efficient - generate one value at a time
"""


# ============================================================================
# EXAMPLE 1: Your First Generator Function
# ============================================================================

def simple_counter(max_count):
    """
    A simple generator that counts from 1 to max_count.
    
    Notice:
    - Uses 'yield' instead of 'return'
    - Execution pauses at each yield
    - State is preserved between calls
    """
    count = 1
    while count <= max_count:
        yield count  # Pauses here and returns count
        count += 1   # Resumes here on next call


# Let's use it:
print("=" * 60)
print("EXAMPLE 1: Simple Counter Generator")
print("=" * 60)

# Create a generator object
counter = simple_counter(5)
print(f"Type of counter: {type(counter)}")
print(f"Is it an iterator? {hasattr(counter, '__iter__')}")
print(f"Is it an iterable? {hasattr(counter, '__next__')}")

# Iterate through the generator
print("\nValues from generator:")
for num in counter:
    print(f"  Got: {num}")

# Try iterating again - generators are exhausted after use!
print("\nTrying to iterate again (generator is exhausted):")
for num in counter:
    print(f"  Got: {num}")  # This won't print anything!


# ============================================================================
# EXAMPLE 2: Generator vs Regular Function
# ============================================================================

def regular_function(n):
    """Regular function - returns a list"""
    result = []
    for i in range(1, n + 1):
        result.append(i ** 2)
    return result


def generator_function(n):
    """Generator function - yields values one at a time"""
    for i in range(1, n + 1):
        yield i ** 2


print("\n" + "=" * 60)
print("EXAMPLE 2: Generator vs Regular Function")
print("=" * 60)

# Regular function - creates entire list in memory
regular_result = regular_function(5)
print(f"Regular function result: {regular_result}")
print(f"Type: {type(regular_result)}")
print(f"Memory: All 5 values stored at once")

# Generator function - creates values on demand
generator_result = generator_function(5)
print(f"\nGenerator function result: {generator_result}")
print(f"Type: {type(generator_result)}")
print(f"Memory: Values generated one at a time")

# To see the values, we need to iterate
print("\nValues from generator:")
for value in generator_result:
    print(f"  {value}")


# ============================================================================
# EXAMPLE 3: Understanding the Execution Flow
# ============================================================================

def execution_demo():
    """
    This demonstrates how execution pauses and resumes.
    Run this step by step to see the flow!
    """
    print("  Step 1: Starting function")
    yield "First value"
    print("  Step 2: After first yield")
    yield "Second value"
    print("  Step 3: After second yield")
    yield "Third value"
    print("  Step 4: Function ending")


print("\n" + "=" * 60)
print("EXAMPLE 3: Understanding Execution Flow")
print("=" * 60)

demo = execution_demo()
print("Generator created, but nothing executed yet!")
print("\nCalling next() for the first time:")
print(f"  Got: {next(demo)}")

print("\nCalling next() for the second time:")
print(f"  Got: {next(demo)}")

print("\nCalling next() for the third time:")
print(f"  Got: {next(demo)}")

print("\nTrying next() one more time (will raise StopIteration):")
try:
    print(f"  Got: {next(demo)}")
except StopIteration:
    print("  ✓ Generator exhausted - StopIteration raised (this is normal!)")


# ============================================================================
# HANDS-ON EXERCISE 1: Your Turn!
# ============================================================================

print("\n" + "=" * 60)
print("HANDS-ON EXERCISE 1")
print("=" * 60)
print("""
Create a generator function called 'even_numbers' that:
1. Takes a parameter 'n' (maximum number)
2. Yields all even numbers from 2 to n (inclusive)

Example: even_numbers(10) should yield: 2, 4, 6, 8, 10

Try it yourself below, then uncomment the test code:
""")

# TODO: Write your generator function here
# def even_numbers(n):
#     # Your code here
#     pass

# Test your function:
# print("\nTesting even_numbers(10):")
# for num in even_numbers(10):
#     print(f"  {num}")


# ============================================================================
# KEY TAKEAWAYS FROM STEP 1
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Generators use 'yield' instead of 'return'
2. They pause execution at yield and resume on next call
3. They maintain state between calls
4. They're memory efficient - generate values on demand
5. Once exhausted, they can't be reused (need to create new generator)
6. They automatically raise StopIteration when done

Next: Move to step2_generator_vs_functions.py to learn about
      memory efficiency and when to use generators!
""")
