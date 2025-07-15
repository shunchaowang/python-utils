# Util to export gitlab projects as csv file
## prerequisite
- python 3+ should be available on the path, to verify run `python --version`
- under the project root create a `venv` by running `python -m venv .`
- activate the `venv` by running `.venv/bin/activate`
- install the required packages by running `pip install -r requirements.txt`
## create a personal access token on gitlab
- the token needs to have api access
- gather all the group ids to export
## export
to export the projects from multi group, separate the group ids by comma, the code will 
remove the duplicates
- run `python export_gitlab_projects.py`
- follow the prompt to input the comma separated project ids and gitlab pat
- the projects will be exported as a file `gitlab_projects.csv` under the project root
