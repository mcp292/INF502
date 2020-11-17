import requests
import json
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from dateutil import parser
from datetime import date
from bs4 import BeautifulSoup as bs


def format_json(data):
    return json.dumps(data, sort_keys=True, indent=2)


def get_repo_summary(repo_index):
    try:
        repo = repos_list[repo_index]
        open_pull_requests = len([p for p in repo.pull_requests if p.state == "open"])
        closed_pull_requests = len([p for p in repo.pull_requests if p.state == "closed"])
        users = len(set([p.user for p in repo.pull_requests]))
        oldest_pull_request = min([parser.parse(p.date_of_creation) for p in repo.pull_requests])
        temp_users = list(set([p.user for p in repo.pull_requests]))

        print("\nSummary for " + str(repo.name) + " repository")
        print("No. of pull requests in open state   : " + str(open_pull_requests))
        print("No. of pull requests in closed state : " + str(closed_pull_requests))
        print("No. of users                         : " + str(users))
        print("Oldest pull request                  : " + str(oldest_pull_request.strftime('%m/%d/%Y')))
    except:
        raise IndexError



def print_graphics(repo_index):
    repo = repos_list[repo_index]
    pull_requests = [p for p in repo.pull_requests]
    df = pd.DataFrame([p.as_dict() for p in pull_requests])

    df["commits"] = pd.to_numeric(df["commits"])
    df["additions"] = pd.to_numeric(df["additions"])
    df["deletions"] = pd.to_numeric(df["deletions"])
    df["changed_files"] = pd.to_numeric(df["changed_files"])

    state_closed = df[df.state == "closed"]
    state_open = df[df.state == "open"]
    data_to_plot = [state_open['commits'], state_closed['commits']]
    plt.boxplot(data_to_plot, patch_artist=True)
    plt.title("open and closed pull requests per commits")
    plt.show()

    data_to_plot = [state_open['additions'], state_closed['additions']]
    plt.boxplot(data_to_plot, patch_artist=True)
    plt.title("open and closed pull requests per additions")
    plt.show()

    data_to_plot = [state_open['deletions'], state_closed['deletions']]
    plt.boxplot(data_to_plot, patch_artist=True)
    plt.title("open and closed pull requests per deletions")
    plt.show()

    df1 = df[['user', 'changed_files']]
    df1 = df1.groupby('user')['changed_files'].apply(list)
    df1 = df1.reset_index()
    data_to_plot = [d for d in df1['changed_files']]
    plt.boxplot(data_to_plot, patch_artist=True)
    plt.title("number of changed_files grouped by user")
    plt.show()

    plt.scatter(df['additions'], df['deletions'])
    plt.xlabel('additions')
    plt.ylabel('deletions')
    plt.title('additions vs deletions')
    plt.show()

    plt.hist(df['commits'])
    plt.ylabel('no. of commits')
    plt.title('no. of commits per pull request')
    plt.show()


def print_graphics_all():
    # get all pull requests for all repos
    pull_requests_list = []
    [pull_requests_list.extend(r.pull_requests) for r in repos_list]

    df = pd.DataFrame([p.as_dict() for p in pull_requests_list])

    df['date_of_creation'] = [parser.parse(x).date() for x in df['date_of_creation']]
    df['commits'] = pd.to_numeric(df['commits'])

    df['counts'] = df['commits']
    df1 = df[['date_of_creation', 'counts']]
    df1 = df1.groupby('date_of_creation').count()
    df1 = df1.reset_index()
    plt.plot(df1['date_of_creation'], df1['counts'])
    plt.title("number of pull requests per day")
    plt.xlabel("day")
    plt.ylabel("no. of pull-requests")
    plt.show()

    df_open = df[df['state'] == 'open']
    df_open = df_open[['date_of_creation', 'counts']]
    df_open = df_open.groupby('date_of_creation').count()
    df_open = df_open.reset_index()
    plt.plot(df_open['date_of_creation'], df_open['counts'], label='open')

    df_closed = df[df['state'] == 'closed']
    df_closed = df_closed[['date_of_creation', 'counts']]
    df_closed = df_closed.groupby('date_of_creation').count()
    df_closed = df_closed.reset_index()
    plt.plot(df_closed['date_of_creation'], df_closed['counts'], label='closed')

    plt.legend()
    plt.xlabel("day")
    plt.ylabel("no. of pull-requests")
    plt.title("open and closed pull-requests per day")
    plt.show()

    df_users_repo = pd.DataFrame(columns=['repo', 'users'])

    i = 0
    for r in repos_list:
        users = len(set([p.user for p in r.pull_requests]))
        df_users_repo.loc[i] = [r.name, users]
        i += 1

    plt.bar(df_users_repo['repo'], df_users_repo['users'])
    plt.xlabel("repository")
    plt.ylabel("no. of users")
    plt.title("no. of users per repository")
    plt.show()

    plt.hist(df['commits'])
    plt.xlabel("pull-request")
    plt.ylabel('no. of commits')
    plt.title('no. of commits per pull request')
    plt.show()


