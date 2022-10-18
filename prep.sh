#!/bin/bash
sleep 2
echo ""
cd ~/Desktop
mkdir amc_py
echo "Creating folder for AMC on Desktop"
sleep 1
echo ""
cd amc_py
echo "Starting to clone repository and prepping the files"
sleep 1
echo ""
sleep 1
git clone https://github.com/mirakklys/python_for_AMC.git
echo ""
sleep 1
echo "Downloading complete"
sleep 1
echo ""
cd python_for_AMC
rm -rf .git README.md Auto\ Multiple\ Choice\ Instructions.pdf prep.sh
echo "Removing unnecessary files"
sleep 1
echo ""
echo "Moving necessary files to amc-py folder"
mv * ..
cd ..
echo ""
rm -rf python_for_AMC
sleep 1
echo "Job done!"
sleep 2
exit
