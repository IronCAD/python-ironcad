import sys
import time

def print_green_dot():
    # ANSI escape code for green
    print("  \033[92m.\033[0m", end="", flush=True)

def print_fail(msg):
    # ANSI escape code for red
    print(f"\n    \033[91mFAIL:\033[0m {msg}")

def print_success(msg):
    # ANSI escape code for green
    print(f"\n    \033[92mPASS:\033[0m {msg}")
