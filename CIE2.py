import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    distance = float(sys.argv[1])
    time = float(sys.argv[2])
else:
    print("Usage: python CIE2.py <distance> <time>")
    distance = 1000
    time = 160
    sys.exit(1)

speed = distance / time

print(f"The calculated speed = {speed:.2f}")
