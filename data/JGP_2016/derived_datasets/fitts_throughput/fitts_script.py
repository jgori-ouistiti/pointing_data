import pathlib
import os

original_dataset_directory = (
    pathlib.Path(__file__).resolve().parents[2] / "original_dataset"
).resolve()


import pandas

main_dataframe = None

for _file in os.listdir(original_dataset_directory):
    file_full_path = (original_dataset_directory / _file).resolve()
    full_dataframe = pandas.read_csv(file_full_path)
    dataframe = full_dataframe[
        [
            "Subject",
            "Practice?",
            "A",
            "W",
            "StartX",
            "StartY",
            "EndX",
            "EndY",
            "TargetX",
            "TargetY",
            "Duration",
        ]
    ]
    dataframe = dataframe[dataframe["Practice?"] == 0]
    if main_dataframe is None:
        main_dataframe = dataframe
    else:
        main_dataframe = pandas.concat(
            [main_dataframe, dataframe], ignore_index=True, join="outer"
        )

# remove practice info
main_dataframe = main_dataframe.drop(labels="Practice?", axis=1)
# rescale in seconds
main_dataframe["Duration"] = main_dataframe["Duration"] / 1000


main_dataframe = main_dataframe.rename(
    columns={
        "Subject": "Participant",
        "StartX": "X0",
        "StartY": "Y0",
        "EndX": "Xf",
        "EndY": "Yf",
        "TargetX": "Xt",
        "TargetY": "Yt",
        "Duration": "MT",
    }
)


main_dataframe.to_csv("fitts.csv")
