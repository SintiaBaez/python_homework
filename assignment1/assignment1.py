# Task 1 - Hello
def hello():
    return "Hello!"


print(hello())

# Task 2 - Greet


def greet(name):

    return f"Hello, {name}!"


print(greet("Sintia"))

# Task 3 - Calculator


def calc(a, b, operation="multiply"):
    try:

     match operation:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
          return a / b
        case "modulo":
            return a % b
        case "int_divide":
            return a // b
        case "power":
            return a ** b
      
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
   
# Task 4 -  Data Type Conversion

def data_type_conversion(value, data_type):
    
    try:
        
      match data_type:
        case "int":
            return int(value)
        case "float":
            return float(value)
        case "bool":
            return bool(value)
        case "str":
            return str(value)
    except ValueError:
       return f"You can't convert {value} into a {data_type}."
   
# Task 5 - Grading System, using *args

def grade(*args):
    try:
       average = sum(args) / len(args)
     
       if average >= 90 and average <= 100:
         return "A"
       elif 80 <= average <= 89:
        return "B"
       elif 70 <= average <= 89:
        return "C"
       elif 60 <= average <= 69:
        return "D"
       else: 
        return "F"
    
    except TypeError:
        return "Invalid data was provided."
    
# Task 6 - Use a For Loop with a Range

def repeat(str, count):
    for i in range(count):
        print(str)
    return str * count

#7 - Student Scores, Using **kwargs

def student_scores(type_of_score, **kwargs):
     
    if type_of_score == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    
    elif type_of_score == "mean":
        total_score = sum(kwargs.values())
        num_students = len(kwargs)
        mean_score = total_score / num_students
        return mean_score
    
    for key, value in kwargs.items():
      print(f"{key} received a score of {value}")
      
# Task 8 - Titleize, with String and List Operations

def titleize(str):
    litle_words = ["in", "the", "of", "and", "or", "from"]
    words = str.split()
    
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    
    for i in range(1, len(words) - 1):
        if words[i] not in litle_words:
            words[i] = words[i].capitalize()
            
    return " ".join(words)

# Task 9 - Hangman, with more String Operations

def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

# Task 10 - Pig Latin, Another String Manipulation Exercise


def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[:2] == "qu":
            pig_latin_word = word[2:] + "quay"
        elif word[0] in vowels:
            pig_latin_word = word + "ay"
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    pig_latin_word = word[i:] + word[:i] + "ay"
                    break
        pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)