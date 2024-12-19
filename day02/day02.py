def is_safe(report):
    # Check if the report is increasing
    increasing_safetly = [ 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1) ] + [True]
    
    # Check if the report is decreasing
    decreasing_safetly = [ 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1) ] + [True]
    
    # Check the safety
    return all(decreasing_safetly) or all(increasing_safetly)

def main() -> None:
    # Read in the lists
    with open('day02-input.txt', 'r') as file:
        reports = [ list(map(int, line.strip().split())) for line in file ]
            
    # Check the safety of each report and output the total safe reports
    total = sum( 1 for report in reports if is_safe(report) )
            
    # Check the safety of each report and output the total safe reports (with problem dampener)
    total_dampener = sum( any( is_safe(report[:i] + report[i + 1:]) for i in range(len(report))) for report in reports )
            
    # Print the results
    print(f"Part one: {total}")
    print(f"Part two: {total_dampener}")

if __name__ == "__main__":
    main()