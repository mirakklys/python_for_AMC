#!/bin/bash
# Echo -e is to show a special formating of the following string
weAreHere=$(pwd)
echo -e '\033[1mHello, this is an interactive prep of AMC'

# Sleep :)
sleep 2
echo -e "Please name your Exam (without spaces): \033[0m"

# Read -r to wait for a response and write it to exam_name variable
read -r exam_name

# Use the variable for naming a folder for this specific exam 
mkdir ~/MC-Projects/${exam_name}
echo -e "\033[1mCreating folder for \033[45m$exam_name\033[0m \033[1mAMC in \033[45m~/MC-Projects\033[0m"
sleep 1

# Decorations, fshuuuh... $COLUMNS is to show the width of terminal and feed it to printf | tr to swap spaces with tilda
printf %"$COLUMNS"s |tr " " "~"
sleep 1

# If block to install AMC
if [[ $(dpkg --get-selections | grep auto-multiple-choice -c) -eq 0 ]] ; then # || [[ $answer_to_q1 = "ye" ]] || [[ $answer_to_q1 = "yes" ]] || [[ -z $answer_to_q1 ]] ; then
    echo -e '\033[1mWe start the automatic setting up\033[0m'
    printf %"$COLUMNS"s |tr " " "~"
    sleep 1
    echo -e "\033[1mPrepping the system for installation of AMC\033[0m"
    sudo apt update
    printf %"$COLUMNS"s |tr " " "~"
    sleep 1
    echo -e "\033[1mUpgrade\033[0m"
    printf %"$COLUMNS"s |tr " " "~"
    echo ""
    sleep 1
    sudo apt full-upgrade -y
    printf %"$COLUMNS"s |tr " " "~"
    echo -e "\033[1mAMC installation\033[0m"
    printf %"$COLUMNS"s |tr " " "~"
    echo ""
    sleep 1
    sudo apt install auto-multiple-choice python-is-python3 zenity -y
    printf %"$COLUMNS"s |tr " " "~"
    echo -e "\033[1mCleaning unnecessary residues\033[0m"
    printf %"$COLUMNS"s |tr " " "~"
    echo ""
    sleep 1
    sudo apt autoremove -y
else 
    echo -e "\033[1mOkay, we are proceeding with the Exam prep shortly\033[0m"
    sleep 1
fi
printf %"$COLUMNS"s |tr " " "~"
cd ~/MC-Projects/${exam_name}
echo -e "\033[1mStarting to clone repository and prepping the files\033[0m"
sleep 1
printf %"$COLUMNS"s |tr " " "~"

# Fetching files needed to run the script and prep the LaTeX file: python_for_AMC.py and the wrongCorrect.png
git clone https://github.com/mirakklys/python_for_AMC.git
printf %"$COLUMNS"s |tr " " "~"
sleep 1
echo -e "\033[1mDownloading complete\033[0m"
sleep 1
cd ~/MC-Projects/${exam_name}/python_for_AMC/source
printf %"$COLUMNS"s |tr " " "~"
echo -e "\033[1mMoving necessary files to \033[45m~/MC-Projects/$exam_name\033[0m \033[1mfolder\033[0m"

# Moving the needed files and deleting all unnecessary stuff
mv -t ~/MC-Projects/${exam_name} python_for_AMC.py Qs.txt wrongCorrect.png
mv -t ~/MC-Projects/${exam_name} ~/MC-Projects/${exam_name}/python_for_AMC/source/Empty/*
cd ~/MC-Projects/${exam_name}
printf %"$COLUMNS"s |tr " " "~"
sleep 1
echo -e "\033[1mRemoving unnecessary files\033[0m"
rm -rf python_for_AMC
printf %"$COLUMNS"s |tr " " "~"
sleep 1

# Script is executable :)
chmod +x python_for_AMC.py
sleep 1
echo -e "\033[1mJob done!\033[0m"
sleep 1
printf %"$COLUMNS"s |tr " " "~"
echo -n -e '\033[1mNow choose the file with the questions. \033[45m(No need to name it Qs.txt, but it has to be *.txt)\033[0m\n'

# Choose the file with questions
w_f_m=$(zenity --file-selection)
sleep 1

# Copy the question into Qs.txt in the folder of the exam 
cp $w_f_m ~/MC-Projects/${exam_name}/Qs.txt
sleep 1

# Run the script in the exam folder, so that all the files are in the same place
cd ~/MC-Projects/${exam_name}
~/MC-Projects/${exam_name}/python_for_AMC.py

# Rename the output file ready for compiling LaTeX pdf
mv prcssdQs.txt $exam_name.txt && rm python_for_AMC.py && cp $exam_name.txt source.tex
printf %"$COLUMNS"s |tr " " "~"
sleep 2
echo -e "\033[1mAll files are processed and cleaned\033[0m"
sleep 1
echo -e "\033[1mYou LaTeX source file is called \033[45m"$exam_name".txt\033[0m"

# And goodbye:)
cd $weAreHere
sleep 1
echo -e "\033[1mNow press any key to quit\033[0m"
until read -s -n 1 -t 0.01; do 
    echo -n "~"
    sleep .5
done 

# for i in {1..125} ; do echo -e "You LaTeX source file is called \033[${i}mexam_name.txt\033[0m $i" ; done
