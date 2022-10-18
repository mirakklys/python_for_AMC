#!/bin/bash
echo -e '\033[1mHello, this is an interactive prep of AMC\033[0m'
# sleep 2
echo -n -e '''\033[1mIs this a first time of using AMC on this machine? (y/n)\033[0m
*if "yes" we will update the system, install AMC program, 
prep python3 environment and download the python scripts to ~/Desktop/amc_py: \033[1m'''
read -r answer_to_q1
echo -e '\033[0m'

# sleep 1
if [[ $answer_to_q1 = "y" ]] || [[ $answer_to_q1 = "ye" ]] || [[ $answer_to_q1 = "yes" ]] || [[ $answer_to_q1 = "Y" ]] || [[ $answer_to_q1 = "YE" ]] || [[ $answer_to_q1 = "YES" ]]; then
    echo -e '\033[1mWe start the automatic setting up\033[0m'
    ./source/prep.sh
    echo -e '\033[1mNow move Qs.txt file that you prepared to ~/Desktop/amc_py folder\033[0m'
    echo -n -e '''Did you move \033[1mQs.txt\033[0m already? (y/n): \033[1m'''
    read -r wait_for_moving
else 
    echo -e "\033[1mOkay, we are proceeding with the Exam prep shortly"
    # sleep 1
fi
    echo -e "\033[0m"

# sleep 1
if [[ answer_to_q2 = "N" ]] || [[ answer_to_q2 = "n" ]] || [[ answer_to_q2 = "no" ]] || [[ answer_to_q2 = "NO" ]] ; then
    echo -e "\033[1mPlease copy/move Qs.txt file to ~/Desktop/amc_py\033[0m"
else 
    ~/Desktop/amc_py/python_for_AMC.py
fi
