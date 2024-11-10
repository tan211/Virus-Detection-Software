import engine
import os
import sys

# Kiểm tra tham số
if len(sys.argv) > 1:
    source_path = sys.argv[1]
    if not os.path.exists(source_path):
        print(f"The provided path does not exist: {source_path}")
        sys.exit(1)
else:
    print("No source path provided")
    sys.exit(1)

malware_checker = engine.malware_checker

# Malware Detection In Folder
virusName = []
virusPath = []

# Xóa tệp nếu tồn tại
for file in ["switch_virusscanner.bb", "switch_io.bb"]:
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error removing file {file}: {e}")

def virusScanner(path):
    # Lấy danh sách tất cả các tệp trong thư mục
    dir_list = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        dir_list.extend([os.path.join(dirpath, file) for file in filenames])
        print([os.path.join(dirpath, file) for file in filenames])

    for i in dir_list:
        print(i)
        if malware_checker(i) != 0:
            try:
                with open("switch_virusscanner.bb", "a", encoding="utf-8") as bb:
                    bb.write(i + "\n")
            except Exception as e:
                print(f"Error writing to file: {e}")

            print(i)
            virusName.append(malware_checker(i) + " :: File :: " + i)
            virusPath.append(i)

virusScanner(source_path)

try:
    with open("switch_io.bb", "w", encoding="utf-8") as bb:
        bb.write("1")
except Exception as e:
    print(f"Error writing to file: {e}")
