import platform
import subprocess

targets_ping = ('yandex.ru', 'youtube.com')
for target in targets_ping:
    if platform.system() == 'Windows':
        args = ['ping', target]
    else:
        args = ['ping', '-c', 4, target]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
