class NonDecreasingSequenceGenerator:
    def __init__(self):
        pass

    def generate_sequences(self, target_sum):
        if target_sum <= 0:
            return []

        all_sequences = []
        self._generate_sequences_recursively(target_sum, 1, [], all_sequences)
        return all_sequences

    def _generate_sequences_recursively(self, remaining_sum, minimum_value, current_sequence, all_sequences):
        """
        Recursively generate all non-decreasing sequences.

        Args:
            remaining_sum: The remaining sum to achieve
            minimum_value: The minimum value allowed for the next number in sequence
            current_sequence: The current partial sequence being built
            all_sequences: List to store all valid sequences
        """
        # Base case: If remaining sum is 0, we found a valid sequence
        if remaining_sum == 0:
            all_sequences.append(current_sequence.copy())
            return

        for next_value in range(minimum_value, remaining_sum + 1):
            current_sequence.append(next_value)

            self._generate_sequences_recursively(
                remaining_sum - next_value,
                next_value,
                current_sequence,
                all_sequences
            )

            current_sequence.pop()

    def print_sequences(self, sequences):
        for sequence in sequences:
            print(" ".join(map(str, sequence)))


def main():
    generator = NonDecreasingSequenceGenerator()

    target_sum = int(input("Enter a target sum n: "))

    print(f"All non-decreasing sequences that sum to {target_sum}:")
    sequences = generator.generate_sequences(target_sum)
    generator.print_sequences(sequences)
    print(f"Total number of sequences: {len(sequences)}")


if __name__ == "__main__":
    main()