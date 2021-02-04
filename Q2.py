from turing import TuringMachine
import time


if __name__ == '__main__':
    input_string = input("please input string : \n")
    tape = input_string + '_'
    initial_state = 'q1'
    final_states = {'q6', 'q7'}

    transition_function = {
        ('q1', 'a'): ('q2', '_', 'R'),
        ('q2', 'x'): ('q2', 'x', 'R'),
        ('q2', 'a'): ('q3', 'x', 'R'),
        ('q3', 'x'): ('q3', 'x', 'R'),
        ('q3', 'a'): ('q4', 'a', 'R'),
        ('q4', 'x'): ('q4', 'x', 'R'),
        ('q4', 'a'): ('q3', 'x', 'R'),
        ('q3', '_'): ('q5', '_', 'L'),
        ('q5', 'a'): ('q5', 'a', 'L'),
        ('q5', 'x'): ('q5', 'x', 'L'),
        ('q5', '_'): ('q2', '_', 'R'),
        ('q2', '_'): ('q6', '_', 'R'),
        ('q1', '_'): ('q7', '_', 'R'),
        ('q1', 'x'): ('q7', 'x', 'R'),
        ('q4', '_'): ('q7', '_', 'R'),
    }
    # ---------------------------------

    turing_machine = TuringMachine(
        tape,
        initial_state,
        final_states,
        transition_function
    )


    while not turing_machine.final() and time.time() - turing_machine.time < 0.1:
        turing_machine.step()

    accepted_tape = '_'
    for i in range(1, len(input_string)):
        accepted_tape += 'x'

    if turing_machine.get_tape() == accepted_tape:
        print("ALLOWED")
    else:
        print("REJECTED")