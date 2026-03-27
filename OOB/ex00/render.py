import sys
import os
import re

if len(sys.argv) != 2:
	print ("An argument must be provided!")
	sys.exit(1)

if os.path.splitext(sys.argv[1])[1] != ".template":
	print ("Wrong file extension!")
	sys.exit(1)

f = sys.argv[1]

if not os.path.isfile(f):
	print("File does not exist!")
	sys.exit(1)

try:
	with open(f,"r") as file_obj:
		template_content = file_obj.read()
except OSError:
	print("Can't read file!")
	sys.exit(1)

settings_dict = {}

try:
	with open("settings.py", "r") as settings_file:
		for line in settings_file:
			match = re.match(r'^\s*([a-zA-Z_]\w*)\s*=\s*"([^"]*)"\s*$', line)
			if not match:
				continue
			key = match.group(1)
			value = match.group(2)
			settings_dict[key] = value
except OSError:
	print("Can't read settings.py!")
	sys.exit(1)

rendered_content = template_content
for key, value in settings_dict.items():
	rendered_content = rendered_content.replace("{"+ key +"}", value)

output_file = os.path.splitext(f)[0] + ".html"
try:
	with open(output_file, "w") as html_file:
		html_file.write(rendered_content)
except OSError:
	print("Can't write html file!")
	sys.exit(1)
