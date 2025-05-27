import os



class CsvReader:
    def __init__(self, paths:list[str]):
        self.data = []
        self.paths = paths
        for path in paths:
            assert os.path.isfile(path), f"{path} - Incorrect path to file"
        with open(paths[0]) as f:
            self.args_order = tuple(f.readline().split(','))
        for path in paths:
            with open(path) as f:
                assert self.args_order == tuple(f.readline().split(',')) , \
                f"{path} - Incorrect order of arguments into file"

        
    def readFiles(self):
        for i in self.paths:
            self.readFile(i)
    
    def readFile(self, path:str):
        with open(path) as f:
            line:str = f.readline()
            while line:
                line = line.split(",")
                tmp_dict = {}
                for arg,value in zip(self.args_order,line):
                    tmp_dict[arg] = value
                self.data.append(tmp_dict)
                line = f.readline()

    def getData(self)-> list[dict]: 
        return self.data