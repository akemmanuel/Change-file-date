import subprocess as sub
import os
from dateutil import parser

#time_string = input("Zeit? ")  # Replace this with your time string
#time_obj = parser.parse(time_string).time()
#formatted_time = time_obj.strftime("%Y-%m-%d %H:%M:%S")
#print(formatted_time)


sub.getoutput("timedatectl set-ntp false")
sub.getoutput('sudo timedatectl set-time "1999-01-01 10:13:13"')
source_file = "test.txt"
try:
    with open(source_file, 'rb') as file:
        content = file.read()

    os.remove(source_file)

    with open(source_file, 'wb') as new_file:
        new_file.write(content)
except FileNotFoundError:
    print(f"Die Datei {source_file} existiert nicht.")

sub.getoutput("timedatectl set-ntp true")

