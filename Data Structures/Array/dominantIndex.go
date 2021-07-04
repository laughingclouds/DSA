package main

func dominantIndex(arr []int) int {
	maxIndex, m := 0, 0

	for index, value := range arr {
		if m < value {
			m = value
			maxIndex = index
		}
	}

	for _, value := range arr {
		if m != value && m < 2*value {
			maxIndex = -1
			break
		}
	}
	return maxIndex
}
