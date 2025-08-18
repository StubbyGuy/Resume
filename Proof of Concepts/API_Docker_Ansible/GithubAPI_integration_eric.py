#Eric Somogyi#

import requests

#### variables defined
github_api_url = "https://api.github.com"
auth_token = ""
headers = {"Authorization": f"token {auth_token}", "Accept": "application/vnd.github.v3+json"}
repository = "StubbyGuy/DePaul-Cybersecurity-Automation-Test"  #added variable for repo in format username/repo


def list_repos(username):
    """Fetch repositories for a specific user"""
    username = "StubbyGuy"
    url = f"{github_api_url}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code == 200: #GET request
        repos = response.json()   
        for repo in repos:                         
            print(f"Repo: {repo['name']}")
            print(f"Description: {repo['description']}")
    else:
        print(f"{response.status_code}")


def create_issue(repo, title, body):
    """Create GitHub Issue for specific repo"""
    url = f"{github_api_url}/repos/{repo}/issues"
    data = {    
        "title": title,  #if you change title, to just a "" you will get the successful error code response.
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201: #POST request
        issue_content = response.json()
        print(f"Issue created: {issue_content['html_url']}")
    else:
        print(f"Issue creation error: {response.status_code} - {response.json()}")


def add_comment(repo, issue_number, comment):
    """Add a comment to an existing issue."""
    url = f"{github_api_url}/repos/{repo}/issues/{issue_number}/comments"
    data = {
        "body": comment
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201: #POST request
        comment_content = response.json()
        print(f"Comment added: {comment_content['html_url']}")   
    else:
        print(f"Comment creation error: {response.status_code} - {response.json()}")


list_repos("username")
print()
create_issue(repository, "issue name", "issue description") 
print()
add_comment(repository, 11, "This is an issue comment")
