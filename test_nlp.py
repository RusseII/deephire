from nltk import sent_tokenize, word_tokenize, pos_tag
import nltk
import RAKE
import os


text = "Machine learning is the science of getting computers to act without being explicitly programmed. " \
       "In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective " \
       "web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today " \
       "that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best " \
       "way to make progress towards human-level AI. In this class, you will learn about the most effective machine " \
       "learning techniques, and gain practice implementing them and getting them to work for yourself. More " \
       "importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the " \
       "practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, " \
       "you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning " \
       "and AI. "
text = "I look for extremely passionate individuals, who are excited to learn. "

# print(nltk.pos_tag(word_tokenize(text)))


path = 'SmartStoplists.txt'
print(os.listdir(os.getcwd()))

Rake = RAKE.Rake('SmartStoplist.txt');
# You can use one of the stoplists included in the repository under stoplists/
print (Rake.run(text));


# if everything in recruiter.Rake() is similar enough to everything in potentialHire.Rake()
# return potentialHire.profile()
