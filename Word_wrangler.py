"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = []
    for element in list1:
        if element not in new_list:
            new_list.append(element)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    for element in list1:
        if element in list2 and element not in new_list:
            new_list.append(element)
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    merged = []
    # making copies to avoid list mutation
    copy1, copy2 = list1[:], list2[:]
    while min(copy1, copy2):
        # adding smaller item (and removing it from its list) one by one
        if copy1[0] < copy2[0]:
            merged.append(copy1[0])
            copy1.pop(0)
        else:
            merged.append(copy2[0])
            copy2.pop(0)

    # must include to whatever has been left in longer list (shorter list is empty by now)
    if copy1:
        merged += copy1
    else:
        merged += copy2
   
    return merged
            
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.    
    """
    if len(list1) == 1:
        return list1
    elif len(list1) == 2:
        return [min(list1), max(list1)]
    else:
        first_half = list1[:(len(list1) / 2)]
        second_half = list1[(len(list1) / 2):]
        return merge(merge_sort(first_half), merge_sort(second_half))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        copy_rest = list(rest_strings)
        print len(rest_strings)
        for element in rest_strings:
            for dummy in range(len(element) + 1):
                new_element = element[:dummy] + \
                first + element[dummy:]
                copy_rest.append(new_element)        
        return copy_rest

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    given_file = urllib2.urlopen(url)
    return given_file

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    
