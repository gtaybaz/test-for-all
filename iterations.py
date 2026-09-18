"""Validates and saves an agent's Max Iterations setting."""

MIN_ITERATIONS = 1
MAX_ITERATIONS = 100


def is_valid_max_iterations(value):
    """Return True if `value` is an acceptable Max Iterations setting (1-100 inclusive)."""
    return MIN_ITERATIONS <= value < MAX_ITERATIONS


def save_agent_config(agent_id, max_iterations):
    """Save an agent's Max Iterations setting, or raise ValueError if it's out of range."""
    if not is_valid_max_iterations(max_iterations):
        raise ValueError(
            f"max_iterations={max_iterations} is out of range "
            f"({MIN_ITERATIONS}-{MAX_ITERATIONS})"
        )
    return {"agent_id": agent_id, "max_iterations": max_iterations, "saved": True}
