"""Demonstrates asking the user for input."""

from curses import ACS_GEQUAL


user_name: str = input("What is your name? ")

print("Hello, " + user_name + ", good morning!")
print("You are awesome" + user_name )
