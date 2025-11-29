import sys

if len(sys.argv == 4):
    print("Usage: python CIE2.py <distance> <time>")
    script_name = (sys.argv[0])
    distance = float(sys.argv[1])
    time = float(sys.argv[2])
    speed = float(sys.argv[3])

else: 
    script_name = (sys.argv[0])
    distance = 1000
    time = 260

    speed = distance / time

    print(f"The calculated speed = {speed:.2f}")

























    