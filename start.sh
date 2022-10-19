#!/bin/bash
echo -e '\033[1mHello, this is an interactive prep of AMC'
sleep 2
echo -e "Please name your Exam (without spaces): "
read -r exam_name
mkdir ~/Desktop/${exam_name}
echo -e "\033[1mCreating folder for $exam_name AMC on Desktop\033[0m"
sleep 1
printf %"$COLUMNS"s |tr " " "~"
echo -n -e '''\033[1mIs this the first time of using AMC on this machine? (y/n)\033[0m
*if "yes" we will update the system, install AMC program, prep python3 environment
Then we will download the python scripts to ~/Desktop/'''$exam_name''': '''
read -r answer_to_q1
printf %"$COLUMNS"s |tr " " "~"
atq1=`echo $answer_to_q1 | tr [:upper:] [:lower:] | cut -c 1`
sleep 1
if [[ $answer_to_q1 = "y" ]] || [[ $answer_to_q1 = "ye" ]] || [[ $answer_to_q1 = "yes" ]] || [[ -z $answer_to_q1 ]] ; then
    echo -e '\033[1mWe start the automatic setting up\033[0m'
    sudo apt update
    printf %"$COLUMNS"s |tr " " "~"
    sleep 1
    echo -e "\033[1mPrepping the system for installation of AMC\033[0m"
    sleep 1
    printf %"$COLUMNS"s |tr " " "~"
    echo -e "\033[1mUpgrade\033[0m"
    sleep 1
    printf %"$COLUMNS"s |tr " " "~"
    sudo apt full-upgrade -y
    printf %"$COLUMNS"s |tr " " "~"
    echo -e "\033[1mAMC installation\033[0m"
    printf %"$COLUMNS"s |tr " " "~"
    sleep 1
    sudo apt install auto-multiple-choice python-is-python3 -y
    printf %"$COLUMNS"s |tr " " "~"
    echo -e "\033[1mCleaning unnecessary residues\033[0m"
    sleep 1
    printf %"$COLUMNS"s |tr " " "~"
    sudo apt autoremove -y
    printf %"$COLUMNS"s |tr " " "~"
    
else 
    echo -e "\033[1mOkay, we are proceeding with the Exam prep shortly\033[0m"
    sleep 1
fi
printf %"$COLUMNS"s |tr " " "~"
cd ~/Desktop/${exam_name}
echo -e "\033[1mStarting to clone repository and prepping the files\033[0m"
sleep 1
printf %"$COLUMNS"s |tr " " "~"
git clone https://github.com/mirakklys/python_for_AMC.git
printf %"$COLUMNS"s |tr " " "~"
sleep 1
echo -e "\033[1mDownloading complete\033[0m"
sleep 1
cd ~/Desktop/${exam_name}/python_for_AMC/source
printf %"$COLUMNS"s |tr " " "~"
echo -e "\033[1mMoving necessary files to $exam_name folder\033[0m"
mv -t ~/Desktop/${exam_name} python_for_AMC.py Qs.txt wrongCorrect.png
cd ~/Desktop/${exam_name}
sleep 1
printf %"$COLUMNS"s |tr " " "~"
echo -e "\033[1mRemoving unnecessary files\033[0m"
rm -rf python_for_AMC
sleep 1
printf %"$COLUMNS"s |tr " " "~"
chmod +x python_for_AMC.py
sleep 1
echo -e "\033[1mJob done!\033[0m"
sleep 1
printf %"$COLUMNS"s |tr " " "~"
echo -e '\033[1mNow move Qs.txt file that you prepared to ~/Desktop/'$exam_name' folder\033[0m (replace the file on the prompt)'
sleep 2
echo -n -e '''Did you move \033[1mQs.txt\033[0m already? (y/n): '''
read -r wait_for_moving
printf %"$COLUMNS"s |tr " " "~"
w_f_m='echo $wait_for_moving | tr [:upper:] [:lower:] | cut -c 1'
sleep 1
count=0
if [[ $w_f_m != "yes" ]] || [[ $w_f_m != "yea" ]] || [[ $w_f_m != "y" ]] ; then
    while [ $count -le 1000 ] ;
        do
            read -p 'Did you move Qs.txt already? (y/n): ' w_f_m
            sleep 1
            if [[ "$w_f_m" = "y" ]] || [[ "$w_f_m" = "yes" ]] ; then
                echo -e "\033[1mGood, then we proceed to LaTeX source processing\033[0m"
                printf %"$COLUMNS"s |tr " " "~"
                sleep 1
s                break
            else 
                sleep 1
                echo -e "\033[1mPlease copy/move Qs.txt file to ~/Desktop/"$exam_name"\033[0m"
                printf %"$COLUMNS"s |tr " " "~"
            fi
    done
else
    pass
fi
sleep 1
cd ~/Desktop/${exam_name}/
~/Desktop/${exam_name}/python_for_AMC.py
mv prcssdQs.txt $exam_name.txt && rm python_for_AMC.py
printf %"$COLUMNS"s |tr " " "~"
sleep 2
echo -e "\033[1mAll files are processed and cleaned\033[0m"
sleep 1
echo -e "\033[1mYou LaTeX source file is called\033[0m "$exam_name".txt"
cd - > /dev/null