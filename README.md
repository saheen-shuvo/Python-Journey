# Python Journey

A personal, practical journey through Python fundamentals. This repository is a growing collection of notes, runnable examples, small problem-solving exercises, and experiments created while learning Python.

It is designed to work as:

- **Personal notes** for reviewing Python concepts.
- **A beginner-friendly reference** for seeing concepts explained through code.
- **A practice archive** for short programming problems and data-structure exercises.
- **A starting point for future projects** as the learning path expands.

> This repository is intentionally learning-focused. Some files are simple demonstrations, while others are unfinished experiments or competitive-programming-style exercises.

## Learning roadmap

The current material progresses through these core topics:

1. Python syntax, variables, data types, input, and type conversion
2. Operators, strings, conditions, and loops
3. Lists, tuples, dictionaries, and sets
4. Functions, arguments, return values, lambdas, iterators, and generators
5. File reading, writing, file pointers, and text processing
6. Exception handling
7. Object-oriented programming, inheritance, and polymorphism
8. Small exercises involving numbers, strings, collections, stacks, and queues

## Repository structure

```text
Python-Journey/
├── basics/
│   ├── variables.py                         # Variables and naming rules
│   ├── dataType.py                          # Built-in Python data types
│   ├── taking_input.py                      # User input and type conversion
│   ├── operators.ipynb                      # Arithmetic, comparison, logical operators, precedence
│   ├── conditional_statement.py             # if / elif / else and nested conditions
│   ├── for_loop.py                          # for loops and range()
│   ├── while_loop.py                        # while loops
│   ├── continue_break.py                    # continue and break
│   ├── string_slice.py                      # String indexing and slicing
│   ├── string_methods.py                    # Common string operations
│   ├── C_Even_Odd_Positive_and_Negative.py  # Count number categories
│   ├── F_Digits_Summation.py                # Sum the last digits of two numbers
│   ├── Q_Digits.py                          # Print digits in reverse order
│   └── test.py                              # Minimal Hello World example
├── list/
│   ├── list.py                              # List creation, indexing, mutation, and methods
│   ├── list_comprehension.py                # List comprehensions
│   ├── stack_as_list.py                     # Stack operations using a list
│   ├── queue_as_list.py                     # Queue operations using a list
│   ├── E_Lowest_Number.py                   # Find a minimum value and its position
│   ├── K_Max_and_Min.py                     # Find minimum and maximum values
│   └── M_Replace_MinMax.py                  # Swap minimum and maximum values
├── tuple/
│   └── tuple.py                              # Immutability, slicing, conversion, and unpacking
├── set/
│   └── set.py                                # Unique values and set operations
├── dictionary/
│   ├── dictionary.py                         # Key-value pairs and dictionary basics
│   ├── dictionary_methods.py                 # Dictionary methods and iteration
│   ├── dictionary_comprehension.py           # Dictionary comprehensions
│   ├── ps_1.py                               # Remove duplicate values with a set
│   └── string-frq-ps.py                      # Frequency counting with a dictionary
├── function/
│   ├── function_basics.py                   # Defining and calling functions
│   ├── arguments.py                          # Positional, keyword, default, *args, and **kwargs
│   ├── func_return_type.py                  # Return values and tuple unpacking
│   ├── lambda_func.py                        # lambda, map, filter, sorted, and reduce
│   └── iterator_&_generator.py               # iter(), next(), yield, and chunked data loading
├── file handling/
│   ├── read_file.py                          # Reading files with read(), readline(), and readlines()
│   ├── write_file.py                         # Writing and appending to files
│   ├── file_pointer.py                       # tell(), seek(), and file positions
│   └── count_words_file.py                   # File text statistics and functional tools
├── exception handling/
│   └── exception_handling.py                 # Exception handling examples
├── oop/
│   ├── oop.py                                # Classes, objects, inheritance, and overriding
│   ├── oop_inheritance.py                    # Single and multiple inheritance
│   └── oop_polymorphism.py                   # Method overriding and flexible arguments
└── .cph/                                     # Competitive programming helper metadata
```

## What you can learn here

### Python basics

The `basics/` directory introduces the building blocks of Python: variable assignment, built-in types, input, conversion between types, operators, conditions, loops, and string manipulation. The `operators.ipynb` notebook provides an interactive version of arithmetic, comparison, logical, and precedence examples.

### Built-in collection types

The collection directories compare the behavior and use cases of Python's most common containers:

