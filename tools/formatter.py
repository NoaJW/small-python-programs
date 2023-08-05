# TODO: Validate that user did not copy other lines that is not part of the code

import sys

def main(): 
    while True: 
        print("Input file path (or 'Q' to quit):")
        file_path = input("> ")
        if file_path.upper() == 'Q':
            sys.exit()

        try: 
            with open(file=file_path, mode='r+', encoding="utf8") as file:
                lines = file.readlines()

                for index, line in enumerate(lines):
                    line = line.strip()    
                    line += "\n"                    # Add back newline as it is removed in strip()      
                    lines[index] = line

                    for char in line:
                        if char.isdecimal():        # Remove the number
                            line = line[1:]
                            lines[index] = line
                            continue
                        else:                       # Remove ". " after the number 
                            line = line[2:]
                            lines[index] = line
                            break

                file.seek(0)
                file.truncate()
                file.writelines(lines)
                print("File has been formatted!")
                break
        except FileNotFoundError:
            print("File not found.")
        except UnicodeDecodeError: 
            print("File is not a text file.")


def is_binary_string(bytes): 
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    return bool(bytes.translate(None, textchars))


if __name__ == '__main__':
    main()