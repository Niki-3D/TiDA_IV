class AlphabetPermutationGenerator:
    def __init__(self):
        pass

    def generate_all_permutations(self, number_of_letters):
        if number_of_letters <= 0:
            return []

        alphabet_letters = [chr(ord('a') + i) for i in range(number_of_letters)]
        all_permutations = []

        self._generate_permutations_recursively(alphabet_letters, [], all_permutations)

        return all_permutations

    def _generate_permutations_recursively(self, remaining_letters, current_permutation, all_permutations):
        if not remaining_letters:
            all_permutations.append(''.join(current_permutation))
            return

        for index, letter in enumerate(remaining_letters):
            current_permutation.append(letter)
            new_remaining_letters = remaining_letters[:index] + remaining_letters[index + 1:]

            self._generate_permutations_recursively(new_remaining_letters, current_permutation, all_permutations)

            current_permutation.pop()

    def print_permutations(self, permutations):
        for permutation in permutations:
            print(permutation)

    def generate_and_print_permutations(self, number_of_letters):
        permutations = self.generate_all_permutations(number_of_letters)
        self.print_permutations(permutations)
        return len(permutations)


class MemoryEfficientPermutationGenerator:
    def __init__(self):
        pass

    def generate_and_print_permutations(self, number_of_letters):
        if number_of_letters <= 0:
            return 0

        alphabet_letters = [chr(ord('a') + i) for i in range(number_of_letters)]
        permutation_count = [0]

        self._generate_and_print_permutations_recursively(alphabet_letters, [], permutation_count)

        return permutation_count[0]

    def _generate_and_print_permutations_recursively(self, remaining_letters, current_permutation, permutation_count):
        if not remaining_letters:
            print(''.join(current_permutation))
            permutation_count[0] += 1
            return

        for index, letter in enumerate(remaining_letters):
            current_permutation.append(letter)
            new_remaining_letters = remaining_letters[:index] + remaining_letters[index + 1:]

            self._generate_and_print_permutations_recursively(
                new_remaining_letters,
                current_permutation,
                permutation_count
            )

            current_permutation.pop()


def calculate_factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def main():
    use_memory_efficient = True

    number_of_letters = int(input("Enter the number of letters (n): "))

    if number_of_letters <= 0:
        print("Please enter a positive integer.")
        return

    expected_count = calculate_factorial(number_of_letters)
    print(f"Generating all {expected_count} permutations of the first {number_of_letters} letters:")

    if use_memory_efficient:
        generator = MemoryEfficientPermutationGenerator()
        actual_count = generator.generate_and_print_permutations(number_of_letters)
    else:
        generator = AlphabetPermutationGenerator()
        actual_count = generator.generate_and_print_permutations(number_of_letters)

    print(f"Generated {actual_count} permutations.")


if __name__ == "__main__":
    main()