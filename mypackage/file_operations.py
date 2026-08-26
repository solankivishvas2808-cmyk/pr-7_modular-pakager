def create_file(filename):
    file = open(filename, "w")
    file.close()
    print("File created successfully!")


def write_file(filename, data):
    file = open(filename, "w")
    file.write(data)
    file.close()
    print("Data written successfully!")


def read_file(filename):
    file = open(filename, "r")
    print("File Content:")
    print(file.read())
    file.close()


def append_file(filename, data):
    file = open(filename, "a")
    file.write(data)
    file.close()
    print("Data appended successfully!")