def list_all_repos():
    i = 1
    print("The repositories available are:\n")
    for r in repos_list:
        print(str(i) + ". " + str(r.name) + "\n")
        i += 1


def list_all_pull_requests(repo_index):
    repo = repos_list[repo_index]
    print("The pull requests are:\n")
    for p in repo.pull_requests:
        print("#{} {}".format(p.number, p.title))


def get_corr_users():
    # get all users
    users_list = []
    [users_list.extend(r.authors) for r in repos_list]

    df = pd.DataFrame([u.as_dict() for u in users_list]) # TODO: saloni explain to me

    df['followers'] = [x.replace(",", "").replace(" ", "") for x in df['followers']] # TODO: error int has no replace should we just remove the replaces?
    df['followers'] = [float(x[:-1]) * 1000 if x[-1] == 'k' else float(x) for x in df['followers']]

    df['following'] = [x.replace(",", "").replace(" ", "") for x in df['following']]
    df['following'] = [float(x[:-1]) * 1000 if x[-1] == 'k' else float(x) for x in df['following']]

    df['contributions'] = [x.replace(",", "").replace(" ", "") for x in df['contributions']]
    df['contributions'] = [float(x[:-1]) * 1000 if x[-1] == 'k' else float(x) for x in df['contributions']]

    df['repositories'] = [x.replace(",", "").replace(" ", "") for x in df['repositories']]
    df['repositories'] = [float(x[:-1]) * 1000 if x[-1] == 'k' else float(x) for x in df['repositories']]

    df['pull_requests'] = pd.to_numeric(df['pull_requests'])
    print(df.corr())


def get_corr_pull_requests(repo_index):
    try:
        repo = repos_list[repo_index]
        df = pd.DataFrame([p.as_dict() for p in repo.pull_requests])
        df = df[['commits', 'additions', 'deletions', 'changed_files']]
        df['commits'] = pd.to_numeric(df['commits'])
        df['additions'] = pd.to_numeric(df['additions'])
        df['deletions'] = pd.to_numeric(df['deletions'])
        df['changed_files'] = pd.to_numeric(df['changed_files'])
        print(df.corr())
    except:
        raise IndexError


