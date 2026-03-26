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

def build_lookup(states, capital_cities):
    code_to_state = {code: state for state, code in states.items()}
    lookup = {}
    for code, city in capital_cities.items():
        if state := code_to_state.get(code):
            pair = (state, city)
            lookup[state.lower()] = pair
            lookup[city.lower()] = pair
    return lookup

def clean_strings(arg_str):
    return [clean for expr in arg_str.split(",") if (clean := " ".join(expr.split()))]

def all_in():
    if len(sys.argv) != 2:
        return

    lookup = build_lookup(states, capital_cities)
    for expr in clean_strings(sys.argv[1]):
        if found := lookup.get(expr.lower()):
            print(f"{found[1]} is the capital of {found[0]}")
        else:
            print(f"{expr} is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()
