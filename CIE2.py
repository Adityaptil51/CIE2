import sys

if len(sys.argv) == 3:
        print("Usage: python CIE2.py <distance> <time>")
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
        sys.exit(2)
else:
    distance = 1000
    time = 260

speed = distance / time
print(f"The calculated speed = {speed:.2f}")
