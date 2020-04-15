import os


class DataSave:

    def __init__(self, path):
        self.path = path

    def save(self, data):
        if not os.path.exists(self.path):
            raise FileExistsError("The path does not exist")
        with open(self.path, 'a') as fp:
            print("Start write data")
            fp.write(str(data) + '\n')
        fp.close()


if __name__ == "__main__":
    test_data = 'This is a test, \n save it'
    save_path = './data/hi.txt'
    ds = DataSave(save_path)
    ds.save(test_data)
