import heapq

# Function to calculate the sum of 10000 medians modulo 10000
def calculate_median_sum(nums):
    min_heap = []  # For the larger half of the numbers
    max_heap = []  # For the smaller half of the numbers
    median_sum = 0

    for num in nums:
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance the heaps to ensure their sizes differ by at most 1
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate the median and update the sum
        if len(max_heap) == len(min_heap):
            median = -max_heap[0]
        else:
            median = -max_heap[0]

        median_sum = (median_sum + median) % 10000

    return median_sum

# Read integers from a file "Median.txt" and calculate the sum of 10000 medians
def main():
    nums = []
    with open("Median.txt") as file:
        for line in file:
            nums.append(int(line.strip()))
    median_sum = calculate_median_sum(nums)
    print(median_sum)

if __name__ == "__main__":
    main()

