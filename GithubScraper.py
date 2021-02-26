import requests
import itertools
import dateutil.parser
from pprint import pprint

#I have no reason to care if you see my auth token. If there's a security breach, at least I'll know who did it.
#Jonathan Giraud CMSC 455

githubHundred = {}

## getting input for query page 1
#inputQuery = str(input("Type a search query or press 'enter' to search all Java repos.\n"))
inputQuery = ''
baseURL = (f"https://api.github.com/search/repositories?q={inputQuery}+is:public+language:Java+pushed%3A>2019-12-31")
searchRepo1 = requests.get(baseURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
repoList1 = searchRepo1.json()
counter = 1
# main loop
for item1 in repoList1['items']:
    username = item1['html_url']
    username = username[19:]
    sep = '/'
    stripped = username.split(sep, 1)[0]
    usernameAndRepo = (stripped + '/'+ item1['name'])
    #print('%d.) Username: %s Reponame: %s' % (counter, stripped, item1['name']))
    #pprint('Repo URL: %s' % item['name'])
    #print('Repo URL: %s' % item1['html_url'])
    apiKey = item1['html_url']
    apiURL = apiKey[:8] + 'api.' + apiKey[8:19] + 'repos/' + apiKey[19:] + '/stats/commit_activity'
    #print('API Key is: %s' % apiURL)

    commitDataURL = requests.get(apiURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
    commitList = commitDataURL.json()

    for commitData in commitList[0]:
        total = 0
        for i in range(1, 52):
            total = total + commitList[i]['total']

    reponame = usernameAndRepo
    totalCommits = int(total)
    githubHundred[reponame] = totalCommits

    #print('%d.) %s, %d' % (counter, usernameAndRepo, total))
    #newDate = dateutil.parser.parse(item1['updated_at']).date()
    #pprint('Last Event At: %s' % newDate)
    counter += 1

print("Found %d Repositories." %
      (counter - 1))


# #####################################################################################################################
# # getting input for query page 2
baseURL = (f"https://api.github.com/search/repositories?page=2&q={inputQuery}+is:public+language:Java+pushed%3A>2019-12-31")
searchRepo2 = requests.get(baseURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
repoList2 = searchRepo2.json()

# main loop
for item2 in repoList2['items']:
    username = item2['html_url']
    username = username[19:]
    sep = '/'
    stripped = username.split(sep, 1)[0]
    usernameAndRepo = (stripped + '/' + item2['name'])
    # print('%d.) Username: %s Reponame: %s' % (counter, stripped, item1['name']))
    # pprint('Repo URL: %s' % item['name'])
    # print('Repo URL: %s' % item1['html_url'])
    apiKey = item2['html_url']
    apiURL = apiKey[:8] + 'api.' + apiKey[8:19] + 'repos/' + apiKey[19:] + '/stats/commit_activity'
    #print('API Key is: %s' % apiURL)

    commitDataURL = requests.get(apiURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
    commitList = commitDataURL.json()

    for commitData in commitList[0]:
        total = 0
        for i in range(1, 52):
            total = total + commitList[i]['total']

    reponame = usernameAndRepo
    totalCommits = int(total)
    githubHundred[reponame] = totalCommits

    #print('%d.) %s, %d' % (counter, usernameAndRepo, total))
    # newDate = dateutil.parser.parse(item1['updated_at']).date()
    # pprint('Last Event At: %s' % newDate)
    counter += 1

print("Found %d Repositories." %
      (counter - 1))

# #####################################################################################################################
# # getting input for query page 3
baseURL = (f"https://api.github.com/search/repositories?page=3&q={inputQuery}+is:public+language:Java+pushed%3A>2019-12-31")
searchRepo3 = requests.get(baseURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
repoList3 = searchRepo3.json()

# main loop
for item3 in repoList3['items']:
    username = item3['html_url']
    username = username[19:]
    sep = '/'
    stripped = username.split(sep, 1)[0]
    usernameAndRepo = (stripped + '/' + item3['name'])
    # print('%d.) Username: %s Reponame: %s' % (counter, stripped, item1['name']))
    # pprint('Repo URL: %s' % item['name'])
    # print('Repo URL: %s' % item1['html_url'])
    apiKey = item3['html_url']
    apiURL = apiKey[:8] + 'api.' + apiKey[8:19] + 'repos/' + apiKey[19:] + '/stats/commit_activity'
    #print('API Key is: %s' % apiURL)

    commitDataURL = requests.get(apiURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
    commitList = commitDataURL.json()

    for commitData in commitList[0]:
        total = 0
        for i in range(1, 52):
            total = total + commitList[i]['total']

    reponame = usernameAndRepo
    totalCommits = int(total)
    githubHundred[reponame] = totalCommits

    #print('%d.) %s, %d' % (counter, usernameAndRepo, total))
    # newDate = dateutil.parser.parse(item1['updated_at']).date()
    # pprint('Last Event At: %s' % newDate)
    counter += 1

print("Found %d Repositories." %
      (counter - 1))

# #####################################################################################################################
# # getting input for query page 4
baseURL = (f"https://api.github.com/search/repositories?page=4&q={inputQuery}+is:public+language:Java+pushed%3A>2019-12-31")
searchRepo4 = requests.get(baseURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
repoList4 = searchRepo4.json()

# main loop
for item4 in repoList4['items']:
    username = item4['html_url']
    username = username[19:]
    sep = '/'
    stripped = username.split(sep, 1)[0]
    usernameAndRepo = (stripped + '/' + item4['name'])
    # print('%d.) Username: %s Reponame: %s' % (counter, stripped, item1['name']))
    # pprint('Repo URL: %s' % item['name'])
    # print('Repo URL: %s' % item1['html_url'])
    apiKey = item4['html_url']
    apiURL = apiKey[:8] + 'api.' + apiKey[8:19] + 'repos/' + apiKey[19:] + '/stats/commit_activity'
    #print('API Key is: %s' % apiURL)

    commitDataURL = requests.get(apiURL, auth=('Jogira','4d9f96a5ca21bc05c5ff05246050ef7b67afbdeb'))
    commitList = commitDataURL.json()

    for commitData in commitList[0]:
        total = 0
        for i in range(1, 52):
            total = total + commitList[i]['total']

    reponame = usernameAndRepo
    totalCommits = int(total)
    githubHundred[reponame] = totalCommits

    #print('%d.) %s, %d' % (counter, usernameAndRepo, total))
    # newDate = dateutil.parser.parse(item1['updated_at']).date()
    # pprint('Last Event At: %s' % newDate)
    counter += 1
    if (counter == 101):
        break

print("Found %d Repositories." %
      (counter - 1))


#print(githubHundred)
sortedGithubHundred = dict(sorted(githubHundred.items(),
                              key=lambda item: item[1],
                              reverse=True))
#print(sortedGithubHundred)

topTen = dict(itertools.islice(sortedGithubHundred.items(), 10))
print('\nTop 10 Github repositories with the most commits:')
for k,v in topTen.items():
    print(k, ('{:,}'.format(v)))