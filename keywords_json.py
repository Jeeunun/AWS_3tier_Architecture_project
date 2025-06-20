import json

keywords = [
    ["Python", 50],
    ["AWS", 30],
    ["Lambda", 20],
    ["EC2", 10],
    ["S3", 15],
    ["Route53", 8]
]

with open("static/keywords.json", "w") as f:
    json.dump(keywords, f)
