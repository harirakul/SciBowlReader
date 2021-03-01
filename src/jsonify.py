import os
import pickle
import json

SUBJECTS = ["BIOLOGY", "CHEMISTRY", "EARTH AND SPACE", "PHYSICS", "MATH", "ENERGY", "ASTRONOMY"]

filenames = []
for subdir, dirs, files in os.walk("data/sets"):
    for file in files:
        filepath = subdir + os.sep + file
        filenames.append(filepath)

for subject in SUBJECTS:
    print("Scraping subject " + subject)
    questions = []
    for filepath in filenames:
        with open(filepath, 'rb') as f:
            p = pickle.load(f)

        for q in p.questions:
            if q['Subject'] == subject:
                questions.append(q)

    with open(f'data/json/{subject}.json', 'w') as f:
        json.dump(questions, f, indent=4)
