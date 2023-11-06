In this folder you can prepare your own facial recognition models to use with Wahl-O-Selfie v2.
To do this you should use the following structure:

face_data/
	raw/
		partyName0/
			politicianName0.jpg
			politicianName1.png
		partyName2/
			politicianName3.jpg

e.g.
face_data/
	raw/
		Freedom Party/
			John Doe.jpg
			Jane Doe.png
		True Democrats/
			Max Mustermann.jpg

Make sure to follow this structure, so that the program can identify and correctly prepare the required files needed for the program to work.
After you have prepared your own model all you have to do is remove/rename the files I included in the program download, remove thie readme file and run the program.