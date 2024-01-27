import time


class View:

    BOARD_STRING = "|------------|" \
                   "\n|  1  |   2  |" \
                   "\n|------------|" \
                   "\n|  3  |   4  |" \
                   "\n-------------|"

    def __init__(self, argument=1):
        pass

    def display_initial_message(self, username):
        self.display_board()
        print("\nThere's a mole out there...")
        print("It exists here, there and everywhere ... at once")
        print("We bestow upon you the Quantum Hammer!!!")
        print("Use it and end the terror of the Quantum-mole!")

    def accept_move(self):
        x = input(
            "What are you going to do? Enter c for classical smash and q for quantum smash, and which gate (ex: c1 or q3): ")
        return x

    def final_message(self, username, win):
        if win:
            print("YOU WIN!")
        else:
            print("YOU MISSED, YOU LOSE!")
            print(
                "The quantum mole lives on ... it is here, there and everywhere ... at once")

    def display_quantum_message(self, hint, hole):
        print("New Information!!!")
        print("Probability amplitude of mole being in hole " + hole + " is ", hint)

    def display_board(self):
        print(View.BOARD_STRING)

    def accept_quantum_gate(self):
        result = []
        gate = input(
            "What quantum gate do you wish to add to the circuit [R/CX/?]: ")
        result.append(gate)

        if gate == 'r' or gate == 'R':
            angle = input("Enter phase [?]: ")
            result.append(angle)

        elif gate == 'cx' or gate == 'CX':
            control_qubit = input("Enter control qubit [1-4]: ")
            result.append(control_qubit)

        else:
            result.append("b")
        target_qubit = input("Enter target qubit [1-4]: ")
        result.append(target_qubit)

        return result
