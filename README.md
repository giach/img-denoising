-> generateNoiseImages takes the input and applies s&p noise and gaussian noise
 and then writes back the files into specific folders for each batch
-> the resulting files are not compliant with the format required by cv2.nlm function so for each
 gauss folder run in Linux( Windows/bash) .FixImages.sh script
-> gc will open the generated noisy images and then apply the algorithms
-> resulting files will be written in folders specific to each algorithm used

pip install -U scikit-image - prerequisites windows-compile-stuff
pip install numpy
pip install opencv
Opencv algorithms work tlv1 and npc. Scikit output black images. Maybe the file should be working differently 