import subprocess

args = ("/home/daniela/Apps/kbmag/bin/x86_64-unknown-linux-gnu-gcc-default64/kbprog", "/home/daniela/Apps/kbmag/standalone/kb_data/f2")

popen = subprocess.Popen(args, stdout=subprocess.PIPE)

popen.wait()

output = popen.stdout.read()
print output
