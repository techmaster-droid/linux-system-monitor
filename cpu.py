import subprocess

result= subprocess.run(
	["top", "-bn1"],
	capture_output = True,
	text = True
)

lines = result.stdout.splitlines()

cpu_line = lines[2]

cpu_list = cpu_line.split(",")

cpu_with_id = cpu_list[3]

cpu_without_id = cpu_with_id.split(" ")[0]

cpu_usage = round(float(100 - float(cpu_without_id)), 2)
print("CPU Summary")
print(f"\nCPU Usage: {cpu_usage}%")
print(f"CPU Idle: {cpu_without_id}%")
