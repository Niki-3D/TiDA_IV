class MaximumSumSubarray:
    def __init__(self):
        pass

    def find_maximum_sum_subarray(self, input_array):
        if not input_array:
            return []

        array_length = len(input_array)

        current_sum = input_array[0]
        maximum_sum = input_array[0]

        current_start_index = 0
        maximum_start_index = 0
        maximum_end_index = 0

        for current_index in range(1, array_length):
            if current_sum < 0:
                current_sum = input_array[current_index]
                current_start_index = current_index
            else:
                current_sum += input_array[current_index]

            if current_sum > maximum_sum:
                maximum_sum = current_sum
                maximum_start_index = current_start_index
                maximum_end_index = current_index

        maximum_sum_subarray = input_array[maximum_start_index:maximum_end_index + 1]
        return maximum_sum_subarray

    def get_maximum_sum(self, input_array):
        maximum_sum_subarray = self.find_maximum_sum_subarray(input_array)
        return sum(maximum_sum_subarray) if maximum_sum_subarray else 0

    def run_test_cases(self, test_case_arrays):
        test_results = {}
        for test_case_index, test_case_array in enumerate(test_case_arrays):
            maximum_subarray = self.find_maximum_sum_subarray(test_case_array)
            maximum_sum = sum(maximum_subarray) if maximum_subarray else 0

            test_results[test_case_index] = {
                'input': test_case_array,
                'maximum_subarray': maximum_subarray,
                'maximum_sum': maximum_sum,
                'subarray_length': len(maximum_subarray)
            }
        return test_results

    def print_test_results(self, test_results):
        print("Maximum Sum Subarray Test Results:\n")
        for result_index, result_data in test_results.items():
            print(f"Test Case {result_index + 1}:")
            print(f"  Input: {result_data['input']}")
            print(f"  Maximum Subarray: {result_data['maximum_subarray']}")
            print(f"  Maximum Sum: {result_data['maximum_sum']}")
            print(f"  Subarray Length: {result_data['subarray_length']}")
            print()


def main():
    subarray_finder = MaximumSumSubarray()

    test_case_arrays = [
        [2, -4, 6, 8, -10, 100, -6, 5],  # Example from the problem
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Common test case
        [-1, -2, -3, -4, -5],  # All negative
        [5, 4, 3, 2, 1],  # All positive
        [],  # Empty array
        [42]  # Single element
    ]

    test_results = subarray_finder.run_test_cases(test_case_arrays)
    subarray_finder.print_test_results(test_results)


if __name__ == "__main__":
    main()