import os
import re
import socket
from collections import Counter

# File paths
file1_path = '/Users/tanujih/my_docker_project/data/IF.txt'
file2_path = '/Users/tanujih/my_docker_project/data/AlwaysRememberUsThisWay.txt'
output_path = '/Users/tanujih/output/result.txt'

# Function to read a file and count words
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        return words

# Count words in both files
words_file1 = count_words(file1_path)
words_file2 = count_words(file2_path)

total_words_file1 = len(words_file1)
total_words_file2 = len(words_file2)
grand_total = total_words_file1 + total_words_file2

# Find the top 3 most frequent words
top3_file1 = Counter(words_file1).most_common(3)

# Handle contractions in the second file
expanded_words = []
for word in words_file2:
    expanded_words.extend(re.split(r"['’]", word))

top3_file2 = Counter(expanded_words).most_common(3)

# Get the machine's IP address
ip_address = socket.gethostbyname(socket.gethostname())

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        print(f"Content of {file_path}: {text}")  # Debug: Print file content
        words = re.findall(r'\b\w+\b', text)
        return words

# Write results to the output file
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as output_file:
    output_file.write(f"Total words in IF.txt: {total_words_file1}\n")
    output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
    output_file.write(f"Grand total of words: {grand_total}\n")
    output_file.write(f"Top 3 words in IF.txt: {top3_file1}\n")
    output_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top3_file2}\n")
    output_file.write(f"IP Address: {ip_address}\n")

# Print the results to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())
