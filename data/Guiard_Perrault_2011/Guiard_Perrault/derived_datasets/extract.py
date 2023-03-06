from pointing_utils import segment, package


import os
import pathlib
import numpy
import matplotlib.pyplot as plt

original_dataset_directory = pathlib.Path(__file__).resolve().parents[1]

FOLDER = "original_dataset"
# FOLDER = "recursion_error"


_files = os.listdir(str((original_dataset_directory / FOLDER).resolve()))


participants = set()
participant_container = {}
for _file in _files:
    file_path = str((original_dataset_directory / FOLDER / _file).resolve())
    header = True
    t = []
    x = []
    participant = _file.split("_")[0][1:]
    if participant not in participants:
        participants.add(participant)
        participant_container[participant] = {}

    with open(file_path, "r") as _file:
        print(file_path)
        for n, line in enumerate(_file):
            if "Instruction" in line:
                speed_accuracy_instruction = line.split(";")[1].split(".")[0]
                continue
            if "Block" in line:
                block_number = line.split(";")[1].strip("\n")
                continue
            if "Time (in s)" in line:
                header = False
                continue
            if not header:
                try:
                    words = line.split(";")
                    if len(words) != 20:
                        print(file_path)
                        exit()
                    t.append(float(words[0]))
                    x.append(float(words[19]))
                except IndexError:
                    print(file_path)
                    print(words)
                    exit()

    data_dict = {"x": numpy.array(x), "t": numpy.array(t)}
    movements = segment(
        data_dict,
        reciprocal=False,
        start_params={"thresh": 5e-2},
        # stop_params={"thresh": (6 - float(speed_accuracy_instruction)) * 0.01},
        stop_params={"thresh": 1e-2},
    )
    container = package(movements, reciprocal=False, json_serializable=True)
    container.update(
        {"Instruction": speed_accuracy_instruction, "Block number": block_number}
    )
    participant_container[participant][
        speed_accuracy_instruction + "_" + block_number
    ] = container


import json

with open("segmented_data.json", "w") as _file:
    json.dump(participant_container, _file)
