#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Learning about date and time."""

import datetime

CURDATE = None


def get_current_date():
    """Assigns the current date

    Args:
        None

    Returns:
        The current date
    """
    return datetime.date.today()

# prints the current date if python is running from the command line ($)

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
