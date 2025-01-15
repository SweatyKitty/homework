class WordsFinder:
	def __init__(self,*file_name):
		self.file_names=[]
		for i in file_name:
			self.file_names.append(i)
	def get_all_words(self):
		self.all_words={}
		for i in self.file_names:
			with open(i,encoding='utf-8') as tf:
				t=tf.read()
				t=t.lower()
				t.replace(',',' ')
				t.replace('.',' ')
				t.replace('=',' ')
				t.replace('!',' ')
				t.replace('?',' ')
				t.replace(';',' ')
				t.replace(':',' ')
				t.replace(' - ',' ')
				t=t.split()
				self.all_words[i]=t
				return self.all_words
	def find(self,word=''):
		wordmini=word.lower()
		w_pos={}
		for name,words in	self.get_all_words().items():
				for i in range(0,len(words)):
					if wordmini==words[i]:
						w_pos[name]=i+1
						break
					else:
						continue	
		return(w_pos)
		
	def count(self,word=''):
		wordmini=word.lower()
		w_count={}
		for name,words in	self.get_all_words().items():
			x=0
			for i in words:
					if wordmini==i:
						x+=1
						continue
					else:
						continue
			w_count[name]=x
		return w_count
		
finder2 = WordsFinder('text.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

#finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
#print(finder1.get_all_words())
#print(finder1.find('Child'))
#print(finder1.count('Child'))	