import re

def multiplication(data, part):
    # Part 1
    if part == 1:
        # Find all matches in sequence
        matches = re.findall(r"mul\((\d+),(\d+)\)", data)
        return sum([int(match[0])*int(match[1]) for match in matches])
    # Part 2
    elif part ==2:
        # Find all matches in sequence, including "don't()" and "do()"
        matches = re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)", data)
        # Process the instructions
        do = True
        total = 0
        for match in matches:
            instruction = match.group()
            # If do instruction, enable multiplication
            if instruction == "do()":
                do = True
            # If don't instruction, disable multiplication
            elif instruction == "don't()":
                do = False
            # Multiply instruction
            else:
                if do: # if enabled, add to the total
                    x, y = map(int, match.groups())
                    total += x * y
        return total

def main() -> None:
    # Read in the data
    with open('day03-input.txt', 'r') as file:
        data = file.read()

    # Print the results
    print(f"Part one: {multiplication(data, part=1)}")
    print(f"Part two: {multiplication(data, part=2)}")

if __name__ == "__main__":
    main()