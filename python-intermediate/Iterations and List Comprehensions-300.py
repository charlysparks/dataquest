## 1. Introduction ##

import csv
f = open("top100.csv","r")
music = list(csv.reader(f))

artists = []
for row in music[1:]:
    artists.append(row[1])

## 2. Extract the Artists using a List Comprehension ##

artists = []
for row in music[1:]:
    artists.append(row[1])
artists_lc = [row[1] for row in music[1:]]

## 3. Getting the Artist Count using a function ##

def counter(artists):
    artist_dict = dict()
    for a in artists:
        if a in artist_dict.keys():
            artist_dict[a] += 1
        else:
            artist_dict[a] = 1
    return artist_dict

counts = counter(artists)

## 4. Getting the artist count using Counter() ##

from collections import Counter
artist_counts = Counter(artists)

## 5. Looping through our counts using the items() method ##

from collections import Counter
artist_counts = Counter(artists)

# Add your code here
artist_counts_list = []
for artist, count in artist_counts.items():
    artist_counts_list.append([artist, count])
print(artist_counts_list)

## 6. Using a List Comprehension ##

from collections import Counter
artist_counts = Counter(artists)
artist_counts_list = []
for artist, count in artist_counts.items():
    artist_counts_list.append([artist,count])
artist_counts_list_two = [[key,value] for key,value in artist_counts.items()]

## 7. Sorting our list of lists to extract the top value ##

artist_counts_list.sort()
first_artist = artist_counts_list[0]

## 8. Specifying a key when sorting our list ##

def by_count(artists):
    return artists[1]

artist_counts_list.sort(key=by_count, reverse=True)
top_artist = artist_counts_list[0]

## 9. Creating a function using lambda ##

f = open("top100.csv","r")
music = list(csv.reader(f))
artists = []
for row in music[1:]:
    artists.append(row[1])
from collections import Counter
artist_dict = Counter(artists)
artist_counts_lol = [[key,value] for key,value in artist_dict.items()]
artist_counts_lol.sort(key=lambda x: x[1], reverse=True)
lambda_top_artist = artist_counts_lol[0:1]

## 10. Creating a Pipeline using Modularization ##

# Add your functions here

# Uncomment when ready
# music_as_list = read_data("top100.csv")
# sorted_lol = clean_data(music_as_list)
# most_popular_artist = top_artist(sorted_lol)
def read_data(filename):
    f = open(filename,"r")
    music = list(csv.reader(f))
    return music

def clean_data(csv_list):
    artists = [row[1] for row in csv_list[1:]]
    artist_dict = Counter(artists)
    artist_counts_list= [[key,value] for key,value in artist_dict.items()]
    artist_counts_list.sort(key=lambda x: x[1], reverse=True)
    return artist_counts_list

def top_artist(list_of_lists):
    return list_of_lists[0]

music_as_list = read_data("top100.csv")
sorted_lol = clean_data(music_as_list)
most_popular_artist = top_artist(sorted_lol)

## 11. How to deal with errors ##

cleaned_list = []
for row in music_sample[1:]:
    try:
        cleaned_list.append([row[0], row[1],float(row[-1])])
    except:
        "Pass"

## 12. Passing new data into our pipeline ##

f = open("top100.csv","r")
music_all = list(csv.reader(f))

from collections import Counter

def extract_artist(music):
    return [row[1] for row in music[1:]]

def get_count(artists):
    artist_dict = Counter(artists)
    return [[key,value] for key,value in artist_dict.items()]

def sort_by_streams(artist_counts):
    artist_counts.sort(key=lambda x: x[1], reverse=True)
    return artist_counts

# Add your code here
artists = extract_artist(music_all)
artist_counts = get_count(artists)
top = sort_by_streams(artist_counts)