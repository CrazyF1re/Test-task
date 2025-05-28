import pytest
from csvreader import CsvReader


def test_init(reader:CsvReader):
    "test instance atributes"
    assert isinstance(reader,CsvReader)
    assert isinstance(reader.data,list)
    assert isinstance(reader.paths,list)

@pytest.mark.parametrize("paths",[[".\csv\data1.csv", ".\csv\data2.csv", ".\csv\data3.csv"],
                                  [".\csv\data1.csv"],
                                  [".\csv\data2.csv", ".\csv\data3.csv"]])
def test_set_paths(reader:CsvReader, paths:list[str]):
    reader.set_paths(paths)
    for path in paths:
        assert path in reader.paths

@pytest.mark.parametrize("expected",[[{'id': '1', 'email': 'alice@example.com', 'name': 'Alice Johnson', 'department': 'Marketing', 'hours_worked': '160', 'hourly_rate': '50'},
                {'id': '2', 'email': 'bob@example.com', 'name': 'Bob Smith', 'department': 'Design', 'hours_worked': '150', 'hourly_rate': '40'},
                {'id': '3', 'email': 'carol@example.com', 'name': 'Carol Williams', 'department': 'Design', 'hours_worked': '170', 'hourly_rate': '60'}]])
def test_read_file(reader:CsvReader, expected):
    reader.read_file(".\csv\data1.csv")
    for i in expected:
        assert i in reader.data

@pytest.mark.parametrize("expected",[[{'department': 'HR', 'id': '101', 'email': 'grace@example.com', 'name': 'Grace Lee', 'hours_worked': '160', 'rate': '45'},
                {'department': 'Marketing', 'id': '102', 'email': 'henry@example.com', 'name': 'Henry Martin', 'hours_worked': '150', 'rate': '35'},
                {'department': 'HR', 'id': '103', 'email': 'ivy@example.com', 'name': 'Ivy Clark', 'hours_worked': '158', 'rate': '38'},
                {'email': 'karen@example.com', 'name': 'Karen White', 'department': 'Sales', 'hours_worked': '165', 'salary': '50', 'id': '201'},
                {'email': 'liam@example.com', 'name': 'Liam Harris', 'department': 'HR', 'hours_worked': '155', 'salary': '42', 'id': '202'},
                {'email': 'mia@example.com', 'name': 'Mia Young', 'department': 'Sales', 'hours_worked': '160', 'salary': '37', 'id': '203'}]])
def test_read_files(reader:CsvReader, expected):
    reader.set_paths([".\csv\data2.csv", ".\csv\data3.csv"])
    reader.read_files()
    for i in expected:
        assert i in reader.data

def test_get_data(reader:CsvReader):
    reader.set_paths([".\csv\data1.csv"])
    reader.read_files()
    for i in reader.get_data():
        assert i in reader.data
