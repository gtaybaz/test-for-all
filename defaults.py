"""Default configuration applied when a brand-new agent is created."""

from iterations import save_agent_config

DEFAULT_MAX_ITERATIONS = 150


def create_default_config(agent_id):
    """Save the default configuration for a newly created agent."""
    return save_agent_config(agent_id, DEFAULT_MAX_ITERATIONS)
