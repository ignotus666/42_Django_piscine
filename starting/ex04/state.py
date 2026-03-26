import sys

states = {
	"Oregon": "OR",
	"Alabama": "AL",
	"New Jersey": "NJ",
	"Colorado": "CO"
}

capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
}

def main():
	if len(sys.argv) != 2:
		return

	capital = sys.argv[1]
	state_code = None
	for code, city in capital_cities.items():
		if city == capital:
			state_code = code
			break

	if state_code is None:
		print("Unknown capital city")
		return

	states_by_code = {code: state for state, code in states.items()}
	print(states_by_code[state_code])

if __name__ == '__main__':
	main()
