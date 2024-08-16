# sample list
phrases = ["good morning","thank you","excuse me","bless you","good job"]
# shallow copy
sub_phrases = phrases[:2]
print(sub_phrases)
# changed good morning to good night, sublist index 0 changed from good morning to good night
# deep copy
deep_sub_phrases = phrases.copy()
print(deep_sub_phrases)