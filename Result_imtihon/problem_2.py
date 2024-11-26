
def isValid (word: str)->bool:
    if len(word)<3:
        return False
    
    unli_count = 0
    undosh_count = 0

    for letter in word:
        if not letter.isalnum():
            return False
        if letter.lower() in 'aeiou':
            unli_count+=1
        else:
            undosh_count+=1
        
    if undosh_count>0 and unli_count>0:
        return True

    return False

    

if __name__ == "__main__":
    
    word = input("So'z kiriting: ")

    print(isValid(word))