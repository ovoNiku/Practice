package main

import (
	"strconv"
)


func narcissistic(n int) bool {
	s := strconv.Itoa(n)
	num := 0
	for i := 0; i < len(s); i++ {
		str := string(s[i])
		b, err := strconv.Atoi(str)
		if err != nil {
			println(err)
		}
		c := 1
		for a := 0; a < len(s); a++ {
			c *= b
		}
		num += c
	}
	return num == n
}



func fiber(n int) int {
	if n == 1 || n == 2 {
		return 1
	} else {
		n1 := 1
		n2 := 1
		rs := 0
		for i := 2; i < n; i++ {
			rs = n1 + n2
			n1, n2 = n2, rs
		}
		return rs
	}
}


func factorial(n int) int {
	a := 1
	for i := 1; i < n; i++ {
		a *= (i + 1)
	}
	return a
}


func addSquares(n int) int {
	a := 1
	for i := 1; i < n; i++ {
		a += (i + 1) * (i + 1)
	}
	return a
}


func strSymmetry(s string) bool {
	l := len(s)
	if l%2 == 0 {
		half := l / 2
		s1 := string(s[:half])
		s2 := string(s[half:])
		s3 := ""
		n := half - 1
		for i := n; i >= 0; i-- {
			s3 += (string(s2[i]))
		}
		return s1 == s3
	} else {
		return false
	}
}


func testNarc() {
	a := narcissistic(153)
	b := narcissistic(1533)
	c := narcissistic(1634)
	if a != true && b != false && c != true {
		println("narc is false")
	}
}


func testFiber() {
	a := fiber(1)
	b := fiber(3)
	c := fiber(5)
	if a != 1 && b != 2 && c != 5 {
		println("fiber is false")
	}
}


func testFactorial() {
	a := factorial(3)
	b := factorial(1)
	if a != 6 && b != 1 {
		println("factorial is false")
	}
}


func testAddSquares() {
	a := addSquares(3)
	b := addSquares(1)
	if a != 14 && b != 1 {
		println("add_squares is false")
	}
}


func teststrSymmetry()  {
	a:= strSymmetry("abba")
	b:=strSymmetry("aaca")
	c:=strSymmetry("aaa")
	if a != true && b != false && c != false{
		println("strSymmetry is false")
	}
}


func main() {
	testNarc()
	testFiber()
	testFactorial()
	testAddSquares()
	teststrSymmetry()
}
