#!/usr/bin/env python
# coding: utf-8

# In[3]:


# run this code to login to https://okpy.org/ and setup the assignment for submission
from ist256 import okclient
ok = okclient.Homework()


# # Now You Code 3: Limerick Generator
# 
# We will write code in this example to create the first two lines of a [Limerick](https://en.wikipedia.org/wiki/Limerick_(poetry). We're going to keep it really simple, and ask for 4 inputs:
# - a woman's name  
# - a place
# - an item
# - a material 
# 
# The place and material must rhyme. The Python program will then output the first two lines of the limerick, substituting the values you've entered. 
# 
# **Example 1:**
# 
# INPUT:
# 
# - Enter a woman's name: Jane
# - Enter a place: New York
# - Enter an item: hat
# - Enter a material, which rhymes with 'New York': cork.
# 
# OUTPUT:
# I once knew Jane from New York. Her hat was constructed of cork.
# 
# **Example 2:**
# 
# INPUT:
# 
# - Enter a woman's name: Agatha
# - Enter a place: my car
# - Enter an item: bike
# - Enter a material, which rhymes with 'my car': tar
# 
# OUTPUT: 
# I once knew Agatha from my car. Her bike was constructed of tar.
# 

# ## Step 1: Problem Analysis
# 
# Inputs:
# 
# Enter a woman's name: Agatha
# 
# Enter a place: my car
# 
# Enter an item: bike
# 
# Enter a material, which rhymes with 'my car': tar
# 
# OUTPUT: I once knew Agatha from my car. Her bike was constructed of tar.
# 
# Algorithm (Steps in Program):
# 
# Ask the user for a name of a woman
# 
# Ask for a place
# 
# Ask for an item 
# 
# Ask for a material that rhymes with the person's given place
# 
# print the given words in a predesigned sentence

# In[1]:


# Step 2: Write code here
name = input("Enter a woman's name: ")
place = input("Enter a place: ")
item =  input("Enter an item: ")
material = input(f"Enter a material, which rhymes with '{place}': ")
print(f'I once knew {name} from {place}. Her {item} was constructed of {material}.')


# ## Step 3: Questions
# 
# 1. What happens when neglect to follow the instructions and enter any inputs we desire? Does the code still run? Why?
# 
# Answer:  The program does not care about what type of text is entered, only if there is text.
# 
# 
# 2. What type of error occurs when the program runs but does not handle bad input?
# 
# Answer:   Logic Error
# 
# 
# 3. Is there anything you can do in code to correct this type of error? Why or why not?
# 
# Answer:  I guess you could make the code only accept words from a list that you give the program, but that is not currently in my realm of understanding.
# 
# 
# 

# ## Step 4: Reflection
# 
# Reflect upon your experience completing this assignment. This should be a personal narrative, in your own voice, and cite specifics relevant to the activity as to help the grader understand how you arrived at the code you submitted. Things to consider touching upon: Elaborate on the process itself. Did your original problem analysis work as designed?  How many iterations did you go through before you arrived at the solution? Where did you struggle along the way and how did you overcome it? What did you learn from completing the assignment? What do you need to work on to get better? What was most valuable and least valuable about this exercise? Do you have any suggestions for improvements?
# 
# To make a good reflection, you should journal your thoughts, questions and comments while you complete the exercise.
# 
# Keep your response to between 100 and 250 words.
# 
# `--== Write Your Reflection Below Here ==--`
# 
# I thought this homework was pretty straightforward, everything that I had to do I have done before. The only bit that gave me some issues was when I was having the code give the output I forgot to add the 'f' before the string, which meant it wasn't properly printing the variables. I like that the first couple things we've had to do is easing us in and letting us get a grasp on the syntax of the language. I am excited for the upcoming assignments that will push my understanding of coding.

# In[ ]:


# to save and turn in your work, execute this cell. Your latest submission will be graded. 
ok.submit()


# In[ ]:




