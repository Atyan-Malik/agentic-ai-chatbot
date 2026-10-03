import math
from datetime import datetime


def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression.
    Example: calculator("25 * 4")
    """
    try:
        allowed = {
            "abs": abs,
            "round": round,
            "pow": pow,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
        }

        result = eval(
            expression,
            {"__builtins__": {}},
            allowed
        )

        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


def get_current_time() -> str:
    """
    Return the current local date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_date() -> str:
    """
    Return today's date.
    """
    return datetime.now().strftime("%Y-%m-%d")


def get_available_tools():
    """
    Return the tools available to the agent.
    """
    return {
        "calculator": calculator,
        "get_current_time": get_current_time,
        "get_current_date": get_current_date,
    }
