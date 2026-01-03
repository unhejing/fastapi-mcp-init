from datetime import datetime

def get_current_time() -> str:
    """
    Get the current time in a human-readable format.

    Returns:
        str: Current time formatted as 'YYYY-MM-DD HH:MM:SS'
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
