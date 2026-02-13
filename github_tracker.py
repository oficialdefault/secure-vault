import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def test_github_connection():
    print("--- 📡 Testing GitHub Connection ---")
    
    # We use the 'user' endpoint to verify the token is valid
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

def get_repo_issues(repo_owner, repo_name):
    # The API endpoint for GitHub issues
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    
    # Headers to identify ourselves to GitHub
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json() # This is the JSON data!
    else:
        print(f"Failed to fetch: {response.status_code}")
        return None

if __name__ == "__main__":
    # Let's track a famous Python library, like 'requests' itself!
    owner = "psf"
    repo = "requests"
    
    issues = get_repo_issues(owner, repo)
    
    if issues:
        print(f"--- Latest Issues for {owner}/{repo} ---")
        for issue in issues[:5]: # Just show the first 5
            print(f"ID: {issue['id']} | Title: {issue['title']}")