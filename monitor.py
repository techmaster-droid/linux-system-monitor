import subprocess

result = subprocess.run(
	["ps", "aux"],
	capture_output=True,
	text=True
)

lines = result.stdout.splitlines()

process_count = {}

suspicious = [
    "nc",
    "netcat",
    "ncat",
    "miner",
    "reverse_shell.py"
]

for line in lines[1:]:
	content = line.split()

	if len(content) > 10:
		command = content[10]
		process_count[command] = process_count.get(command,0)+1

found = 0

for i in process_count:
	print(f"{i} -> {process_count[i]}")
	if i in suspicious:
		print(f"\nALERT: Suspicious process detected: {i}\n")
		found += 1

if found == 0:
	print("\nNo suspicious processes detected\n")
