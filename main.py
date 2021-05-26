from dataclasses import dataclass


def readData():
    fin = open("data.in", "r")
    initialState = fin.readline().split()[1].strip()
    finalState = fin.readline().split()[1].strip()
    line = fin.readline().split()
    if len(line) == 1:
        badState = ""
    else:
        badState = line[1].strip()

    emptySymbol = fin.readline().split()[1].strip()
    print(initialState)
    print(finalState)
    print(badState)
    print(emptySymbol)

    lines = []

    for line in fin.readlines():
        l = [x.strip() for x in line.split(",")]
        if l != [""]:
            lines.append(l)

    transitions = dict()

    for i in range(0, len(lines), 2):
        transitions[lines[i][0], lines[i][1]] = lines[i + 1]

    # print(transitions)
    fin.close()

    return (initialState, finalState, badState, emptySymbol, transitions)


def openMenu():
    TM = TuringMachine(*readData())

    while 1:

        print("Type 1 to query")
        print("Type 0 to exit")

        opcode = input().strip()

        if opcode == "0":
            break
        elif opcode == "1":
            print("Insert the word you wish to check")
            word = input().strip()
            TM.check(word)
        else:
            print("Invalid input")


# print(lines)

@dataclass
class TuringMachine:
    initialState: str
    finalState: str
    badState: str
    emptySymbol: str
    tape: dict
    transitions: dict

    def __init__(self, initialState, finalState, badState, emptySymbol, transitions):
        self.initialState = initialState
        self.finalState = finalState
        self.badState = badState
        self.emptySymbol = emptySymbol
        self.transitions = transitions
        self.tape = dict()

    def check(self, word):

        self.tape = dict()

        for i in range(len(word)):  # We place the word on our tape
            self.tape[i] = word[i]

        currentIndex = 0  # Where we start
        currentState = self.initialState

        flag = 1

        while currentState != self.badState and currentState != self.finalState:
            currentCharacter = self.tape.get(currentIndex, self.emptySymbol)
            if (currentState, currentCharacter) not in self.transitions.keys():
                flag = 0
                break

            transition = self.transitions[(currentState, currentCharacter)]

            currentState = transition[0]
            self.tape[currentIndex] = transition[1]
            if transition[2] == '>':
                currentIndex += 1
            elif transition[2] == '<':
                currentIndex -= 1
            else:
                pass

        if flag == 0 or currentState == self.badState:
            print("The word {} was not accepted by our Turing Machine".format(word))
        else:
            print("The word {} was accepted by our Turing Machine".format(word))


# def check(self,word):


# print(transitions)


openMenu()
