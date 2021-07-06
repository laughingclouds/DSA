package main

func reverseString(s []byte) {
	length := len(s)

	left, right := 0, length-1

	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}
