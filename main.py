# import plot

arr1 = [0, 2, 1, 2, 1, 2]
arr2 = [0, 1, 0, 0, 0, 1, 2, 0, 2, 2, 3, 0, 1]
arr3 = [0, 1, 0, 2, 0, 3, 1, 1, 2, 0]
arr4 = [5, 2, 3, 2, 1, 2, 3, 4, 2, 4, 1, 0, 1, 5, 3]
arr5 = [0, 3, 2, 1, 2]
arr6 = [0, 3, 2, 1, 3]

all_tests = [
    (arr1, 2),
    (arr2, 6),
    (arr3, 5),
    (arr4, 35),
    (arr5, 1),
    (arr6, 3),
]


def calc_water_1(arr_heights: list[int]) -> int:
    curr_count = 0
    curr_max = 0

    for index, height in enumerate(arr_heights):
        diff = curr_max - height
        if diff <= 0:
            curr_max = height
        elif diff > 0:
            curr_count += diff

    return curr_count


def calc_water_2(arr_heights: list[int]) -> int:
    curr_count = 0
    curr_max = 0

    for index, height in enumerate(arr_heights):
        diff = curr_max - height
        if diff <= 0:
            curr_max = height
        elif diff > 0:
            curr_count += diff

    return curr_count


def calc_water_3(arr_heights: list[int]) -> int:
    # Save total water count
    total_count = 0
    # keeps save the current max number
    curr_max = 0
    # keeps save the current min number
    curr_min = 0
    # keeps save the accumulate of water count while
    # not encounter with curr_max again
    curr_accum = 0
    # Keeps count of the sum of local minimums
    same_min_count = 0
    # Keeps info if just passed a maximum
    first_down = True

    for index, height in enumerate(arr_heights):
        diff = curr_max - height
        if diff <= 0:
            # print(index, curr_accum, "accum", sep="\t")
            curr_max = height
            total_count += curr_accum
            curr_accum = 0
            first_down = True
            same_min_count = 0
        else:
            min_diff = height - curr_min
            if min_diff <= 0 or first_down:
                curr_accum += diff
            else:
                # print(
                #     index,
                #     curr_accum,
                #     min_diff,
                #     same_min_count,
                #     total_count,
                #     "diff",
                #     sep="\t",
                # )
                min_to_take = min_diff * same_min_count
                curr_accum += diff - min_to_take
                total_count += min_to_take

            same_min_count = same_min_count + 1 if curr_min == height else 1
            curr_min = height
            first_down = False

    return total_count


if __name__ == "__main__":
    for test_data in all_tests:
        arr, res = test_data
        print("Para el vector:", arr)
        print("Hay", calc_water_3(arr), "conteos de agua.")
        print("Deberia contar", res, "conteos de agua.")
        print()

    # plot.plot_arrays(arr1, arr2, arr3, arr4, arr5, arr6)
