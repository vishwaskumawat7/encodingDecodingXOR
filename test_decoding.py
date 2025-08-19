import time
from main import main
import sys

# Checking if the required arguments passed in CLI
if len(sys.argv) !=2:
    print("Invalid input!\nArguments have to be provided in this order: python3 file.py flag.\nExample Input: python3 test_decoding.py --decode")
    sys.exit(1)

# Removing the hyphens from the left side of the flag
flag = (sys.argv[1]).lstrip("-")

# Checking if the flag is allowed or not
if flag != 'decode':
    print("Invalid flag detected\nExample Input: python3 test_decoding.py --decode")
    sys.exit(1)

for i in range(1, 16):

    # opening the file to read the content
    with open(f"inp_dec_to_enc/input{i}.txt") as f:
        text,key = f.read().split("\n", 1)

    print("---------------------")
    print(f"Running Test Case {i}")
    print("---------------------\n")

    # storting the time at the starting of the function
    start_time = time.time()

    # calling the main function to implement decoding using XOR algorithm
    result = main(text,key)

    print("Encoded String:",text)
    print("Decoded String:", result)

    # storting the time at the ending of the function
    end_time = time.time()
    
    print("")
    print("************************************")

    # calculating the total execution time
    print(f"Execution time: {end_time - start_time:.4f} seconds")
    print("************************************\n")