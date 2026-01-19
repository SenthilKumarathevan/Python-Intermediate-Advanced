# Python Generators — First Principles to Practical Use

**Main goal:** Explain Python generators from first principles and provide progressively structured, well-commented examples that you can run and experiment with in a Jupyter notebook inside VS Code.

---

## 1. Why generators exist (the problem they solve)

In Python, many tasks involve producing a sequence of values:

- Reading lines from a file
- Iterating over large datasets
- Producing values one-by-one in a loop

A common beginner approach is to build a list and return it. This works, but it has a drawback:

- The entire list must be stored in memory before you can use it.

**Generators solve this by producing one value at a time, on demand.**

---

## 2. First comparison: list vs generator (mental model)

### List (eager evaluation)

- All values are created immediately
- Stored in memory

### Generator (lazy evaluation)

- Values are created only when requested
- Uses much less memory
- Remembers where it left off

Keep this sentence in mind:

> **A generator is a function that pauses and resumes execution.**

---

## 3. Your first generator: replacing `return` with `yield`

Example: numbers from 1 to 3

```python
def number_generator():
    yield 1
    yield 2
    yield 3
````

### What is happening?

* `yield` produces a value and pauses the function
* The function resumes from the next line when asked again

---

## 4. Calling a generator (important beginner detail)

```python
gen = number_generator()
```

At this point:

* The function has **not executed**
* `gen` is a **generator object**

Check it:

```python
gen
```

You will see something like:

```
<generator object number_generator at 0x...>
```

---

## 5. Getting values using `next()`

```python
next(gen)  # First value
next(gen)  # Second value
next(gen)  # Third value
```

### What happens internally?

1. Python runs the function until the first `yield`
2. Returns that value
3. Pauses execution
4. Continues from the next line on the next call

If you call `next(gen)` again after all values are exhausted:

```python
next(gen)
```

You will get:

```
StopIteration
```

This signals that the generator is finished.

---

## 6. Using generators in a `for` loop (most common usage)

You rarely use `next()` manually in real code.

```python
for value in number_generator():
    print(value)
```

### Why this works

* `for` automatically calls `next()`
* It stops cleanly when `StopIteration` is raised

---

## 7. Generator with a loop (realistic pattern)

```python
def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1
```

Run it in a Jupyter cell:

```python
for number in count_up_to(5):
    print(number)
```

### Key learning points

* Local variables (`current`) are remembered
* The function resumes exactly where it paused

---

## 8. Comparing memory usage (conceptual example)

### List version

```python
def list_version(n):
    return [i for i in range(n)]
```

### Generator version

```python
def generator_version(n):
    for i in range(n):
        yield i
```

### Important difference

* `list_version(1_000_000)` stores one million values in memory
* `generator_version(1_000_000)` produces one value at a time

This is why generators are preferred for large or infinite sequences.

---

## 9. Generator expressions (generator version of list comprehensions)

### List comprehension

```python
numbers = [x * 2 for x in range(5)]
```

### Generator expression

```python
numbers = (x * 2 for x in range(5))
```

### Key difference

* Square brackets `[]` → list
* Parentheses `()` → generator

Use it like this:

```python
for n in numbers:
    print(n)
```

---

## 10. When you should use generators

### Use generators when:

* You only need values one at a time
* The dataset is large
* You want better memory efficiency
* You are streaming data or processing pipelines

### Avoid generators when:

* You need random access (`my_data[10]`)
* You need to reuse values multiple times without regenerating them

---

## 11. Common beginner mistakes (and how to avoid them)

### Mistake 1: Expecting a generator to behave like a list

```python
gen = count_up_to(3)
list(gen)
list(gen)  # This will be empty
```

**Reason:**

* Generators are exhausted after one pass

### Mistake 2: Forgetting that generators only run when iterated

```python
gen = count_up_to(3)
# Nothing happens yet
```

Execution starts only when:

* `next()` is called
* or a `for` loop begins

---

## 12. Summary (one-paragraph mental model)

A Python generator is a function that produces values one at a time using `yield`, pausing its execution between values and resuming exactly where it left off, making it memory-efficient and ideal for sequential or large-scale data processing.

---

### Next logical directions

If you want, the next steps could include:

* Visualizing generator execution step-by-step
* Using generators with files
* Chaining generators together
* Understanding `yield from`
