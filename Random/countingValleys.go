package main

func countingValleys(steps int32, path string) int32 {
	step, count := int32(0), int32(0)

	if steps == 2 {
		if path[0] == 'D' {
			return 1
		} else {
			return 0
		}
	}
	for _, v := range path {
		if v == 'D' {
			step--
		} else {
			step++

			if step == 0 {
				count++
			}
		}
	}
	return count
}