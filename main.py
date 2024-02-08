def sort_on(dict):
    return dict["num"]


def report(source, strings, dict):
    wordcount = counter(strings)
    dict_list = [{"letter":a, "num": b} for a, b in dict.items() if a.isalpha()]
    dict_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {source} ---")
    print(f"{wordcount} words found in the document")
    for i in dict_list:
        print(f"The '{i['letter']}' character was found {i['num']} times")
    print("--- End report ---")


def counter(y):
    return len(y)

def splitter(y):
    return y.split()

def lettercounter(list):    
    lettercount = {}
    for words in list:
        for letter in words:
            lowercase = letter.lower()            
            lettercount[lowercase] = 0
    for words in list:
        for letter in words:
            lowercase = letter.lower()            
            lettercount[lowercase] += 1
    return lettercount

def main():
    source = "books/frankenstein.txt"    
    with open(source) as f:
        contents = f.read()
    strings = splitter(contents)   
    dict = lettercounter(strings)
    report(source, strings, dict)


    
       

            
        


main()
