import pickle
import warnings
warnings.filterwarnings("ignore")

with open('model/MLE.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    mle = pickle.load(f)

while True:             
    word = input("Enter a word: ")
    if word == "q":       
        break
    else:
        next = mle.generate(text_seed=[word], random_seed=5)
        score = mle.score(word)
        print("Next word is :",next)
        print("Score is :",score)   
    
    


