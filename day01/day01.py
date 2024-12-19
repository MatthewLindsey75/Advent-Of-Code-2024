# Count occurences in the other list
def count(number, list):
    return sum( 1 for round in range(len(list)) if number == list[round] )

def main() -> None:
    # Read in the lists
    with open('day01-input.txt', 'r') as file:
        lines = [map(int, line.strip().split()) for line in file]
        list1, list2 = map(list, zip(*lines))

    # Sort the two lists
    list1.sort()
    list2.sort()

    # Calculate the distance score
    distance_score = sum( abs(list1[i] - list2[i]) for i in range(len(list1)) )

    # Calculate the similarity score
    similarity_score = sum( list1[i] * count(list1[i], list2) for i in range(len(list1)) )
        
    # Print the results
    print(f"Part one: {distance_score}")
    print(f"Part two: {similarity_score}")
    
if __name__ == "__main__":
    main()