import subprocess

def get_cpu_info():

	result= subprocess.run(
        	["top", "-bn1"],
        	capture_output = True,
        	text = True
	)

	lines = result.stdout.splitlines()

	cpu_line = lines[2]

	cpu_list = cpu_line.split(",")

	cpu_with_id = cpu_list[3]

	cpu_idle = cpu_with_id.split()[0]

	cpu_usage = round(float(100 - float(cpu_idle)), 2)
	print("CPU Summary")
	print("-----------")
	print(f"\nCPU Usage: {cpu_usage}%")
	print(f"CPU Idle: {cpu_idle}%\n")


def get_memory_info():
	result = subprocess.run(
	        ["free", "-h"],
        	capture_output = True,
        	text=True
	)

	lines = result.stdout.splitlines()

	line = lines[1]

	memory_data = line.split()

	print("Memory Summary")
	print("--------------")
	print(f"\nTotal Memory: {memory_data[1]}")
	print(f"Used Memory: {memory_data[2]}")
	print(f"Free Memory: {memory_data[3]}\n")


def get_process_info():
	print("Process Summary")
	print("---------------\n")
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

	found = False

	for i in process_count:
        	print(f"{i} -> {process_count[i]}")
        	if i in suspicious:
                	print(f"\nALERT: Suspicious process detected: {i}\n")
                	found =True

	if not found:
        	print("\nNo suspicious processes detected\n")


print("Linux System Monitor\n")

get_cpu_info()
get_memory_info()
get_process_info()
