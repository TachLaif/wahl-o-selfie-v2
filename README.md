# Wahl-O-Selfie - v2
<a href="https://www.python.org/downloads/release/python-3120/"><img src="https://img.shields.io/badge/python-3.12.0-success?style=for-the-badge&logo=python&logoColor=white"></img></a>
<img src="https://img.shields.io/badge/Last%20update-13.11.2023-blue?style=for-the-badge"></img> 
<a href="https://github.com/TachLaif/wahl-o-selfie-v2/blob/main/LICENSE"><img src="https://img.shields.io/github/license/TachLaif/wahl-o-selfie-v2?style=for-the-badge"></img></a> 

## Description
Wahl-O-Selfie v2 is using facial recognition to categorize human faces into (german) political partys similar to "<a href="https://www.wahl-o-mat.de">Wahl-O-Mat</a>[^1]".


## Table of Contents
- <a href="#description">Description</a>
- <a href="#table-of-contents">Table of Contents</a>
- <a href="#how-to-install">How to install</a>
  - <a href="#installing-face_recognition-for-windows2">Installing face-recognition (for Windows)</a>
  - <a href="#installing-the-other-dependency">Installling the other dependency</a>
  - <a href="#installing-wahl-o-selfie">Installing Wahl-O-Selfie</a>
- <a href="#how-to-use">How to use</a>
- <a href="#how-it-works">How it works</a>
- <a href="#problems">Problems</a>
- <a href="#license-and-credits">License and credits</a>
- <a href="#postscript">Postscript</a> <!-- OPTIONAL -->

## How to install

Wahl-O-Selfie (v2) requires:
- <a href="https://www.python.org/downloads/release/python-3120/">Python 3.12.0</a>
- <a href="https://pypi.org/project/face-recognition/">face_recognition</a>
  - <a href="https://visualstudio.microsoft.com/de/">Microsoft Visual Studio 2015 (or newer)</a>
  - <a href="https://cmake.org/download/">CMake</a>
  - <a href="https://pypi.org/project/dlib/">dlib</a>
- <a href="https://pypi.org/project/Pillow/">pillow</a>
- os
- pickle

### Installing face_recognition (for Windows)[^2]
To install face_recognition you have to have <a href="https://www.python.org/downloads/release/python-3120/">Python 3.12.0</a> and <a href="https://visualstudio.microsoft.com/de/">Microsoft Visual Studio 2015 (or newer)</a> with C/C++ Compiler  installed. After that you have to install <a href="https://cmake.org/download/">CMake</a> for Windows and **add it to your system variables**. Then you have to install <a href="https://pypi.org/project/dlib/">dlib</a> using pip:

```bash
pip install dlib
```

and finally you can install the <a href="https://pypi.org/project/face-recognition/">face_recognition</a> library, also by using pip:

```bash
pip install face_recognition
```

### Installing the other dependency

Finally, you can install the other dependency with pip:

```bash
pip install Pillow
```

The libraries _os_, _pickle_ and _time_ are pre-installed with Python

### Installing Wahl-O-Selfie

Download the project as a _.zip file_ and unzip iton your machine. Then open **main.py** with a code editor, preferably with <a href="https://code.visualstudio.com/download">Microsoft Visual Stusio Code</a>, but make sure that you have the **Python extension** installed.

## How to use

After running the program a new file, called _result.jpg_ by default, apears in the program folder. In this picture you can see the face of a man surrounded by a rectangle with the predicted party below it, as seen here:

<img src="https://github.com/TachLaif/wahl-o-selfie-v2/assets/104715363/519280b9-2ab4-4e3d-8c73-2d5bc5c14fe1" width="384" height="384">

If you want to try the program on one of your pictures you have to copy it into the program directory and either rename it to _testimage.jpg_ (if your picture is a jpg file) or you have to change the first parameter in the last line in the _main.py_ file:

```python
predictParty('testimage.jpg', 'result.jpg', False)
```

The first parameter ('testimage.jpg') is the picture that will be loaded to be analyzed. The second parameter ('result.jpg') is the name of the picture that will be saved after the analyzation. The third parameter (which is currently set to False) determines if the program should print (cool looking) lines inbetween the face landmarks which are used to identify the faces. These lines look like this:

<img src="https://github.com/TachLaif/wahl-o-selfie-v2/assets/104715363/86f74da2-2ac4-4ae0-a162-3733adb924de" width="384" height="384">

cool, eh?

In the program directory I also included a second testimage you can try the program on. (Both of the testimages were created with <a href="https://thispersondoesnotexist.com">This Person does not exist</a>, just in case you wonder.)

You can also create your own dataset to be used to identify people. More instructions can be found in "face_data/raw/readme.txt".

## How it works

