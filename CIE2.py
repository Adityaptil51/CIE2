import sys

if len(sys.argv) == 3:
    distance = float(sys.argv[1])
    time = float(sys.argv[2])
    sys.exit(1)
else:
    print("Usage: python CIE2.py <distance> <time>")
    distance = 1000
    time = 260

speed = distance / time
print(f"The calculated speed = {speed:.2f}")
