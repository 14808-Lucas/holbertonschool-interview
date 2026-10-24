#!/usr/bin/python3
"""Reads log lines from stdin and prints file size and status code stats."""
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and the count of each status code."""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code]:
            print("{}: {:d}".format(code, status_counts[code]))
    sys.stdout.flush()


def main():
    """Parse stdin line by line, printing stats every 10 lines and at exit."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in
                     ("200", "301", "400", "401", "403", "404", "405", "500")}
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                total_size += int(parts[-1])
                if parts[-2] in status_counts:
                    status_counts[parts[-2]] += 1
            except (IndexError, ValueError):
                pass
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
