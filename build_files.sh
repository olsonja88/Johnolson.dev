# build_files.sh
pip install -r requirements.txt
yes | python3.9 manage.py collectstatic
