import sys
for i in enumerate(sys.argv, start=0):
    print(i, sys.argv[int(i)])
