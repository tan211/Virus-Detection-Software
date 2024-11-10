import engine
import os

malware_checker = engine.malware_checker


#Malware Dectection In Folder
virusName = []
virusPath = []

try : 
    os.remove("switch_virusscanner.bb")
    os.remove("switch_io.bb")


except:pass
username = os.environ.get('USERNAME').upper().split(" ")

def virusScanner(path):

    # Get the list of all files in directory tree at given path
    dir_list = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]
        print([os.path.join(dirpath, file) for file in filenames])

    for i in dir_list:
        print(i)
        if malware_checker(i) != 0:
            try : 
                with open("switch_virusscanner.bb","a") as bb:

                    bb.write(i+"\n")
                    bb.close()
            except:pass

            print(i)
            virusName.append(malware_checker(i)+" :: File :: "+i)
            virusPath.append(i)


paths_to_scan = [
    r"C:\Windows\System32",
    r"C:\Windows\SysWOW64",
    r"C:\Windows\Temp",
    r"C:\Users\{}~1\AppData".format(username[0]),
    r"C:\Users\{}~1\Downloads".format(username[0]),
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup",
    r"C:\Program Files",
    r"C:\Program Files (x86)"
]

for path in paths_to_scan:
    virusScanner(path)


try : 
    with open("switch_io.bb","w") as bb:
        bb.write("1")
        bb.close()

except:pass
