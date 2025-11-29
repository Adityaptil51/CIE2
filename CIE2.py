import sys

if len(sys.argv) == 3:
    try:
        print("Usage: python CIE2.py <distance> <time>")
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    except ValueError:
        print("Invalid parameters! Using default values.")
        distance = 1000
        time = 260
else:
    distance = 1000
    time = 260

speed = distance / time
print(f"The calculated speed = {speed:.2f}")
