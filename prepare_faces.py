# Copyright (C) 2023 - TechLife
#
# Wahl-O-Selfie (https://github.com/TachLaif/wahl-o-selfie-v2)
# - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 06.11.2023
#
# This work is made available under the [LICENSE NAME HERE]
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

import os
import pickle
import face_recognition
import time
def loadKnown() -> tuple[list, list, list]:
    start_time = time.time()
    if os.path.isfile('face_data/encodings.dat') and os.path.isfile('face_data/names.dat') and os.path.isfile('face_data/partys.dat'):
        with open('face_data/encodings.dat', 'rb') as f:
            known_face_encodings = pickle.load(f)
        with open('face_data/names.dat', 'rb') as f:
            known_face_names = pickle.load(f)
        with open('face_data/partys.dat', 'rb') as f:
            known_face_partys = pickle.load(f)
    else:
        known_face_encodings = []
        known_face_names = []
        known_face_partys = []

        face_folder = "./face_data/raw"
        folders = os.listdir(face_folder)
        for folder in folders:
            files_folder = face_folder + "/" + folder
            files = os.listdir(files_folder)
            for file in files:
                image_of_face = face_recognition.load_image_file(face_folder + "/" + folder + "/" + file)
                encoding_of_face = face_recognition.face_encodings(image_of_face, model = "large")[0]
                name = file.split(".", 1)
                known_face_encodings.append(encoding_of_face)
                known_face_names.append(name[0])
                known_face_partys.append(folder)
                print(folder + " - " + name[0])
        with open('face_data/encodings.dat', 'wb') as f:
            pickle.dump(known_face_encodings, f)
        with open('face_data/names.dat', 'wb') as f:
            pickle.dump(known_face_names, f)
        with open('face_data/partys.dat', 'wb') as f:
            pickle.dump(known_face_partys, f)
    print("--- %s seconds ---" % (time.time() - start_time))
    return known_face_encodings, known_face_names, known_face_partys