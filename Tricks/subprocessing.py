import subprocess

#subprocess.run(['ls', '-la'])

proc = subprocess.run(['ls', '-la'])

print(proc.args)
