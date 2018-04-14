######################################
# Copyright (c) 2017 Innocent Nsabimana & Partner: Dan Turner
# CSCI 150, Fall 2017
# Lab 9: Sentiment Analysis
######################################
import os

def result_message(score):
    if score > 2:
        print("score:", score)
        print("Positive! =)")
    else:
        print("score:", score)
        print("Negative. =(")

def average(score, count):
    if count != 0:
        return score/ count

def score_word(word):
    f = open("movieReviews.txt")
    rev = f.readlines()
    count = 0
    sum = 0
    for line in rev:
        review = line.lower().split()
        score = review[0]
        text = review[1:]
        if word in text:
            count += 1
            sum += int(score)
    if count != 0:
        return average(sum, count)
    else:
        return None

def score_user_word():
    word = input("Please enter a word:").lower()
    score = score_word(word)
    if score == None:
        print("Sorry, that word is not in the database.")
    else:
        result_message(score)

def score_phrase(phrase):
    count = 0
    total = 0
    lst_phrase = phrase.lower().split()
    for i in lst_phrase:
        word = score_word(i)
        if word != None:
            count += 1
            total += word
    if count != 0:
        return average(total, count)
    else:
        return None

def score_user_phrase():
    user_phrase = input("Please enter a word or phrase:").lower()
    user_score_phrase = score_phrase(user_phrase)
    if user_score_phrase == None:
        print("Sorry, none of those words are in the database.")
    else:
        result_message(user_score_phrase)

def read_movie_reviews(review_file):
    dict_score = {}
    dict_times = {}
    ovaral_dict = {}
    f = open(review_file)
    data = f.readlines()
    for line in data:
        words = line.lower().split()
        used_words = []
        for i in words[1:]:
            if i not in used_words:
                if i in dict_score:
                    dict_score[i] += int(words[0])
                    dict_times[i] += 1
                else:
                    dict_score[i] = int(words[0])
                    dict_times[i] = 1
                used_words.append(i)

    for i in dict_score:
        ovaral_dict[i] = dict_score[i]/dict_times[i]

    return ovaral_dict

def score_phrase_dict(word_scores, phrase):
    count = 0
    score = 0
    words = phrase.lower().split()
    for i in words:
        if i in word_scores:
            score += word_scores[i]
            count += 1

    return average(score, count)

def new_file():
    if os.path.isfile("movieReviews.txt.cache") == False:
        dictionary_data = read_movie_reviews("movieReviews.txt")
        file_out = open("movieReviews.txt" + ".cache", "w")
        for key in dictionary_data:
            file_out.write(key + " " + str(dictionary_data[key]) + "\n" )
        file_out.close()

    new_dict = {}
    file = open("movieReviews.txt.cache", "r")
    content = file.readlines()
    for line in content:
        line_list = line.lower().split()
        new_dict[line_list[0]] = float(line_list[1])
    file.close()
    return new_dict

def main():
    d = new_file()
    print("Reading movie reviews...")
    phrase = input("Please enter a phrase, or quit:")
    while phrase != "quit":
        phrase_score = score_phrase_dict(d, phrase)
        if phrase_score == None:
            print("Sorry, none of those words are in the database.")
        else:
            result_message(phrase_score)
        phrase = input("Please enter a phrase, or quit:").lower()
    print("Goodbye!")

main()




