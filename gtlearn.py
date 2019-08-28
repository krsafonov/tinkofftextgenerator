import random, re, pickle, argparse


class gentext:
    def __init__(self):
        self.data = {}
    def learn(self, file_name):
        file = open(file_name, 'r', encoding='cp1251')
        t = ""
        for line in file:
            t +=line.lower()
        file.close()
        text = re.findall('[a-zа-яё]+', t, flags=re.IGNORECASE)
        for item in range(len(text)-1):
            self.add_pair(text[item],text[item+1])

    def add_pair(self,w1,w2):
        if self.data.get(w1) == None:
            a = set()
            a.add(w2)
            self.data[w1]=a
        else:
            self.data[w1].add(w2)
    def save(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.data, f)
            f.close()
    def init(self):
        with open('data.pickle', 'rb') as f:
            self.data = pickle.load(f)
            f.close()
