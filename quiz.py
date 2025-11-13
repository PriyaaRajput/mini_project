# -*- coding: utf-8 -*-
import time
question=[
    {"Question":"What is capital of India?","options":["Punjab","Delhi","U.P","Kashmir"],"Answer":1},
    {"Question":"smiling emoji?","options":["😊","😒","😣","😮"],"Answer":0}]
i=1
total_score=0
time_limit=5
for q in question:
    print(f" Ques{i+1}:{q["Question"]}")
    for index, option in enumerate(q["options"]):
        print(f"{index+1}:{option}")
    start=time.time()    
    ans=int(input("enter your answer(1-4)"))-1
    end=time.time()
    dif=start- end
    if(  dif> time_limit):
        print("Time's Up")
        break
    elif (ans==q["Answer"]):
        print("correct")
        print("your answer is recorded")
        total_score+=1
    else:
        print(f"the correct answer is:{q['options'][q['Answer']]}")
    i+=1  
    
"""    if dif>5:
        print("time's Up")
    else:    
      print("your answer is recorded")"""
print("The total score is :",total_score)    
      
