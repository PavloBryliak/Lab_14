from linkedbst import LinkedBST
from time import time
import random


def open_file():
    """
    Function to open and pars txt file, which
    returns first 1100 words from given words library.
    """
    with open("words.txt", "r") as f:
        words = list(map(lambda x: x.strip(), f.readlines()))[0:1100]
    return words


def random_words():
    """Function to randomly chose 1100 finding words"""
    lst = []
    words = open_file()
    random.shuffle(words)
    for i in range(1100):
        lst.append(words[i])
    return lst


def list_search(file, word_list):
    """Function to find randomly chosen 1100 words"""
    lst = []
    for i in word_list:
        lst.append(i in file)


def build_tree(file):
    """Function to build a tree with given elements"""
    tree = LinkedBST()
    for i in file:
        tree.add(i)
    return tree


def search_tree(tree, r_words):
    """Function for finding given elements in Binary Search Tree"""
    for i in r_words:
        tree.find_words(i)


if __name__ == '__main__':

    words = random_words()
    _open = open_file()
    tree = build_tree(_open)

    start1 = time()
    search_tree(tree, words)
    print("Binary Search Tree searching time: ", time() - start1)

    start2 = time()
    list_search(_open, words)
    print("List searching time: ", time() - start2)