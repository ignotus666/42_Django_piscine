import sys
import os

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