package main

func canChange(start string, target string) bool {

	bs := []byte{}
	bt := []byte{}

	for i := 0; i < len(start); i++ {

		if start[i] != '_' {
			bs = append(bs, start[i])
		}

		if target[i] != '_' {
			bt = append(bt, target[i])
		}
	}

	return string(bs) == string(bt)
}

func main() {

	str := "_R"
	target := "R_"

	r := canChange(str, target)

	println(r)
}
