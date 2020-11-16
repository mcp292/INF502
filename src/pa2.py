import requests
import json
import csv
import os
from datetime import date
from bs4 import BeautifulSoup as bs

def format_json(data):
    return json.dumps(data, sort_keys=True, indent=2)


class Repo:
    def __init__(self, user, repo):
        username = 'mcp292'
        token = ''
        
        sesh = requests.Session()
        sesh.auth = (username, token)

        response = sesh.get("https://api.github.com/repos/{}/{}".format(user, repo))
        #        response = requests.get("https://api.github.com/repos/{}/{}".format(user, repo))
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
        response = sesh.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
        #response = requests.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
        pull_request_data = response.json()

        # extract pull requests
        self.pull_requests = []
        
        for pull_request in pull_request_data:
            self.pull_requests.append(PullRequest(pull_request, user, repo))

        # for each extracted pull request store author
        self.authors = []
        existing_author = None  # default
        
        for pull_request in self.pull_requests:
            # check if author already added
            for author in self.authors:
                if (pull_request.user == author.user):
                    existing_author = author

            # if author exists increment num pull requests
            if (existing_author != None):
                existing_author.inc_num_pull_requests()
            else:
                # add to list
                self.authors.append(Author(pull_request.user))

            # reset to default
            existing_author = None
        
        # write to csv
        self.write_to_csv(user, repo, self.pull_requests, self.authors)
        
        print()
        print(self.name)
        print(self.owner)
        print(self.description)
        print(self.homepage)
        print(self.num_forks)
        print(self.watchers)
        print(self.date_of_collection)
        print(self.num_stars)
        print([str(item) for item in self.pull_requests])
        print([str(item) for item in self.authors])
        

    def __str__(self):
        return "{}/{}: {} ({})".format(self.owner, self.name, self.description, self.num_stars)


    def to_CSV(self, filename):
        file_exist = os.path.exists(filename)

        header = vars(self).copy() # was deleting from original class

        del header["pull_requests"]
        del header["authors"]

        with open(filename, mode='a', newline='') as CSVfile:
            file_writer = csv.writer(CSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            if(not file_exist):
                file_writer.writerow(header)

            file_writer.writerow(header.values())

            
    def write_to_csv(self, user, repo, pull_requests, authors):
        # create file names
        repo_fn="repos.csv"
        pull_req_fn = "{}-{}.csv".format(user, repo)
        author_fn="user.csv"

        # write repo data
        self.to_CSV(repo_fn)

        # write pr data
        for req in pull_requests:
            req.to_CSV(pull_req_fn)

        # write author data
        for author in authors:
            author.to_CSV(author_fn)
        

class PullRequest:
    def __init__(self, pull_request, user, repo):
        username = 'mcp292'
        token = ''
        
        sesh = requests.Session()
        sesh.auth = (username, token)

        self.title = pull_request["title"]
        self.number = pull_request["number"]
        self.body = pull_request["body"]
        self.state = pull_request["state"]
        self.date_of_creation = pull_request["created_at"]
        self.user = pull_request["user"]["login"]
        self.closing_date = None
        
        if (self.state != "open"):
            self.closing_date = pull_request["closed_at"]

        # get additional data by querying pull request number
        response = sesh.get("https://api.github.com/repos/{}/{}/pulls/{}".format(user, repo, self.number))
        #response = requests.get("https://api.github.com/repos/{}/{}/pulls/{}".format(user, repo, self.number))
        pull_request_data = response.json()

        # print("\n\nADD PR DATA\n\n", format_json(pull_request_data))       
            
        self.num_commits = pull_request_data["commits"]
        self.additions = pull_request_data["additions"]
        self.deletions = pull_request_data["deletions"]
        self.changed_files = pull_request_data["changed_files"]

        # write to csv
        # filename = "{}-{}.csv".format(user, repo)
        # self.to_CSV(filename)

        
        # TODO: print all
        print("\n\nPR vars\n\n")
        print(self.title)
        print(self.number)
        # print(self.body)
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

        
        
    def __str__(self):
        return "{} ({})".format(self.title, self.state)


    def to_CSV(self, filename):
        path= os.getcwd() + "/repos"

        # if dir doesn't exist
        if (not os.path.exists(path)):
            try:
                os.mkdir(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)

        # cd into dir
        os.chdir(path)

        file_exist = os.path.exists(filename)
        
        with open(filename, mode='a', newline='') as CSVfile:
            file_writer = csv.writer(CSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            if (not file_exist):
                file_writer.writerow(vars(self))

            file_writer.writerow(vars(self).values())
            

class Author:
    def __init__(self, user):
        self.user = user
        self.num_pull_requests = 1
        # set defaults for pages that might not have this data
        self.num_followers = 0
        self.num_following = 0
        
        
        # scrape user info from page
        response = requests.get("https://github.com/{}".format(user))        
        soup = bs(response.content, "html.parser")

        # if user found
        if (response.status_code == 200):
            # get num followers
            num_followers = soup.find("a", attrs={"href": "/{}?tab=followers".format(user)}) # inside this block
            if (num_followers != None):
                num_followers = num_followers.find("span", attrs={"class": "text-bold text-gray-dark"}) # find it! scrape it!
                self.num_followers = int(num_followers.text)

            # get num following
            num_following = soup.find("a", attrs={"href": "/{}?tab=following".format(user)}) # inside this block
            if (num_following != None):
                num_following = num_following.find("span", attrs={"class": "text-bold text-gray-dark"}) # find it! scrape it!
                self.num_following = int(num_following.text)

            # get num repos
            num_repos = soup.find("a", attrs={"href": "/{}?tab=repositories".format(user)}) # inside this block
            num_repos = num_repos.find("span", attrs={"class": "Counter"}) # find it! scrape it!
            self.num_repos = int(num_repos.text) + 1 # it's a counter so it starts at zero (add 1)

            # get number contributions in last year 
            num_contributions = soup.find("div", attrs={"class": "js-yearly-contributions"}) # inside this block
            num_contributions = num_contributions.find("h2") # find it! scrape it!
            self.num_contributions = int("".join(filter(str.isdigit, num_contributions.text))) # get number from str
        else:
            print("\n\n")
            print(user, "not found");
            print("\n\n")
            
        
    def inc_num_pull_requests(self):
        self.num_pull_requests = self.num_pull_requests + 1


    def __str__(self):
        return "{}: {}".format(self.user, self.num_pull_requests)
            

# Check limit
username = 'mcp292'
token = ''

sesh = requests.Session()
sesh.auth = (username, token)

response = sesh.get("https://api.github.com/users/{}".format(username))
print(format_json(dict(response.headers)))



# repo = Repo("JabRef", "jabref")

