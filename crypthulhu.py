import sys


def main():
    print('''
   ___                 _   _           _ _           
  / __\ __ _   _ _ __ | |_| |__  _   _| | |__  _   _ 
 / / | '__| | | | '_ \| __| '_ \| | | | | '_ \| | | |
/ /__| |  | |_| | |_) | |_| | | | |_| | | | | | |_| |
\____/_|   \__, | .__/ \__|_| |_|\__,_|_|_| |_|\__,_|
           |___/|_|                                  
            by tavroux | version 1.0
    ''')
    print('Crypthulhu rises from the deep...')
    # Validate correct number of inputs (3)
    if len(sys.argv) == 1:
        print('''
Crypthulhu takes two files, Xor's them, and creates a third,
unintelligible file. File C is essentially an encrypted version
of the smaller file A or B, with the longer file serving as
the key. Crypthulhu can be ran a second time with File C and
the longer file A or B to recreate the shorter file.''')
        sys.exit()
    elif len(sys.argv) != 4:
        print('Was expecting 3 inputs but got', len(sys.argv) - 1, 'instead.')
        sys.exit()

    # Take input from the command line
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    file_c = sys.argv[3]

    try:
        # Read in the two input files
        print('Crypthulhu reaches his slimy tentacles into', file_a, 'and', file_b, '.')
        with open(file_a, 'rb') as a, open(file_b, 'rb') as b:
            file_a_bytes = bytearray(a.read())
            file_b_bytes = bytearray(b.read())
    except Exception as e:
        # If the script has any issues handling the files (such as non-existent files), print this here
        print('The given files have escaped the grasp of Crypthulhu... for now...')
        print(e)
    else:
        # Xor the two input files
        file_c_bytes = bytearray()
        for b1, b2 in zip(file_a_bytes, file_b_bytes):
            file_c_bytes.append(b1 ^ b2)

        # Write the Xor'd bytearray to file
        print('Crypthulhu creates the Xor\'d content in', file_c)
        c = open(file_c, 'wb')
        c.write(file_c_bytes)
        c.close()


if __name__ == '__main__':
    main()
