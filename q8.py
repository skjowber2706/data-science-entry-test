prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer:
# I think promptb will give better response


# Q8b: Give TWO reasons to support your choice.

# Your answer (Reason 1):
# prompt_b is better strucutred with clearer steps, so AI can follow easily

# Your answer (Reason 2):
# it clearly tells the role, task and audience which helps AI understand context better


# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer:
# prompt_a gives more real life context and explanes the situation better


# Task 2

# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.

# Your answer:

improved_prompt = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment.

Role: You are a data analyst helping a retail marketing team.

Task:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.

Audience: CEO presentation on Friday.
Constraints: keep it simple and no technical jargon.
"""

# Explanation:
# I borrowed the "Role" and "structured steps" from prompt_b
# becuase it makes the instruction more clear and easy for AI to follow
