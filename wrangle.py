import csv # give python csv superpowers

with open(r"uk-towns-sample.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for town in reader:
        if town["county"] == "Warwickshire":
            print(town["name"] + " is in " + town["local_government_area"])