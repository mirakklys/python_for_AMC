#!/bin/bash
echo '''
'''
sleep 2
echo "Prepping the system for installation of AMC"
sleep 2
echo '''
'''
echo "Upgrade"
sleep 2
echo '''
'''
sudo apt full-upgrade -y
echo '''
'''
echo "AMC installation"
echo '''
'''
sleep 2
sudo apt install auto-multiple-choice python-is-python3 -y
echo '''
'''
echo "Cleaning unnecessary residues"
sleep 2
echo '''
'''
sudo apt autoremove -y
mkdir ~/Desktop/${exam_name}
echo '''
'''
echo "Creating folder for AMC on Desktop"
sleep 2
echo '''
'''
cd ~/Desktop/${exam_name}
echo "Starting to clone repository and prepping the files"
sleep 2
echo '''
'''
git clone https://github.com/mirakklys/python_for_AMC.git
echo '''
'''
sleep 2
echo "Downloading complete"
sleep 2
cd ~/Desktop/${exam_name}/python_for_AMC/source
echo "Moving necessary files to $exam_name folder"
mv -t ~/Desktop/${exam_name} python_for_AMC.py open_Qs_for_AMC.py Qs.txt wrongCorrect.png
cd ~/Desktop/${exam_name}
echo '''
'''
echo "Removing unnecessary files"
rm -rf python_for_AMC
sleep 2
echo '''
'''
chmod +x python_for_AMC.py open_Qs_for_AMC.py
sleep 2
echo "Job done!"
sleep 2
exit
