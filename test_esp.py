import subprocess

p1 = subprocess.run(['ls', '-la'], capture_output=True, text=True)

print(p1.stdout)