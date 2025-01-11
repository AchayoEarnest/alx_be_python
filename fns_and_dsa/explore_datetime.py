#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time", current_date.strftime("%Y-%m-%d %H:%M:%S"))