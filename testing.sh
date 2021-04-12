#! /bin/bash 
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest
pip3 install pytest-cov

python3 -m pytest service1 --cov
python3 -m pytest service2 --cov
python3 -m pytest service3 --cov
python3 -m pytest service4 --cov