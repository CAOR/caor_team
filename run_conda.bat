REM call activate py27
pip install Jinja2
pip install unidecode
REM pip install unidecode
REM pip install urllib
python page_team.py FR > page_fr.txt
python page_team.py EN > page_en.txt
REM call deactivate
PAUSE