After running the 'predictParty' function the program procedes to run the 'loadKnown' function in 'prepare_faces.py'. The 'loadKnown' function then checks if the three required files 'face_data/encodings.dat', 'face_data/names.dat' and 'face_data/partys.dat' exist. If they exist the program loads the variables saved in these files, which contain the required informations needed by the program to identify and associated the correct names and partys to the faces it finds in the picture. If the program does not find the required files it will try to generte them based on the directory structure in 'face_data/raw/'. Currently, however, this would not work, as there is no compatible folder structure present by default.

```python
    picture = face_recognition.load_image_file(inputImage)
    face_locations = face_recognition.face_locations(picture)
    face_encodings = face_recognition.face_encodings(picture, face_locations, model = 'large')
```

In these lines the program loads the image it has to process and identifies the locations of the faces present in the picture and their corresponding encoding, which are stored in the variables 'face_locations' and 'face_encodings'. 'face_locations' is relatively self explanatory, 'face_encodings' is a list containing the data needed (and provided) by the library I use for the facial recognition stuff. Basicaly the library converts the facial points in the picture of each face into some number values which it then can use to check how similar two faces are. In the 'face_data/encodings.dat' file are the encodings of the politicians used in the model. Please note the extra parameter 'model = 'large'' which tells the library that it should used more points per face which makes the overall recognition part more accurate.

```python
pil_image = Image.fromarray(picture)
```

With this line the program converts the previously opened picture to a format with which I can edit using pillow. This will be used to draw the rectangle and the optional face landmarks on the picture.

Speaking of face landmarks, this code executes if the optional 'showFaceLandmarks' parameter in the function is set to _True_:

```python
if showFaceLandmarks:
        face_landmarks_list = face_recognition.face_landmarks(picture, face_locations, 'large')
        for face_landmarks in face_landmarks_list:
            draw = ImageDraw.Draw(pil_image)
            for facial_feature in face_landmarks.keys():
                draw.line(face_landmarks[facial_feature], width=2, fill = (255, 0, 0))
            del draw
```

This code is responsible for drawing these cool looking red lines connecting the points used by the library to determine how a face looks.

The following for-loop goes through each face located in the image and analyzes the current face. 

```python
matches = face_recognition.compare_faces(known_face_encodings, face_encodings, tolerance = 0.5)
similar = face_recognition.face_distance(known_face_encodings, face_encodings)
```

The first line determines if the currently processed face is of one of the party members in which case the program will show the name and the party the face belongs to. This is happening in the following lines 

```python
if True in matches:
            first_match_index = matches.index(True)
            information = known_face_names[first_match_index] + ' - ' + known_face_partys[first_match_index]
```

The second line, however, determines how similar the face is to the faces in the model. 

```python
list = similar.tolist()
lowest_match_index = list.index(min(list))
information = known_face_partys[lowest_match_index]
```

With this code it converts the similarity values to a list and finds the element with the lowest similarity value, as this is the one that looks the most like the face that is currently processed in the for-loop. 

```python
draw = ImageDraw.Draw(pil_image)
draw.rectangle(((left, top), (right, bottom)), outline = (0, 255, 255), width = 5)
draw.rectangle(((left, bottom), (right, bottom + 21)), fill = (0, 0, 0), outline = (0, 0, 0), width = 5)
draw.text((left + 6, bottom + 6), information, fill = (255, 255, 255))
del draw
```

Finally, it draws the box around the face and a rectangle below it in which it writes the name and/or the party the face corresponds to. And saves the image to the designated location and file name.

```python
pil_image.save(outputImage)
```

## Problems 

The program does not generate an average between the party members, instead it uses the party of the member who looks most like the person in the picture.

## License and credits

This work is made available under the **<a href="https://github.com/TachLaif/wahl-o-selfie-v2/blob/main/LICENSE">GNU Affero General Public License v3.0</a>**.

Project made by **<a href="https://github.com/TachLaif">TechLife</a>**.
<br><br><a href="https://discord.com"><img src="https://img.shields.io/badge/TechLife-@techlife-informational?style=for-the-badge&logo=discord&logoColor=white"></a><br><a href="https://twitter.com/_Tech4Life_"><img src="https://img.shields.io/badge/Twitter-@__Tech4Life__-informational?style=for-the-badge&logo=twitter&logoColor=white"></a><br><a href="https://www.buymeacoffee.com/TechLife"><img src="https://img.shields.io/badge/Buy%20me%20a-coffee-red?style=for-the-badge&logo=buymeacoffee&logoColor=white" title="I like coffee!"></a>

## Postscript
A similar project like this was build using the self-reported political orientation of over a million participants from Facebook and dating website acconts from three countries (the U.S, the UK and Canada). This facial recognition model achived an accuracy of around 72%. If you want to read the article yourself you can find it <a href="https://rdcu.be/cYEvm">HERE</a>

[^1]: The <a href="https://www.wahl-o-mat.de">Wahl-O-Mat</a> is a website by the german <a href="www.bpb.de">bpb</a> with questions you can fill outand afterwards you can see wich political partys have similar interests. This is supposed to help people make up their mind about who they should vote for.
[^2]: https://github.com/ageitgey/face_recognition/issues/175#issue-257710508
