#!/usr/bin/python3
import base64, codecs, os, sys

print("pydeobfuscate by Noxturnix")
print("Source code available at https://github.com/Noxturnix/pydeobfuscate")

if len(sys.argv) == 3:
	fileLocation = sys.argv[1]
	outputLocation = sys.argv[2]

	solvedCode = ""

	while True:
		if solvedCode:
			code = solvedCode
		else:
			code = open(fileLocation, "r", encoding="utf-8").read()

		code = [line for line in code.split("\n") if line != ""]
		code = code[:-1]
		code = "\n".join(code)
		breakLoop = False
		if all([obfsKeyword in code for obfsKeyword in ["magic", "love", "god", "destiny", "joy", "trust", "eval"]]):
			eval(compile(code,'<string>','exec'))
		else:
			breakLoop = True
		
		solvedCode = base64.b64decode(trust).decode("utf-8")
		if breakLoop:
			open(outputLocation, "w", encoding="utf-8").write(solvedCode)
			break

	print("\033[1;32mFile deobfuscated.\033[0m")	
else:
	pyname = sys.argv[0]
	print("Usage: %s [source] [output]" % (pyname))
