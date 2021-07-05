package main

func generate(numRows int) [][]int {
	if numRows == 1 {
		return [][]int{{1}}
	}
	triangle := [][]int{{1}, {1, 1}}

	for i := 2; i < numRows; i++ {
		row := []int{1}

		for j := 1; j < i; j++ {
			row = append(row, triangle[i-1][j-1]+triangle[i-1][j])
		}
		row = append(row, 1)
		triangle = append(triangle, row)
	}
	return triangle
}
