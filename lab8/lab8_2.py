import requests
import json
import random

# 2.1 
character_id = random.randint(1, 826)
character_url = f"https://rickandmortyapi.com/api/character/{character_id}"
character_response = requests.get(character_url).json()

# 2.2 
print("JSON Response:", json.dumps(character_response, indent=2))

# 2.3 
file_name = f"info_character_{character_id}.json"
with open(file_name, 'w') as file:
    json.dump(character_response, file, indent=2)
print(f"JSON response saved to {file_name}")

# 2.4 
episode_urls = character_response['episode']
episode_ids = [int(url.split("/")[-1]) for url in episode_urls]

# 2.5 
example_episode_url = "https://rickandmortyapi.com/api/episode/1"
example_episode_response = requests.get(example_episode_url).json()
episode_attributes = example_episode_response.keys()

# 2.6 
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

# 2.7 2.8
episode_objects = []
for episode_id in episode_ids:
    episode_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    episode_data = requests.get(episode_url).json()
    episode_objects.append(Episode(**episode_data))

# 2.9 
all_episodes_url = "https://rickandmortyapi.com/api/episode"
all_episodes_response = requests.get(all_episodes_url).json()

# 2.10
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

# 2.11  2.12
random_character = Character(**character_response)


# 2.13 Result
print(f"\nRandom Character ID: {character_id}")
print("\nEpisode URLs:")
for url in episode_urls:
    print(url)
print("\nEpisode Objects:")
for episode_obj in episode_objects:
    print(f"{episode_obj.name} - {episode_obj.id}")

print("\nRandom Character Object:")
print(f"Name: {random_character.name}")
print(f"Status: {random_character.status}")
print(f"Species: {random_character.species}")

