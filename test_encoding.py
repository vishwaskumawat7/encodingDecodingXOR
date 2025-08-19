import time
from main import main
import sys

# Checking if the required arguments passed in CLI
if len(sys.argv) !=2:
    print("Invalid input!\nArguments have to be provided in this order: python3 file.py flag.\nExample Input: python3 test_encoding.py --encode")
    sys.exit(1)

# Removing the hyphens from the left side of the flag
flag = (sys.argv[1]).lstrip("-")

# Checking if the flag is allowed or not
if flag != 'encode':
    print("Invalid flag detected\nExample Input: python3 test_encoding.py --encode")
    sys.exit(1)

for i in range(1, 16):

    # opening the file to read the content
    with open(f"inp_enc_to_dec/input{i}.txt") as f:
        text,key = f.read().split("\n", 1)

    print("---------------------")
    print(f"Running Test Case {i}")
    print("---------------------\n")

    # storting the time at the starting of the function
    start_time = time.time()

    # calling the main function to implement encoding using XOR algorithm
    result = main(text,key)

    print("Original String:",text)
    print("Encoded String:", result)

    # storting the time at the ending of the function
    end_time = time.time()
    
    print("")
    print("************************************")

    # calculating the total execution time
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("************************************\n")