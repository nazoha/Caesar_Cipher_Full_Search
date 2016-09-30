def siza_decode(decode_string):
    for i in range(26):
        tango = ""
        for j in range(len(decode_string)):
            ascii_code = ord(decode_string[j]) + i
            if ascii_code > 90:
                ascii_code = ascii_code - 26
            tango = tango + chr(ascii_code)
        print("key={0}: {1}\n".format(i, tango))

def main():
    input_decode = input()
    siza_decode(input_decode)

if __name__ == '__main__':
    main()