- **Lists:** ordered and mutable collections, slicing, sorting, nested lists, comprehensions, stacks, and queues.
- **Tuples:** ordered and immutable collections, tuple unpacking, conversions, and mutable values nested inside tuples.
- **Sets:** unique values, membership checks, and union, intersection, difference, and symmetric-difference operations.
- **Dictionaries:** key-value storage, updates, removal, iteration, comprehensions, and frequency counting.

### Functions and functional patterns

The `function/` directory demonstrates function definitions, parameters, default values, positional and keyword arguments, variable-length arguments, return values, lambda functions, and docstrings. It also introduces iterators and generators, including a generator that loads a list in chunks.

### Files and exceptions

The file examples cover common file modes such as `r`, `w`, `a`, and `r+`, along with `read()`, `readline()`, `readlines()`, `tell()`, and `seek()`. The exception-handling directory is reserved for practicing safer error-aware Python programs.

### Object-oriented programming

The `oop/` directory starts with classes and objects and then develops the ideas of inheritance and polymorphism. Examples include `Person` and `Student`, `Vehicle` and `Car`, multiple inheritance with `Hybrid`, and method overriding with `Dog` and `Cat`.

## Getting started

### Requirements

- Python 3.10 or newer is recommended.
- Jupyter Notebook or JupyterLab is optional for `basics/operators.ipynb`.
- `function/func_return_type.py` uses `sklearn.model_selection.train_test_split`, so install scikit-learn if you want to run that example.

No project-wide package manager or dependency lockfile is currently required for the basic examples.

### Clone the repository

```bash
git clone https://github.com/saheen-shuvo/Python-Journey.git
cd Python-Journey
```

### Run a Python example

Run a file from the repository root:

```bash
python basics/variables.py
python list/list_comprehension.py
python function/lambda_func.py
python oop/oop.py
```

On systems where `python` points to Python 2, use `python3` instead:

```bash
python3 basics/test.py
```

### Open the notebook

```bash
jupyter notebook basics/operators.ipynb
```

### Run input-based exercises

Some exercises expect input from standard input. For example:

```bash
python basics/F_Digits_Summation.py
```

Then enter two numbers separated by a space. Other input-based examples include `basics/Q_Digits.py`, `basics/C_Even_Odd_Positive_and_Negative.py`, and the exercises in `list/`.

### File-handling examples

Several scripts use a file named `example.txt` in the current working directory. Create one before running those examples:

```bash
echo "Python is a readable programming language." > "example.txt"
python "file handling/read_file.py"
python "file handling/file_pointer.py"
python "file handling/count_words_file.py"
```

## Suggested study order

If you are following this repository as a course or revision guide, use this order:

1. `basics/variables.py`, `dataType.py`, and `taking_input.py`
2. `basics/operators.ipynb`, `conditional_statement.py`, and the loop examples
3. `basics/string_slice.py` and `string_methods.py`
4. `list/list.py`, `list/list_comprehension.py`, and the stack/queue examples
5. `tuple/tuple.py`, `set/set.py`, and the `dictionary/` examples
6. `function/function_basics.py`, `arguments.py`, and `func_return_type.py`
7. `function/lambda_func.py` and `iterator_&_generator.py`
8. The `file handling/` and `exception handling/` directories
9. `oop/oop.py`, `oop/oop_inheritance.py`, and `oop/oop_polymorphism.py`
10. Revisit the problem-solving scripts and rewrite them with cleaner input validation and reusable functions

## Notes about the examples

- Most files are standalone demonstrations and print their results directly.
- Input-based exercises may assume a particular input format; read the file before running it.
- Some examples intentionally show a concept in a simple way rather than as production-ready code.
- A few scripts are works in progress and may need small corrections while the learning journey continues.
- The `.cph/` directory contains helper metadata related to competitive-programming files and is not part of the learning roadmap.

## Learning goals

This repository will continue to grow toward:

- Cleaner and more idiomatic Python
- Better input validation and exception handling
- Reusable functions instead of repeated top-level code
- Testing examples with `pytest`
- More algorithm and data-structure exercises
- Modules, packages, virtual environments, and dependency management
- Small practical projects that combine the concepts in this repository

## Contributing and using these notes

This is primarily a personal learning journal, but others are welcome to read, fork, experiment with, and improve it. If you find an error or have a clearer explanation, open an issue or submit a pull request with a focused change.

When adding new notes, prefer:

- One focused concept per file
- Descriptive filenames
- Short comments explaining the idea
- A small runnable example
- A problem-solving example when appropriate
- Updated documentation when a new topic or directory is added

## License

No license has been selected for this repository yet. If you want others to legally reuse, modify, or redistribute the notes, add an appropriate open-source license.

---

Built while learning Python, one example at a time.
