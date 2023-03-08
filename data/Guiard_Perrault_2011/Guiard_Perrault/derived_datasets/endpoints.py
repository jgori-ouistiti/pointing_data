import pandas
import json

main_dataframe = None

with open("segmented_data_JG_060323.json", "r") as _file:
    container = json.load(_file)

full_dataframe = pandas.DataFrame(
    columns=[
        "Participant",
        "X0",
        "Y0",
        "Xt",
        "Yt",
        "MT",
        "strategy",
        "block",
    ]
)

for participant in container:
    for condition in container[participant]:
        for mov in container[participant][condition]:
            values = container[participant][condition][mov]
            t, x = values["t"], values["x"]
            strategy, block = condition.split("_")
            row = {
                "Participant": int(float(participant)),
                "X0": x[0],
                "Xf": x[-1],
                "Xt": None,
                "MT": t[-1] - t[0],
                "strategy": strategy,
                "block": block,
                "A": 150,
            }
            full_dataframe = full_dataframe.append(row, ignore_index=True)

full_dataframe.to_csv("fitts.csv")
