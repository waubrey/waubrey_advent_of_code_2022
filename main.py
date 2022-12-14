def elf_most_calories(input):
    all_elf_calories = []
    list_calories_per_elf = []
    total_calories_per_elf = []
    with open(input) as f:
        lines = f.readlines()
        #print(len(lines))
        for line in lines:
            line = line.strip().rstrip()
            if line == '':
                list_calories_per_elf.append(all_elf_calories)
                all_elf_calories = []
            else:
                all_elf_calories.append(int(line))
        list_calories_per_elf.append(all_elf_calories)
        for i in list_calories_per_elf:
            total_calories_per_elf.append(sum(i))
        print("largest amount of calories =", max(total_calories_per_elf))
        elf_calories_totals_sorted = sorted(total_calories_per_elf)
        #print(list_calories_per_elf)
        #print(sum(elf_calories_totals_sorted[-3:]))
        # print("calories carried by top 3 elves =", sum(sorted(total_calories_per_elf)[:3]))

# not working as expected
def elf_most_calories_1pass(input):
    temp = 0
    highest = 0
    with open(input) as f:
        lines = f.readlines()
        #print(len(lines))
        for index, line in enumerate(lines):
            print(index, line)
            line = line.strip().rstrip()
            if line == '':
                if temp > highest:
                    highest = temp
                    temp = 0
            else:
                temp += int(line)
        if temp > highest:
            highest=temp
    print("one pass =", highest)


# Opponent A = rock, B = paper, C = scissors
# Player X = rock, Y = paper, Z = scissors
# rock = 1, paper = 2, scissors = 3
# lose = 0, draw = 3, win = 8
# part2 X = lose, Y = draw, Z = win
def rock_paper_scissors_sg(rps):
    rules_dict = {"A Y": 8, "A Z": 3, "A X": 4, "B X": 1, "B Z": 9, "B Y": 5, "C X": 7, "C Y": 2, "C Z": 6}
    score = 0
    with open(rps) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line in rules_dict:
                score += rules_dict.get(line)
            else:
                print("not in rules dict")
        print(score)


def rock_paper_scissors_p2(rps):
    rules_dict = {"AB": 8, "AC": 3, "AA": 4, "BA": 1, "BC": 9, "BB": 5, "CA": 7, "CB": 2, "CC": 6}
    score = 0
    with open(rps) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line[2] == 'Y':
                score += rules_dict.get(line[0] + line[0])
            elif line[2] == 'X' and line[0] == 'A':
                score += rules_dict.get((line[0] + 'C'))
            elif line[2] == 'X' and line[0] == 'B':
                score += rules_dict.get((line[0] + 'A'))
            elif line[2] == 'X' and line[0] == 'C':
                score += rules_dict.get((line[0] + 'B'))
            elif line[2] == 'Z' and line[0] == 'A':
                score += rules_dict.get((line[0] + 'B'))
            elif line[2] == 'Z' and line[0] == 'B':
                score += rules_dict.get((line[0] + 'C'))
            elif line[2] == 'Z' and line[0] == 'C':
                score += rules_dict.get(line[0] + 'A')
        print(score)


def rucksack_priority_sum(input):
    compartment_one = []
    compartment_two = []
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            half_list = int((len(line)-1) / 2)
            #print(half_list)
            compartment_one += [line[0:half_list]]
            compartment_two += [line[half_list:]]
        # for i in range(len(compartment_one)):
        #     print(compartment_one[i])
        #     if compartment_one[i] == compartment_two[i]:
        #         print(compartment_one[i])
        # print(compartment_one)
        # print(compartment_two)



if __name__ == '__main__':
    #elf_most_calories('input.txt')
    elf_most_calories('test.txt')
    #elf_most_calories_1pass("test.txt")
    # rock_paper_scissors_sg(rps.txt")
    #rock_paper_scissors_p2("rps.txt")
    #rucksack_priority_sum("rucksack.txt")
