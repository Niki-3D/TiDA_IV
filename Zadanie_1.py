class LongestIncreasingSubsequence:
    def __init__(self):
        pass

    def find_sequence(self, input_array):
        if not input_array:
            return []

        array_length = len(input_array)
        subsequence_lengths = [1] * array_length
        previous_indices = [-1] * array_length

        for current_index in range(1, array_length):
            for previous_index in range(current_index):
                if input_array[current_index] > input_array[previous_index] and subsequence_lengths[current_index] < subsequence_lengths[previous_index] + 1:
                    subsequence_lengths[current_index] = subsequence_lengths[previous_index] + 1
                    previous_indices[current_index] = previous_index

        maximum_length = max(subsequence_lengths)
        ending_index = subsequence_lengths.index(maximum_length)

        reconstructed_sequence = []
        while ending_index != -1:
            reconstructed_sequence.append(input_array[ending_index])
            ending_index = previous_indices[ending_index]

        return reconstructed_sequence[::-1]

    def get_sequence_length(self, input_array):
        return len(self.find_sequence(input_array))

    def run_test_cases(self, test_case_arrays):
        test_results = {}
        for test_case_index, test_case_array in enumerate(test_case_arrays):
            increasing_subsequence = self.find_sequence(test_case_array)
            subsequence_length = len(increasing_subsequence)
            test_results[test_case_index] = {
                'input': test_case_array,
                'sequence': increasing_subsequence,
                'length': subsequence_length
            }
        return test_results

    def print_test_results(self, test_results):
        print("Longest Increasing Subsequence Test Results:\n")
        for result_index, result_data in test_results.items():
            print(f"Test Case {result_index + 1}:")
            print(f"  Input: {result_data['input']}")
            print(f"  Sequence: {result_data['sequence']}")
            print(f"  Length: {result_data['length']}")
            print()


def main():
    subsequence_finder = LongestIncreasingSubsequence()

    test_case_arrays = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],
        [3, 4, 5, 1],
        [50, 3, 10, 7, 40, 80],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [42]
    ]

    test_results = subsequence_finder.run_test_cases(test_case_arrays)
    subsequence_finder.print_test_results(test_results)


if __name__ == "__main__":
    main()