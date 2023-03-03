from pointing_utils import segment, package

import numpy
import pathlib
import os

original_dataset_directory = pathlib.Path(__file__).resolve().parents[0]


_folders = os.listdir(str((original_dataset_directory / "original_data").resolve()))

main_container = {}
for _folder in _folders:
    _files = os.listdir(
        str((original_dataset_directory / "original_data" / _folder).resolve())
    )
    print(_folder)
    participant = _folder[1:]
    participant_container = {}
    for nfile, _file in enumerate(_files):
        _words = _file.split(",")
        w_trial = float(_words[3][:-4]) / 3.608
        d_trial = float(_words[2]) / 3.608

        with open(
            str(
                (
                    original_dataset_directory / "original_data" / _folder / _file
                ).resolve()
            ),
            "r",
        ) as tmp_f:
            for n, line in enumerate(tmp_f):
                _words = line.split(",")

                if n == 0:
                    timestamps = []
                    _width = []
                    _dist = []
                    _pos = []
                    _spd = []
                    _acc = []
                else:
                    timestamps.append(float(_words[24]))
                    _width.append(float(_words[29]))
                    _dist.append(float(_words[30]))
                    _pos.append(float(_words[27]))

        timestamps = numpy.array(timestamps)
        _pos = numpy.array(_pos)

        ## Cut first and last movement

        data_dict = {"x": _pos, "t": timestamps}
        movements, negmovs = segment(
            data_dict, reciprocal=True, resampling_period=0.01, trim=[1, -1]
        )
        container = package(movements, negmovs, reciprocal=True, json_serializable=True)
        container.update({"W": w_trial, "D": d_trial})
        participant_container[_file] = container
    main_container[str(participant)] = participant_container

import json

with open("segmented_data.json", "w") as _file:
    json.dump(main_container, _file)
