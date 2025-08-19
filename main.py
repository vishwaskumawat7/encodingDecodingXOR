import sys 

def xorAlgorithm(inp:str,key:str)->str:
    """
    This function is used to implement XOR Algorithm and returns the binary after implementing it.
    """
    # Converting the string to binary
    binInp =  format(ord(inp),'08b')
    binKey =  format(ord(key),'08b')

    # Implementing the XOR functionality - 1 if the binary of key and input is different otherwise its 0.
    xorOutBin = "".join('1' if bitInp != bitKey else '0' for bitInp, bitKey in zip(binInp,binKey))
    return xorOutBin

def encodeDecodeXOR(inp:str, key:str)-> str:
    """
    This function is used to encode/decode string using XOR algorithm. It accepts two arguments one is `inp` which is normal string or encoded string which you want to encode/decode and another is `key` which is used to encode/decode the input string.
    """
    inpLength = len(inp)
    keyLength = len(key)
    output = ""

    # Iterating over the input and encoding/decoding it using key
    for i in range(inpLength):

        # Repeating the key if the length of key is smaller than input string
        try:
            k = key[i % keyLength]
        except ZeroDivisionError:
            return "Division by zero not allowed"

        # Calling the xorAlgorithm which will return the encoded/decoded binary.
        xorOutBin = xorAlgorithm(inp[i],k)

        # Converting the binary to character
        xorOut = chr(int(xorOutBin,2))

        # Concatenting the string
        output +=xorOut
    return output

def main(text,key):

    # calling the encodeDecodeXOR function to encode or decode the input
    result = encodeDecodeXOR(text, key)
    return(result)
    
if __name__=="__main__":
    print("Welcome to the program. Here you can encode/decode XOR algorithm")

    # Checking if the required arguments passed in CLI
    if len(sys.argv) !=2:
        print("Invalid input!\nArguments have to be provided in this order: python3 file.py flag.`\nValid flags are:\n1. --encode: To encode the string using XOR algorithm\n2. --decode: To decode the encoded input using XOR algorithm")
        sys.exit(1)

    # Removing the hyphens from the left side of the flag
    flag = (sys.argv[1]).lstrip("-")

    # Flags allowed for this code
    valid_flags = ['encode','decode']

    # Checking the condition of flag not from allowed ones
    if flag not in valid_flags:
        print("Invalid flag detected\nValid flags are:\n1. --encode: To encode the string using XOR algorithm\n2. --decode: To decode the encoded input using XOR algorithm")
        sys.exit(1)

    # Getting input string
    text = input(f"Enter the text you want to {flag}: ")

    # Getting key as input
    key = input(f"Enter the key for {flag[:-1]}ing: ")

    print(main(text,key))