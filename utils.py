"""
Utility functions for the expense tracker
"""

import os


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)


def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:,.2f}"
