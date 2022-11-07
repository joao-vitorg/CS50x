import csv
import sys
from csv import DictReader

T_STR = dict[str, str]


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    db: dict[str, T_STR] = {}
    sequences: list[str]

    with open(sys.argv[1], "r") as f:
        reader: DictReader[T_STR] = csv.DictReader(f)
        sequences = reader.fieldnames[1:]
        for person in reader:
            db[person.pop("name")] = person

    # Read DNA sequence file into a variable
    dna: str
    with open(sys.argv[2], "r") as f:
        dna = f.read()

    # Find the longest match of each STR in DNA sequence
    person: T_STR = {}
    for sequence in sequences:
        lm = longest_match(dna, sequence)
        person[sequence] = str(lm)

    # Check database for matching profiles
    for name, value in db.items():
        if person == value:
            print(name)
            return

    print("No match")
    return


def longest_match(sequence: str, subsequence: str) -> int:
    """Returns length of the longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
