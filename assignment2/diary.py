#Task 1: Diary
import traceback
import os 

try:
 with open("diary.txt", "a") as file:
      first_prompt = True
      
      
      while True:
            if first_prompt:
                user_input = input("What happened today?")
                first_prompt = False
            else:
                user_input = input("What Else?")
            
            file.write(user_input + "\n")
            
            if user_input.lower() == "done for now":
                print("Diary entry completed. Goodbye!")
                break
    
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
    
    
    
    