import subprocess

result = subprocess.run(
	["free", "-h"],
	capture_output = True,
	text=True
)

lines = result.stdout.splitlines()

line = lines[1]

memory_data = line.split()

print("Memory Summary")
print(f"\nTotal Memory: {memory_data[1]}")
print(f"Used Memory: {memory_data[2]}")
print(f"Free Memory: {memory_data[3]}")
