import sys
from pswGen.password_gen import gen_psw

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    print(gen_psw(length))