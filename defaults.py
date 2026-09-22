"""Default configuration applied when a brand-new agent is created."""

from iterations import save_agent_config, MAX_ITERATIONS

DEFAULT_MAX_ITERATIONS = MAX_ITERATIONS


def create_default_config(agent_id):
    """Save the default configuration for a newly created agent."""
    return save_agent_config(agent_id, DEFAULT_MAX_ITERATIONS)
