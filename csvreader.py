"To check valide path or not"
import os



class CsvReader:
    """
    instead of csv module class allows read csv files by path
    """
    def __init__(self, paths:list[str]):
        self.data = []
        self.paths = paths
        for path in paths:
            assert os.path.isfile(path), f"{path} - Incorrect path to file"
    def read_files(self):
        "read all files into list"
        for i in self.paths:
            self.read_file(i)
    def read_file(self, path:str):
        "read file using path"
        with open(path, encoding='utf-8') as f:
            args_order = tuple(f.readline().rstrip().split(','))
            line:str = f.readline().rstrip()
            while line:
                line = line.rstrip().split(",")
                tmp_dict = {}
                for arg,value in zip(args_order,line):
                    tmp_dict[arg] = value
                self.data.append(tmp_dict)
                line = f.readline()

    def get_data(self)-> list[dict]:
        "returns data as list of dictionaries" 
        return self.data
