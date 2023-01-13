#!/usr/bin/python3
def multiple_returns(sentence):
    # if to return len(sentence) sentence else return 0, None 
    return (len(sentence), sentence[0]) if sentence else (0, None) 
