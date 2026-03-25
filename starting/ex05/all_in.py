import sys


def get_data():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return states, capital_cities


def normalize(text):
	return " ".join(text.strip().split()).lower()


def build_lookup(states, capital_cities):
	state_to_capital = {}
	capital_to_state = {}

	for state_name, code in states.items():
		capital_name = capital_cities[code]
		state_to_capital[normalize(state_name)] = (state_name, capital_name)
		capital_to_state[normalize(capital_name)] = (state_name, capital_name)

	return state_to_capital, capital_to_state


def main():
	if len(sys.argv) != 2:
		return

	query = sys.argv[1]
	if ",," in query:
		return

	states, capital_cities = get_data()
	state_to_capital, capital_to_state = build_lookup(states, capital_cities)

	for raw_expr in query.split(","):
		display_expr = " ".join(raw_expr.strip().split())
		if not display_expr:
			continue

		key = display_expr.lower()
		if key in state_to_capital:
			state_name, capital_name = state_to_capital[key]
			print(f"{capital_name} is the capital of {state_name}")
		elif key in capital_to_state:
			state_name, capital_name = capital_to_state[key]
			print(f"{capital_name} is the capital of {state_name}")
		else:
			print(f"{display_expr} is neither a capital city nor a state")


if __name__ == '__main__':
	main()
