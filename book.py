from browser import aio

import war_and_peace as wp

from collections import Counter



import string



def count_words(text):

    temp = text.split()

    word_count = 0

    for word in temp:

            word_count += 1

    return word_count



def count_vowels(text):

    vowels = ['a', 'e', 'i', 'o', 'u']

    vowel_count = 0

    for letters in text:

        if letters.lower() in vowels:

            vowel_count += 1

    return vowel_count



def count_distinct_words(text):

    words = text.lower().split()  

    distinct_words = Counter(words)  

    return len(distinct_words)

   

def count_paragraphs(text):

    paragraphs = text.split('\n')

    paragraph_count = Counter(paragraphs)

    return len(paragraph_count)

   



def count_sentences(text):

    sentence_count = text.count('.') + text.count('?') + text.count('!') + text.count('...')

    return sentence_count

   

def letter_frequency(text):

    return {letter: text.lower().count(letter) for letter in string.ascii_lowercase}

   

def word_frequency(text):

    words = text.lower().split()

    word_counts = {}

    for word in words:

        if word in word_counts and word:

            word_counts[word] += 1

        else:

            word_counts[word] = 1

    return sorted(word_counts.items(), key=lambda item: item[1], reverse = True)

   

def pair_frequency(text):

    total = text.lower().count("to the")

    return total

   

def sentence_frequency(text):

    end_punctuation = {'.', '?', '!', '...'}

    sentences = []

    start = 0



    for i, char in enumerate(text):

        if char in end_punctuation:

           

            if i + 1 < len(text) and text[i + 1] == ' ' and (i + 2 == len(text) or text[i + 2].isupper()):

                sentences.append(text[start:i + 1].strip())

                start = i + 2

   

    if start < len(text):

        sentences.append(text[start:].strip())



    sentence_counts = Counter(sentences)

   

    return sentence_counts

   

def pair_each_sentence(text):

    search_string = "to the"  

    text = text.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ')

    sentences = text.replace('!', '.').replace('?', '.').split('.')  

    string_counts = {}

    for sentence in sentences:

        trimmed_sentence = sentence.strip()  

        if trimmed_sentence:  

            count = trimmed_sentence.lower().count(search_string)  

            if count > 0:

                string_counts[trimmed_sentence] = count  



    return sorted(string_counts.items(), key=lambda item: item[1], reverse = True)

   

def pair_each_paragraph(text):

    search_string = "to the"  

   

    paragraphs = text.split('\n')

    string_counts = {}

    for paragraph in paragraphs:

        trimmed_paragraph = paragraph.strip()  

        if trimmed_paragraph:  

            count = trimmed_paragraph.lower().count(search_string)  

            if count > 0:

                string_counts[trimmed_paragraph] = count  



    return sorted(string_counts.items(), key=lambda item: item[1], reverse = True)

   



async def main():

    book = await wp.book()
    

   

    print(f'there are {count_words(book)} words in war and peace')

    print(f'there are {count_vowels(book)} vowels in war and peace')

    print(f'there are {count_distinct_words(book)} distinct words in war and peace')

    print(f'there are {count_sentences(book)} sentences in war and peace')

    print(f'there are {count_paragraphs(book)} paragraphs in war and peace')

    print(f'Frequency of each letter{letter_frequency(book)}')

    print(f'Frequency of each word: {word_frequency(book)}')

    print(f'Frequency of each sentence: {sentence_frequency(book)}')

    print(f"Frequency of the pair 'to the': {pair_frequency(book)}")

    print(f"Frequency of 'to the' in each sentence: {pair_each_sentence(book)}")

    print(f"Frequency of 'to the' in each paragraph: {pair_each_paragraph(book)}")

    





aio.run(main())
