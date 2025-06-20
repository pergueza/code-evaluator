# Code Evaluator

This is a simple Python tool to evaluate and compare two solution scripts that address the same problem.

It compares:
- Execution time
- Code length (number of lines)
- Style warnings (basic line length check)

### Usage

1. Place two files named `solution1.py` and `solution2.py` in the `examples/` directory.  
   Each file must define a function named `solve()` with no arguments.

2. Run the evaluator:
```bash
python main.py


## Outup Example

Evaluation Report:
------------------
Solution 1:
- Time: 0.000016s
- Lines of Code: 6
- Style Warnings (long lines): 0

Solution 2:
- Time: 0.000007s
- Lines of Code: 2
- Style Warnings (long lines): 0

Recommendation:
Solution 2 is cleaner and more concise.


### Note
This project was developed as a demonstrative exercise aligned with the responsibilities of the Coding Expert - LATAM role at Outlier.ai.
