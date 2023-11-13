# Copyright (C) 2023 - TechLife
#
# Wahl-O-Selfie (https://github.com/TachLaif/wahl-o-selfie-v2)
# - Made with ♥ by TechLife (https://github.com/TachLaif)
# Last update: 06.11.2023
#
# This work is made available under the [LICENSE NAME HERE]
# More informations about the license can be found at:
# https://www.gnu.org/licenses/agpl-3.0

import face_recognition
from PIL import Image, ImageDraw
from prepare_faces import loadKnown


def predictParty(inputImage:str, outputImage:str = 'result.jpg', showFaceLandmarks:bool = False):
    known_face_encodings, known_face_names, known_face_partys = loadKnown()

    picture = face_recognition.load_image_file(inputImage)
    face_locations = face_recognition.face_locations(picture)
    face_encodings = face_recognition.face_encodings(picture, face_locations, model = 'large')
    
    pil_image = Image.fromarray(picture)

    if showFaceLandmarks:
        face_landmarks_list = face_recognition.face_landmarks(picture, face_locations, 'large')
        for face_landmarks in face_landmarks_list:
            draw = ImageDraw.Draw(pil_image)
            for facial_feature in face_landmarks.keys():
                draw.line(face_landmarks[facial_feature], width=2, fill = (255, 0, 0))
            del draw

    for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings, tolerance = 0.5)
        similar = face_recognition.face_distance(known_face_encodings, face_encodings)

        if True in matches:
            first_match_index = matches.index(True)
            information = known_face_names[first_match_index] + ' - ' + known_face_partys[first_match_index]
        else:
            list = similar.tolist()
            lowest_match_index = list.index(min(list))
            information = known_face_partys[lowest_match_index]
        draw = ImageDraw.Draw(pil_image)
        draw.rectangle(((left, top), (right, bottom)), outline = (0, 255, 255), width = 5)
        draw.rectangle(((left, bottom), (right, bottom + 21)), fill = (0, 0, 0), outline = (0, 0, 0), width = 5)
        draw.text((left + 6, bottom + 6), information, fill = (255, 255, 255))
        del draw
    pil_image.save(outputImage)

if __name__ == '__main__':
    predictParty('testimage.jpg', 'result.jpg', False)