class Repo:
    def __init__(self, user, repo):
        print("Collecting repo data...")

        response = sesh.get("https://api.github.com/repos/{}/{}".format(user, repo))
        # response = requests.get("https://api.github.com/repos/{}/{}".format(user, repo))

        if response.status_code == 200:
            repo_data = response.json()
            # print(self.format_json(repo_data))

            self.name = repo_data["name"]
            self.owner = repo_data["owner"]["login"]
            self.description = repo_data["description"]
            self.homepage = repo_data["homepage"]
            self.repo_license = repo_data["license"]["name"]
            self.num_forks = repo_data["forks_count"]
            self.watchers = repo_data["watchers"]
            self.date_of_collection = date.today()
            self.num_stars = repo_data["stargazers_count"]

            # get pull request data from first page (1)
            print("Collecting pull request data...")

            response = sesh.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
            # response = requests.get("https://api.github.com/repos/{}/{}/pulls?page={}".format(user, repo, 1))
            pull_request_data = response.json()

            # extract pull requests
            self.pull_requests = []

            for pull_request in pull_request_data:
                self.pull_requests.append(PullRequest(pull_request, user, repo))

            # for each extracted pull request store author
            print("Collecting user data...")
            
            self.authors = []
            existing_author = None  # default

            # add this author first (repo author)
            self.authors.append(Author(user))
            
            for pull_request in self.pull_requests:
                # check if author already added
                for author in self.authors:
                    if (author.user == pull_request.user):
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
            # we did it here to make sure all the information is complete
            # before writing (users with multiple pull requests etc.)
            self.write_to_csv(user, repo, self.pull_requests, self.authors)

            # print()
            # print(self.name)
            # print(self.owner)
            # print(self.description)
            # print(self.homepage)
            # print(self.num_forks)
            # print(self.watchers)
            # print(self.date_of_collection)
            # print(self.num_stars)
            # print([str(item) for item in self.pull_requests])
            # print([str(item) for item in self.authors])
        else:
            print("Request Failed with code: ",response.status_code)
            raise ValueError

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
        self.repo = repo
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
        # response = requests.get("https://api.github.com/repos/{}/{}/pulls/{}".format(user, repo, self.number))
        pull_request_data = response.json()

        self.num_commits = pull_request_data["commits"]
        self.additions = pull_request_data["additions"]
        self.deletions = pull_request_data["deletions"]
        self.changed_files = pull_request_data["changed_files"]

        # print all
        # print()
        # print(self.title)
        # print(self.number)
        # # print(self.body)
        # print(self.state)
        # print(self.date_of_creation)
        # print(self.user)
        # if (self.closing_date != None):
        #     print(self.closing_date)
        # print(self.num_commits)
        # print(self.additions)
        # print(self.deletions)
        # print(self.changed_files)
        # END print all


    def __str__(self):
        return "{} ({})".format(self.title, self.state)


    def to_CSV(self, filename):
        directory = os.getcwd() + "/repos"
        path = "{}/{}".format(directory, filename)

        # if dir doesn't exist
        if (not os.path.exists(directory)):
            try:
                os.mkdir(directory)
            except OSError:
                print ("Creation of the directory %s failed" % directory)

        file_exist = os.path.exists(path)

        with open(path, mode='a', newline='') as CSVfile:
            file_writer = csv.writer(CSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if (not file_exist):
                file_writer.writerow(vars(self))

            file_writer.writerow(vars(self).values())


    def as_dict(self):
        return {'state': self.state, 'commits': self.num_commits, 'additions': self.additions,
                'deletions': self.deletions, 'changed_files': self.changed_files, 'user': self.user,
                'date_of_creation': self.date_of_creation, 'repo': self.repo}


class Author:
    def __init__(self, user):
        self.user = user
        self.num_pull_requests = 1

        # set defaults for pages that might not have this data
        self.num_followers = 0
        self.num_following = 0
        self.num_contributions = 0
        self.num_repos = 0

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
        # else:
        #     print(user, "not found");
        #     print()


    def inc_num_pull_requests(self):
        self.num_pull_requests += 1


    def __str__(self):
        return "{}: {}".format(self.user, self.num_pull_requests)


    def to_CSV(self, filename):
        file_exist = os.path.exists(filename)

        header = vars(self).copy()

        with open(filename, mode='a', newline='') as CSVfile:
            file_writer = csv.writer(CSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if(not file_exist):
                file_writer.writerow(header)

            file_writer.writerow(header.values())


    def as_dict(self):
        return {'login': self.user, 'followers': self.num_followers, 'following': self.num_following,
                'contributions': self.num_contributions, 'pull_requests': self.num_pull_requests,
                'repositories': self.num_repos}



################### TEST SECTION ########################

import unittest

class TestFoo(unittest.TestCase):
    def test_no_Repo_case(self):
        self.failUnlessRaises(ValueError, Repo,"Jabref","NO_REPO")
    def test_no_owner_case(self):
        self.failUnlessRaises(ValueError, Repo,"NO_OWNER","Jabref")
    def test_get_repo_summary(self):
        self.failUnlessRaises(IndexError, get_repo_summary,-5)
    def test_get_corr_pull_requests(self):
        self.failUnlessRaises(IndexError, get_corr_pull_requests,-5)

if __name__ == '__main__':
    login_list = []
    users_list = []
    pull_requests_list = []
    repos_list = []
    username = 'gorkemnisanci96'
    token = '3668b7520d93f97e66041d9e40ae20c7b3b4e970'
    sesh = requests.Session()
    sesh.auth = (username, token)
    unittest.main()

########################################################



#if __name__ == "__main__":
#    # global vars
#    login_list = []
#    users_list = []
#    pull_requests_list = []
#    repos_list = []

#    username = 'mcp292'
#    token = ''
#    sesh = requests.Session()
#    sesh.auth = (username, token)

#    # check rate limit
#    # response = sesh.get("https://api.github.com/users/{}".format(username))
#    # print(format_json(dict(response.headers)))

#    select = 0

#    try:
#        while select != 10:

#            print("Choose from one of the following options: ")
#            print("\t1. Data for a specific repository from github")
#            print("\t2. List all the collected repositories")
#            print("\t3. List all pull requests from an existing repository")
#            print("\t4. List the summary of a repository")
#            print("\t5. Create graphics for a given repository")
#            print("\t6. Create graphics for all the collected repositories")
#            print("\t7. Calculate correlation between the data collected for users")
#            print("\t8. Calculate correlation between all the numeric data in the pull requests for a repository")
#            print("\t9. Exit")

#            select = int(input("Enter your choice: "))
#            if select == 1:
#                owner = input("Enter the github owner name: ")
#                repo = input("Enter the repository name: ")
#                print()
#                repos_list.append(Repo(owner, repo))
#            elif select == 2:
#                list_all_repos()
#            elif select == 3:
#                list_all_repos()
#                print("Select a repo from the list")
#                index = int(input("Enter index of repo: "))
#                list_all_pull_requests(index - 1)
#            elif select == 4:
#                list_all_repos()
#                print("Select a repo from the list")
#                index = int(input("Enter index of repo: "))
#                get_repo_summary(index - 1)
#            elif select == 5:
#                list_all_repos()
#                print("Select a repo from the list")
#                index = int(input("Enter index of repo: "))
#                print_graphics(index - 1)
#            elif select == 6:
#                print_graphics_all()
#            elif select == 7:
#                get_corr_users()
#            elif select == 8:
#                list_all_repos()
#                print("Select repo from the list")
#                index = int(input("Enter index of repo: "))
#                print()
#                get_corr_pull_requests(index - 1)
#            elif select == 9:
#                break
#            else:
#                print("invalid selection")

#            print()

#    except Exception as e:
#        print(e)
