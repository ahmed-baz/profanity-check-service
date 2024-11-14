from better_profanity import profanity

# Function to check for profanity
def check_profanity(text):
    return profanity.contains_profanity(text)    

# Function to clear the profanity text
def clear_text(text):
    return profanity.censor(text)