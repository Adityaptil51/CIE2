import sys

if len(sys.argv) == 3:
    distance = float(sys.argv[1])
    time = float(sys.argv[2])

elif len(sys.argv) == 1:
    distance = 1000
    time = 260

else:
    print("Usage: python CIE2.py <distance> <time>")
    sys.exit(1)

speed = distance / time
print(f"The calculated speed = {speed:.2f}")
