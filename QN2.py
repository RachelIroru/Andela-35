
def capitalize_sequences():
    number_of_squences = int(
        Numbers('Enter number sequences you want to enter: '))
    sequences = []
    for input in range(number_of_squences):
        sequences.append(input().upper())

    print()
    print('Capitalized Squences')
    print("="*20)
    for sequence in sequences:
        print(sequence)


capitalize_sequences()