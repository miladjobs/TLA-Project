from turing import TuringMachine
import time


if __name__ == '__main__':
    input_string = input("please input number : \n")
    input_machine_string = ''
    for _ in range(int(input_string)):
        input_machine_string += '1'
    flag_first_iteration = True
    while input_machine_string != '1' or flag_first_iteration:
        flag_first_iteration = False
        tape_for_check_even = input_machine_string + '_'
        initial_state_for_check_even = 'q0'
        final_states_for_check_even = {'q2'}

        transition_function_for_check_even = {
            ('q0', '1'): ('q1', '_', 'R'),
            ('q1', '1'): ('q0', '_', 'R'),
            ('q1', '_'): ('q3', '_', 'R'),
            ('q0', '_'): ('q2', '_', 'R'),
        }
        # ---------------------------------

        check_even_turing_machine = TuringMachine(
            tape_for_check_even,
            initial_state_for_check_even,
            final_states_for_check_even,
            transition_function_for_check_even
        )
        even_flag = True
        while not check_even_turing_machine.final():
            if time.time() - check_even_turing_machine.time > 0.1:
                even_flag = False
                break
            check_even_turing_machine.step()
        if even_flag:
            tape_for_divide = input_machine_string + '_'
            initial_state_for_divide = 'q0'
            final_states_for_divide = {'q4'}

            transition_function_for_divide = {
                ('q0', '1'): ('q1', 'y', 'R'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '_'): ('q2', '_', 'L'),
                ('q2', '1'): ('q3', '_', 'L'),
                ('q3', '1'): ('q3', '1', 'L'),
                ('q3', 'y'): ('q0', 'y', 'R'),
                ('q0', '_'): ('q4', '_', 'R'),
            }

            divide_turing_machine = TuringMachine(
                tape_for_divide,
                initial_state_for_divide,
                final_states_for_divide,
                transition_function_for_divide
            )

            while not divide_turing_machine.final():
                divide_turing_machine.step()
            input_machine_string = divide_turing_machine.get_tape()
            print(len(input_machine_string), end=' ')


        else:
            tape_for_multiply = input_machine_string + 's111'
            initial_state_multiply = 'q0'
            final_states_multiply = {'q12'}

            transition_function_multiply = {
                ('q0', '1'): ('q0', '1', 'R'),
                ('q0', 's'): ('q1', 's', 'R'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '_'): ('q2', 's', 'L'),
                ('q2', '1'): ('q2', '1', 'L'),
                ('q2', 's'): ('q3', 's', 'R'),
                ('q3', 'x'): ('q3', 'x', 'R'),
                ('q3', 's'): ('q12', '1', 'R'),
                ('q3', '1'): ('q4', 'x', 'L'),
                ('q4', 'x'): ('q4', 'x', 'L'),
                ('q4', 's'): ('q5', 's', 'L'),
                ('q5', 'y'): ('q5', 'y', 'L'),
                ('q5', '_'): ('q11', '_', 'R'),
                ('q11', 'y'): ('q11', '1', 'R'),
                ('q11', 's'): ('q3', 's', 'R'),
                ('q5', '1'): ('q6', 'y', 'R'),
                ('q6', 'y'): ('q6', 'y', 'R'),
                ('q6', 's'): ('q7', 's', 'R'),
                ('q7', '1'): ('q7', '1', 'R'),
                ('q7', 'x'): ('q7', 'x', 'R'),
                ('q7', 's'): ('q8', 's', 'R'),
                ('q8', '1'): ('q8', '1', 'R'),
                ('q8', '_'): ('q9', '1', 'L'),
                ('q9', '1'): ('q9', '1', 'L'),
                ('q9', 's'): ('q10', 's', 'L'),
                ('q10', '1'): ('q10', '1', 'L'),
                ('q10', 'x'): ('q10', 'x', 'L'),
                ('q10', 's'): ('q5', 's', 'L'),
            }

            multiple_turing_machine = TuringMachine(
                tape_for_multiply,
                initial_state_multiply,
                final_states_multiply,
                transition_function_multiply
            )

            while not multiple_turing_machine.final():
                multiple_turing_machine.step()
            input_machine_string = multiple_turing_machine.get_tape()
            print(len(input_machine_string), end=' ')


