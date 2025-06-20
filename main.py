import time
import importlib.util
from pathlib import Path
from rich import print


def load_function_from_file(file_path: str):
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "solve")


def measure_execution_time(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


def get_file_length(file_path):
    with open(file_path, "r") as f:
        return len(f.readlines())


def analyze_code_style(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
            long_lines = [line for line in content.splitlines() if len(line) > 79]
            return len(long_lines)
    except Exception:
        return -1


def evaluate():
    path1 = "examples/solution1.py"
    path2 = "examples/solution2.py"

    func1 = load_function_from_file(path1)
    func2 = load_function_from_file(path2)

    time1 = measure_execution_time(func1)
    time2 = measure_execution_time(func2)

    len1 = get_file_length(path1)
    len2 = get_file_length(path2)

    style1 = analyze_code_style(path1)
    style2 = analyze_code_style(path2)

    report = f"""
Evaluation Report:
------------------
Solution 1:
- Time: {time1:.6f}s
- Lines of Code: {len1}
- Style Warnings (long lines): {style1}

Solution 2:
- Time: {time2:.6f}s
- Lines of Code: {len2}
- Style Warnings (long lines): {style2}

[bold]Recommendation:[/bold]
"""
    if style1 < style2:
        report += "Solution 1 is cleaner and more concise."
    elif style1 > style2:
        report += "Solution 2 is more readable and style-compliant."
    else:
        report += "Both solutions are equally clear in style."

    with open("evaluations/analysis_01.txt", "w") as f:
        f.write(report)

    print(report)


if __name__ == "__main__":
    Path("evaluations").mkdir(exist_ok=True)
    evaluate()
