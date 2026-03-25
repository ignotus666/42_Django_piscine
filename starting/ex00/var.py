def my_var():
	int_var = 42
	str_num_var = "42"
	str_text_var = "quarante-deux"
	float_var = 42.0
	bool_var = True
	list_var = [42]
	dict_var = {42: 42}
	tuple_var = (42,)
	set_var = set()

	variables = [
		int_var,
		str_num_var,
		str_text_var,
		float_var,
		bool_var,
		list_var,
		dict_var,
		tuple_var,
		set_var,
	]

	for value in variables:
		print(f"{value} has a type {type(value)}")


if __name__ == '__main__':
	my_var()
