def main(pro_input):
    length = len(pro_input)
    my_stack = []
    first_char = pro_input[0]
    current_char = first_char

    second_char = None
    my_stack.append(0)  # for first char
    for i in range(1, length):
        next_char = pro_input[i]
        if first_char == 'a':
            if second_char == 'b':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            elif second_char == 'c':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            else:
                my_stack.append(0)
                if current_char != next_char:
                    current_char = next_char
                    second_char = current_char


        elif first_char == 'b':
            if second_char == 'a':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            elif second_char == 'c':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            else:
                my_stack.append(0)
                if current_char != next_char:
                    current_char = next_char
                    second_char = current_char
        elif first_char == 'c':
            if second_char == 'b':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            elif second_char == 'a':
                if current_char == next_char:
                    my_stack.append(0)
                else:
                    my_stack.pop()
            else:
                my_stack.append(0)
                if current_char != next_char:
                    current_char = next_char
                    second_char = current_char
        else:
            my_stack.append("error")
    return my_stack


if __name__ == "__main__":
    try:
        my_stack = main(input("please input string : \n"))
        if len(my_stack) == 0:
            print("ALLOWED")
        else:
            print("REJECTED")
    except:
        print("REJECTED")
