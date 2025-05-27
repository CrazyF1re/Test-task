""" json     - to write data into file
    argparse - to parse arguments
    csvreader- own library to read csv files
"""
import json
import argparse
from csvreader import CsvReader


def create_payout(data:list[dict], filename:str):
    "Create payout, print it at terminal and save into file"
    departments:dict[str,list[dict]] = {}
    res:dict[str,list[dict]] = {}
    for i in data:
        res[i["department"]] = []
        if departments.get(i["department"]):
            departments[i["department"]].extend([i])
        else:
            departments[i["department"]]= [i]
    for dep,value in departments.items():
        for employe in value:
            hourly_rate = employe.get("hourly_rate") or employe.get("rate") \
                or employe.get("salary")
            res[dep].extend([{
                "name": employe["name"],
                "hours_worked": employe["hours_worked"],
                "hourly_rate" : hourly_rate,
                "payout" : int(employe["hours_worked"])*int(hourly_rate)
            }])
    with open(f"{filename}.json",'w', encoding='utf-8') as f:
        json.dump(res, f)
    #PAYOUT REPORT
    print("\t\tname\t\thours\trate\tpayout")
    for dep,employes in res.items():
        print(dep)
        for emp in employes:
            print(f"----------------{emp["name"]}", end="\t")
            print(f"{emp["hours_worked"]}", end="\t")
            print(f"{emp["hourly_rate"]}", end="\t")
            print(f"{emp["payout"]}", end="\n")
def main():
    "Main"
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", type=str, nargs='+', help="List of paths to .csv files")
    parser.add_argument("--report", type=str, default="payout",help="Name of output file")
    args = parser.parse_args()
    reader = CsvReader(args.paths)
    reader.read_files()
    data = reader.get_data()
    create_payout(data, args.report)



if __name__ == "__main__":
    main()
