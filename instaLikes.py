import requests
clientId = open("instagramClientId").read()
print clientId

userName = raw_input("Enter A Username: ")

q = requests.get("https://api.instagram.com/v1/users/search?q=%s&client_id=%s" % (userName, clientId))

t = q.json()

userId = t["data"][0]["id"]

print "UserId: ", userId

next = requests.get("https://api.instagram.com/v1/users/%s/media/recent/?client_id=%s&count=0" %(userId, clientId))

final = next.json()

numberOfLikes = final["data"][0]["likes"]["count"]

print "Number of Likes: ", numberOfLikes
t
mediaId = final["data"][0]["id"]

print mediaId

actual = requests.get("https://api.instagram.com/v1/media/%s/likes?client_id=%s" % (mediaId, clientId))

likes = actual.json()

listOfLikes = []


for d in likes["data"]:
	 listOfLikes.append(d["username"])

for d in listOfLikes:
	print d
