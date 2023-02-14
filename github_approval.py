from github import Github

# Replace 'access_token' with your personal access token
g = Github('access_token')

# Replace 'repo_owner' and 'repo_name' with the repository's owner and name
repo = g.get_repo('repo_owner/repo_name')

# Retrieve a list of pull requests that are waiting for approval
pulls = repo.get_pulls(state='open', base='master', sort='created', direction='desc')

# Iterate through the list of pull requests and approve them
for pull in pulls:
    if not pull.mergeable:
        continue
    reviews = pull.get_reviews()
    for review in reviews:
        if review.user.login == 'your_github_username' and review.state == 'APPROVED':
            break
    else:
        pull.create_review(event='APPROVE')
