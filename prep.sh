#!/bin/bash
cd ~/Desktop
mkdir amc_py
cd amc_py
git clone https://github.com/mirakklys/python_for_AMC.git
rm -rf .git READMR.md Auto Multiple Choice Instructions.pdf prep.sh
mv * ..
cd ..
rm -rf python_for_AMC
exit
