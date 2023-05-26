
import spacy

nlp = spacy.load("en_core_web_md")

# read the movies.txt file and create a movie description list
with open("movies.txt", "r") as file:
    movie_description = [line.strip() for line in file]


def find_similar_movie(description):
    # initialize the maximum similarity score and the most similar movie title
    max_similarity = -1
    most_similar_movie = ""

    # process the input description
    doc1 = nlp(description)

    # iterate over each movie description and calculate its similarity score
    for desc in movie_description:
        doc2 = nlp(desc)
        similarity = doc1.similarity(doc2)
        
        # if the similarity score is higher than the current maximum, update the maximum and the most similar movie title
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = desc.split("\t")[0]

    # check if any similarities were found
    if max_similarity > -1:
        return most_similar_movie
    else:
        return "A similar movie was not found."

# test the function with the given input description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous" \
              "for the Earth, the Illuminati trick Hulk into a shuttle and launch him into" \
              "space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on" \
              "the planet Sakaar where he is sold into slavery and trained as a gladiator."

similar_movie = find_similar_movie(description)
print("Please watch:", similar_movie)