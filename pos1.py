#(C)Tsubasa Kato 2021/2/22
#Referenced https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b to make this script.
import nltk
#tokens = nltk.word_tokenize("Hello, I would like to go to Boston.")

inputfile = open('input.txt', 'r')
Lines = inputfile.readlines()


f = open('tagged.txt', 'w')
for line in Lines:
	line = line.replace("\n", "")
	tokens = nltk.word_tokenize(line)
	tagged = nltk.pos_tag(tokens)
	tagged_to_write = str(tagged)
	tagged_to_write = tagged_to_write.replace("\n", "")
	
	line_to_write = line + "\t" + tagged_to_write + "\n"
	print(line_to_write)	
	f.write(line_to_write)
	
f.close()
