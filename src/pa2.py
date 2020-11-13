import requests
import json
from datetime import date

def format_json(data):
    return json.dumps(data, sort_keys=True, indent=2)


class Repo:
    def __init__(self, user, repo):
        response = requests.get("https://api.github.com/repos/{}/{}".format(user, repo))
        repo_data = response.json()

        # print(self.format_json(repo_data))
                
        self.name = repo_data["name"]
        self.owner = repo_data["owner"]["login"]
        self.description = repo_data["description"]
        self.homepage = repo_data["homepage"]
        self.repo_license = repo_data["license"]["name"] # TODO: class?
        self.num_forks = repo_data["forks_count"]
        self.watchers = repo_data["watchers"]
        self.date_of_collection = date.today()
        self.num_stars = repo_data["stargazers_count"]
               

        # get pull request data from first page (1)
        response = requests.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
        pull_request_data = response.json()

        # print("\nPR\n\n", self.format_json(pull_request_data))

        self.pull_requests_url = repo_data["pulls_url"]

        # TODO: make nested class for pull requests and have a list of pull_requests classes here.
        # TODO: loop through each pr and pass json to class
        # print("\nFOR\n\n")

        self.pull_requests = []
        
        for pull_request in pull_request_data:
            self.pull_requests.append(PullRequest(pull_request, user, repo))
            break               # TODO remove 
        # # Test igors TODO
        # response = requests.get("https://api.github.com/search/issues?q=is:pr+repo:{}/{}".format(user, repo, 1))
        # pull_request_data = response.json()

        # print("\n\nIGOR\n\n", self.format_json(pull_request_data))


        print()
        print(self.name)
        print(self.owner)
        print(self.description)
        print(self.homepage)
        print(self.num_forks)
        print(self.watchers)
        print(self.date_of_collection)
        print(self.num_stars)
        print(self.pull_requests_url)


    def __str__(self):
        return "{}/{}: {} ({})".format(self.owner, self.name, self.description, self.num_stars)


class PullRequest:
    def __init__(self, pull_request, user, repo):
        self.title = pull_request["title"]
        self.number = pull_request["number"]
        self.body = pull_request["body"]
        self.state = pull_request["state"]
        self.date_of_creation = pull_request["created_at"]
        self.user = pull_request["user"]["login"]
        self.closing_date = None # TODO: it's a print safety, remove?
        
        if (self.state != "open"):
            self.closing_date = pull_request["closed_at"]

        # get additional data by querying pull request number
        response = requests.get("https://api.github.com/repos/{}/{}/pulls/{}".format(user, repo, self.number))
        pull_request_data = response.json()

        # print("\n\nADD PR DATA\n\n", format_json(pull_request_data))       
            
        self.num_commits = pull_request_data["commits"]
        self.additions = pull_request_data["additions"]
        self.deletions = pull_request_data["deletions"]
        self.changed_files = pull_request_data["changed_files"]

        # TODO: print all
        print("\n\nPR vars\n\n")
        print(self.title)
        print(self.number)
        print(self.body)
        print(self.state)
        print(self.date_of_creation)
        print(self.user)               
        if (self.closing_date != None):
            print(self.closing_date)
        print(self.num_commits)
        print(self.additions)
        print(self.deletions)
        print(self.changed_files)
        # END print all

# # user data
# response = requests.get("https://api.github.com/users/JabRef")
# user_data = format_json(response.json())

# print("\nUSER:\n\n", user_data)

# # repo data (also has user (owner) data)
# response = requests.get("https://api.github.com/repos/JabRef/jabref")
# repo_data = format_json(response.json())

# print("\nREPO:\n\n", repo_data)

repo = Repo("JabRef", "jabref")
