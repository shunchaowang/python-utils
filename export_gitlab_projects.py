import csv

import gitlab
from gitlab.exceptions import GitlabAuthenticationError, GitlabGetError

GITLAB_URL = "https://gitlab.com"
CSV_FILE = "gitlab_projects.csv"

group_input = input("Enter the Gitlab Group IDs separated by a comma: ")
gitlab_pat = input("Enter the Gitlab Personal Access Token: ")

group_ids = set(group_input.split(","))
with open(CSV_FILE, mode="w", newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerow(['Group', 'Name', 'Web URL'])
  try:
    gl = gitlab.Gitlab(GITLAB_URL, private_token=gitlab_pat)
    for group_id in group_ids:
      group = gl.groups.get(group_id)
      projects = group.projects.list(all=True, include_subgroups=True, archived=False)
      for project in projects:
        print(f"Exporting {project.name} in {group.name}")
        writer.writerow([group.name, project.name, project.web_url])

      print(f"✅ Exported {len(projects)} projects to '{CSV_FILE}'")

  except GitlabAuthenticationError as e:
    print("❌ Authentication failed: Please check your private token or GitLab URL.")
  except GitlabGetError as e:
    print(f"❌ Failed to retrieve group ': {e}")
  except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
