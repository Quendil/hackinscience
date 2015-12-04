import sys
if len(sys.argv) == 4:
    if sys.argv[2] == '+':
        print(int(sys.argv[1]) + int(sys.argv[3]))
    if sys.argv[2] == '-':
        print(int(sys.argv[1]) - int(sys.argv[3]))
    if sys.argv[2] == '*':
        print(int(sys.argv[1]) * int(sys.argv[3]))
    if sys.argv[2] == '/':
        if sys.argv[3] == '0':
            print('input error')
        else:
            print(int(sys.argv[1]) / int(sys.argv[3]))
    if sys.argv[2] == '%':
        print(int(sys.argv[1]) % int(sys.argv[3]))
    if sys.argv[2] == '^':
        print(int(sys.argv[1]) ** int(sys.argv[3]))
    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '/'\
       and sys.argv[2] != '*' and sys.argv[2] != '%' and sys.argv[2] != '^':
        print('input error')
else:
    print('usage: ./solution.py a_number (an_operator +-*/%^) a_number')
