"""Agent naming: sanitization and uniqueness checks."""

import re

_UNSAFE = re.compile(r"\.\./")


def sanitize_agent_name(name):
    """Strip path-traversal sequences from a user-supplied agent name."""
    return _UNSAFE.sub("", name)


def is_agent_name_available(name, existing_names):
    """Return True if `name` isn't already taken.

    Agent names are case-sensitive by design - "Bot" and "bot" are treated as
    distinct agents, matching how the rest of the platform treats names.
    """
    return name not in existing_names
