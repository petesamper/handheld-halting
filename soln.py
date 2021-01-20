# Instructions
ACC = "acc"
JMP = "jmp"
NOP = "nop"


acc = 0


def handle_acc(acc_instruction):
    acc_amount = 0
    for char in acc_instruction:
        if char == "+":
            #acc_amount += int(acc_instruction[char:-1])
            #acc += acc_amount


def handle_jmp(jmp_instr):
    distance = 0
    for char in jmp_instr:
        if char == "+" or "-":
            amount_idx = jmp_instr.index(char)
            distance += int(jmp_instr[amount_idx:-1])
            print(distance)

def soln(input_file):
    with open(input_file, "r") as reader:
        instruction_list = reader.readlines()
        i = 0
        while i < len(instruction_list):
            if ACC in instruction_list[i]:
                # handle_acc(instruction_list[i])
                print("acc: ", acc)
            if JMP in instruction_list[i]:
                handle_jmp(instruction_list[i])
            if NOP in instruction_list[i]:
                continue


soln("input.txt")
