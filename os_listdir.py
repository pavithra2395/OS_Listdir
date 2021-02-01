import os


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


res = {}
for file in files("."):
    # print (file)
    file_size = os.path.getsize(file)
    #     print("bytes: ", file_size)
    res[file] = file_size

print(res)

# path = "D:\\python"
