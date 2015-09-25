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

    Examples:
        >>> import task_01
        >>> task_01.CURDATE
        >>> task_01.get_current_date()
        datetime.date(2015, 9, 25)

        $ python -i task_01.py
        2015-09-25
        >>> CURDATE
        datetime.date(2015, 9, 25)
    """
    return datetime.date.today()

# prints the current date if python is running from the command line ($)

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
