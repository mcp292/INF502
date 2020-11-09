import requests
import json

class Repo:
    def __init__(self, user, repo):
        response = requests.get("https://api.github.com/repos/{}/{}".format(user, repo))
        repo_data = response.json()

        print(self.format_json(repo_data))
                
        self.name = repo_data["name"]
        self.owner = repo_data["owner"]["login"]
        self.description = repo_data["description"]
        self.homepage = repo_data["homepage"]
        self.repo_license = repo_data["license"]["name"] # TODO: class?
        self.num_forks = repo_data["forks_count"]
        self.watchers = repo_data["watchers"]
        # TODO        self.date_of_collection = repo_data["date_of_collection"]
        #        self.num_stars = repo_data[" TODO num_stars


        # get pull request data from first page (1)
        response = requests.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
        pull_request_data = response.json()

        print("\nPR\n\n", self.format_json(pull_request_data))

        self.pull_requests_url = repo_data["pulls_url"]

        # TODO: make nested class for pull requests and have a list of pull_requests classes here.
        
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
#        print(self.date_of_collection)
        # TODO: date_of_creation
        # TODO        print(self.num_stars)
        print(self.pull_requests_url)



    def format_json(self, data):
        return json.dumps(data, sort_keys=True, indent=2)


    def __str__(self):
        return "{}/{}: {} ({})".format(self.owner, self.name, self.description, self.num_stars)


# # user data
# response = requests.get("https://api.github.com/users/JabRef")
# user_data = format_json(response.json())

# print("\nUSER:\n\n", user_data)

# # repo data (also has user (owner) data)
# response = requests.get("https://api.github.com/repos/JabRef/jabref")
# repo_data = format_json(response.json())

# print("\nREPO:\n\n", repo_data)

repo = Repo("JabRef", "jabref")
