import hashlib
import os

# --------------Check-Hash-With-Malware---------------

# def md5_hash(filename):
#     with open(filename, 'rb') as f:
#         bytes = f.read()
#         md5hash = hashlib.md5(bytes).hexdigest()
#         f.close
#     return md5hash

# def malware_checker(pathOfFile):
#     hash_malware_check = md5_hash(pathOfFile)
#     malware_hashes = open("virusHash.txt", "r")
#     malware_hashes_read = malware_hashes.read().splitlines()
#     malware_hashes.close()
    
#     for check in malware_hashes_read:
#         if check == hash_malware_check:
#             return "red"
#     return "green"
        
# print(malware_checker("sample.jpg"))

# ---------Hash+NameMalware------------


# def md5_hash(filename):
#     with open(filename, 'rb') as f:
#         bytes = f.read()
#         md5hash = hashlib.md5(bytes).hexdigest()
#         f.close
#     return md5hash

# def malware_checker(pathOfFile):
#     hash_malware_check = md5_hash(pathOfFile)
#     malware_hashes = open("virusHash.txt", "r")
#     malware_hashes_read = malware_hashes.read()
#     malware_hashes.close()
    
#     virusInfo = open("virusInfo.txt", "r").readlines()
    
#     if malware_hashes_read.find(hash_malware_check) != -1:
#         return virusInfo[malware_hashes_read.index(hash_malware_check)]
#     else:
#         return 0
        
# print(malware_checker("sample.jpg"))

# ----------------------------------

# malware_hashes = list(open("virusHash.txt", "r").read().split('\n'))
    
# virusInfo = list(open("virusInfo.txt", "r").read().split("\n"))

# def sha256_hash(filename):
#     with open(filename, 'rb') as f:
#         bytes = f.read()
#         sha256_hash = hashlib.sha256(bytes).hexdigest()
#         f.close
#     return sha256_hash

# def malware_checker(pathOfFile):
#     global malware_hashes
#     global virusInfo
#     hash_malware_check = sha256_hash(pathOfFile)
#     counter = 0
    
#     for i in malware_hashes:
#         if i == hash_malware_check:
#             return virusInfo[counter]
#         counter +=1
#     return 0
        
# print(malware_checker("sample.jpg"))

# ------------Folder-Scan-Hash---------

# malware_hashes = list(open("virusHash.txt", "r").read().split('\n'))
    
# virusInfo = list(open("virusInfo.txt", "r").read().split("\n"))

# def sha256_hash(filename):
#     with open(filename, 'rb') as f:
#         bytes = f.read()
#         sha256_hash = hashlib.sha256(bytes).hexdigest()
#         f.close
#     return sha256_hash

# def malware_checker(pathOfFile):
#     global malware_hashes
#     global virusInfo
#     hash_malware_check = sha256_hash(pathOfFile)
#     counter = 0
    
#     for i in malware_hashes:
#         if i == hash_malware_check:
#             return virusInfo[counter]
#         counter +=1
#     return 0

# virusName = []

# def folderScanner():
#     path = "D:\\Labs\\Chapter_3L"
#     dir_list = os.listdir(path)
    
#     fileN = ""
    
#     for i in dir_list:
#         fileN = path+"\\"+i
#         if malware_checker(fileN) != 0:
#             virusName.append(malware_checker(fileN)+" :: File :: " + i)
        
# folderScanner()
# print(virusName) 

# ------------------------Deep-Scanning-----------------------+ # --------------------VirusRemover-----------------


# malware_hashes = list(open("virusHash.txt", "r").read().split('\n'))
    
# virusInfo = list(open("virusInfo.txt", "r").read().split("\n"))

# def sha256_hash(filename):
#     try:
#         with open(filename, 'rb') as f:
#             bytes = f.read()
#         sha256_hash = hashlib.sha256(bytes).hexdigest()
#         f.close
#         return sha256_hash
#     except:
#         return 0

# def malware_checker(pathOfFile):
#     global malware_hashes
#     global virusInfo
#     hash_malware_check = sha256_hash(pathOfFile)
#     counter = 0
    
#     for i in malware_hashes:
#         if i == hash_malware_check:
#             return virusInfo[counter]
#         counter +=1
#     return 0

# virusName = []
# virusPath = []

# def deepScanning(path):
    
#     dir_list = list()
    
#     for (dirpath, dirnames, filenames) in os.walk(path):
#         dir_list += [os.path.join(dirpath, file) for file in filenames]
        
#     for i in dir_list:
#         print(i)
#         if malware_checker(i) != 0:
#             virusName.append(malware_checker(i)+" :: File :: " + i)
#             virusPath.append(i)
            
# def virusRemover(path):
#     deepScanning(path)
#     if virusPath:
#         for i in virusPath:
#             os.remove(i)
#     else:
#         return 0
        
# virusRemover("D:\\Labs\\Chapter_3L")

# # --------------------JunkFile-Remover-----------------

def junkFileRemover():
    
    temp_list = list ()
    
    username = os.environ.get('USERNAME').upper().split(" ")
    # ---temp---
    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Temp"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]
        
    # ---%temp%---
    for (dirpath, dirnames, filenames) in os.walk("C:\\Users\\{}\\AppData\\Local\\Temp".format(username[0])):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    # ---prefetch---
    for (dirpath, dirnames, filenames) in os.walk("C:\\Windows\\Prefetch"):
        temp_list += [os.path.join(dirpath, file) for file in filenames]
        temp_list += [os.path.join(dirpath, file) for file in dirnames]

    if temp_list:
        for i in temp_list:
            print(i)
            
            try:
                os.remove(i)
                
            except:
                pass
            
            try: 
                os.rmdir
            except:
                pass
    else:
        return 0

junkFileRemover()

# -----------ramBooter------------

# def ramBooter():
#     taskList = ["notepad.exe", "msedge.exe", "cmd.exe"]
    
#     for i in taskList:
#         try:
#             os.system("taskkill /f /im {}".format(i))
#         except:
#             print(f"Failed to kill {i}, moving to the next process.")
#             continue

# ramBooter()
