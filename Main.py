'''
Created on Oct 24, 2018

@author: Joseph Baca
'''

from Lab3.AVL_Tree import AVLTree, Node
from Lab3.RedBlack_Tree import RedBlackTree, RBTNode




#------Code for Debuging:----
def printTree(root):
    if root == None:
        return None
    
    printTree(root.left)
    print(root.key)
    printTree(root.right)
#----------------------------


#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------This is the code given to us-----------------------------------------------------------

def load_words():
    with open("smallText") as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def print_anagrams(word, prefix=""):
    
    english_words = load_words()
    
    if len(word) <= 1:
        stri = prefix + word
        if stri in english_words:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                print_anagrams(before + after, prefix + cur)
                
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

#Creating a Global count to avoid confusion inside the recursive method
count=0    
def anagramsFromTree(word, userTree, prefix="" ):
    
    english_words = userTree
    global count
    
    if len(word) <= 1:
        stri = prefix + word
        if english_words.search(stri) == True: #Searches for the element in the Given Tree: AVL, RBT
            count+=1
            #print(prefix + word) # Will Print all Anagrams of a given word
           
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                anagramsFromTree(before + after,userTree, prefix + cur)
                
                
def count_anagrams(word, userTree):
    global count
    anagramsFromTree(word,userTree)
    return count

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------User Prompt for his/her Type of Tree--------------------------------------------------

def promptUser():
    
    userinput=""
    while userinput != AVLTree() or userinput != RedBlackTree():    # While the user has entered a proper tree
        userinput = input("Enter Type of tree. Example : 'AVL' or  'RBT' ")
        
        if userinput != "AVL" and userinput != "RBT":   # If the tree doesnt exist
            print("Sorry We're expecting: AVL or RBT")
        else:
            if userinput == "AVL":
                print()
                print("Thank you!")
                return "AVL"   # Return proper Tree as String to be converted later
            else:
                print()
                print("Thank you!")
                return "RBT" # Return proper Tree as String to be converted later


def storingWordsIn(userTree, textFile):
    
    textFile = open(textFile,"r").read().split("\n")
    
    if userTree == "AVL":
        print("----------------AVL TREE SELECTED-----------------")
        print("Processing your Data...")
        
        userTree = AVLTree()
        for line in textFile:
            userTree.insert(Node(line))    #AVL takes in a Node
            
            #print(line)    # Debugging: Make sure every line is properly inserted
            
    else:
        print("--------------RBT TREE SELECTED-------------------")
        print("Processing your Data...")
        
        userTree= RedBlackTree()
        for line in textFile:
            userTree.insert(line)   #RBT takes in a Key
        
            #print(line)    # Debugging: Make sure every line is properly inserted
    return userTree

#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

countForDict=0
def anagToDictHelper(word, MyTextFile, prefix="" ):     # Helper function that does the recursion and counts anagrams
    
    english_words = load_words()
    global countForDict
    
    if len(word) <= 1:
        stri = prefix + word
        if stri in english_words:
            countForDict+=1
            #print(prefix + word)
           
            
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.
                
                anagToDictHelper(before + after, MyTextFile, prefix + cur)


def anagramsToDictionary(dictionary, MytextFile):
    
    MytextFile = open(MytextFile, "r").read().split("\n")
    global countForDict
    
    for line in MytextFile:
        anagToDictHelper(line, MytextFile)
        dictionary[line] = countForDict
        countForDict=0
        
    dictionary = sorted(dictionary.items(), key= lambda t: t[1], reverse=True) # Lambda function tells the Sorted Method to Sort by the value in the dictionay.
    return dictionary


#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------


def main():
    
    textFile = "words_alpha.txt"
    #word = input("Enter your Word! ")    # Promps user for Word
    word = "spot"
    
    
    userTree = promptUser() # Prompts user for Tree
    userTree = storingWordsIn(userTree, textFile)
    print("Total Anagrams: ",count_anagrams(word, userTree)) # count_anagrams returns an int
    
    
    
    
    # ***************** This code retrives the word with the most anagrams *****************
    '''
    MytextFile = "smallText"
    dictionary={}
    
    dictionary =anagramsToDictionary(dictionary, MytextFile) # Puts anagrams Into the dictionary.
    #print(dictionary) #Debugging
    print("The word with the most Anagrams in the file is: ")
    print(*dictionary[0], sep = "  Anagrams: ")
    '''
    
    
main()




'''
To Do List:

    1. Promt the user for type of tree. (Done)
    2. Store words.txt in users prompt Tree. (Done)
    3. Write function: Count_anagrams() returns the number of anagrams that english word has. (Done)
    4. Make a random word file, then make a function to find the word with the most anagrams. (Done)
    

    -----------------------Notes-------------------------
    
        AVL: 
            #Insertion method takes in a Node
            #.remove_key or .remove_Node
        RBT: 
            #Insertion method takes in a key
            #_bst_remove(key) removes a node
    
    myRBTree = RedBlackTree()
    myRBTree.insert("Hey im RBT! ")
    #myRBTree._bst_remove(2)
    print(myRBTree.search("Hey im RBT! ").key)
    
    
    myAVLTree = AVLTree()
    myAVLTree.insert(Node("Hey im AVL! "))
    #myAVLTree.remove_key(2)
    print(myAVLTree.search("Hey im AVL! ").key)
    
    -----------------------Notes-------------------------
'''



