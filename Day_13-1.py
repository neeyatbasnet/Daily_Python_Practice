total_sum = 0
current_num = ""

try:
    with open("textfile.txt", "r") as f:
        for line in f:
            for char in line:
                if char.isdigit():
                    # Build the number digit by digit
                    current_num += char
                else:
                    # If we hit a non-digit, check if we have a number to add
                    if current_num:
                        total_sum += int(current_num)
                        current_num = "" # Reset for the next number
        
        # Final check in case a line ends with a number
        if current_num:
            total_sum += int(current_num)
            current_num = ""

    print(total_sum)

except FileNotFoundError:
    print("File not Found")
