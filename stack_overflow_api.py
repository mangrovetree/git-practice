import requests

response = requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

# loop going through stack overflow and finding unanswered questions
for question in response.json()["items"]:
    if not question["is_answered"]:
        print(question["title"])
        print(question["link"])
        print()
