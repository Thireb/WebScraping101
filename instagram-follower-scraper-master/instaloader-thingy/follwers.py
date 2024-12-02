import instaloader

L = instaloader.Instaloader(user_agent="--no-iphone")
L.login('Choudary_writes','76.warraich')
USER = "ameerhamzarubani"
PROFILE = USER

# Load session previously saved with `instaloader -l USERNAME`:
#L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, PROFILE)

# likes = set()
# print("Fetching likes of all posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     print(post)
#     likes = likes | set(post.get_likes())

print("Fetching followers of profile {}.".format(profile.username))
followers = set(profile.get_followers())
#print(followers)
for follwer in profile.get_followers():
    print(follwer)
#ghosts = followers - likes
#
#print("Storing ghosts into file.")
#with open("inactive-users.txt", 'w') as f:
#    for ghost in ghosts:
#        print(ghost.username, file=f)
