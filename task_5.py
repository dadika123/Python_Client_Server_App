import subprocess

targets_ping = ('yandex.ru', 'youtube.com')
for target in targets_ping:
    args = ['ping', target]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('windows-1251').encode('utf-8')
        print(line.decode('utf-8'))
