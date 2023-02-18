# Import Required Module
import requests
from bs4 import BeautifulSoup

# Web URL
Web_url = "https://content.acloud.guru/911064fb-0683-46b2-8ba6-07db3901cd47/1351620000001-000010.mp4?Expires=1672763280&Signature=am6KQJ73vIAt97WfO2RUV9iB0/bzeZzegM+pTf49lMM69XJimhGlkAN6XK+0LSpFKkgSp6wTGH/jo8YEeUzTw6eO0gzkKt7x+ojd0xBD7ywW17bPDhXxS8HW2Y5Rj81ZSc6LOBQ9oXOoWV+jzw5y/CtbbA5af3bgQ0WDDj9tffQxHsgZtZeyjmB/OpdcdPf+2DKUBIQInqBO/DdGHq9v0DVPGZgiKjNNPAogE1aGt89Z1SwiLdl7PBavGSmflCSQgbkSmbANBtC9Yz81IQwxW0IAoS5a9mRidHmeU5BVVACbCOorvwtpYW7uSZ72DdUon/Jevsjo0dPe74NSHQusXA==&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jb250ZW50LmFjbG91ZC5ndXJ1LzkxMTA2NGZiLTA2ODMtNDZiMi04YmE2LTA3ZGIzOTAxY2Q0Ny8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjcyNzYzMjgwfX19XX0=&Key-Pair-Id=APKAISLU6JPYU7SF6EUA"

# Get URL Content
r = requests.get(Web_url)

# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')

# List of all video tag
video_tags = soup.findAll('video')
print("Total ", len(video_tags), "videos found")

if len(video_tags) != 0:
	for video_tag in video_tags:
		video_url = video_tag.find("a")['href']
		print(video_url)
else:
	print("no videos found")

