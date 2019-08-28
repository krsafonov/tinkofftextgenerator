import random, re, pickle, argparse

class word:
    def __init__(self, name) :
        self.name = name
        self.count = 0
        self.deps = {}
        self.quantity = 0
    def add(self, dep):
        if self.deps.get(dep) == None:
            self.deps[dep] = 1
            self.count += 1
        else:
            self.count += 1
            self.deps[dep] += 1
        self.quantity +=1
    def random(self):
        random_int = random.randint(1, self.quantity)
        pos = 0
        for i in self.deps:
            pos += self.deps[i]
            if pos >= random_int:
                return i
    

class gentext:
    def __init__(self):
        self.data = {}
        self.allwordsquantity = 0
    def learn(self, file_name):
        try:
            file = open(file_name, 'r', encoding='cp1251')
            t = ""
            for line in file:
                t +=line.lower()
            file.close()
            text = re.findall('[a-zа-яё]+', t, flags=re.IGNORECASE)
            for item in range(len(text)-1):
                self.add_pair(text[item],text[item+1])
        except FileNotFoundError:
            print("File not found")
    def add_pair(self,w1,w2):
        if self.data.get(w1) == None:
            w = word(w1)
            w.add(w2)
            self.data[w1] = w
        else:
            self.data[w1].add(w2)
    def save(self):
        self.allwordsquantity = 0
        for i in self.data:
            self.allwordsquantity += self.data[i].count
        with open('allwordsquantity.pickle', 'wb') as f:
            pickle.dump(self.allwordsquantity, f)
            f.close()
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.data, f)
            f.close()
    def init(self):
        with open('data.pickle', 'rb') as f:
            self.data = pickle.load(f)
            f.close()
        with open('allwordsquantity.pickle', 'rb') as f:
            self.allwordsquantity = pickle.load(f)
            f.close()
    def printall(self):
        for i in self.data:
            print(self.data[i].name, self.data[i].count, self.data[i].deps)
    def clear(self):
        self.data = {}
        self.allwordsquantity = 0
        self.save()
    def get_random_word(self):
        random_int = random.randint(1, self.allwordsquantity)
        pos = 0
        for i in self.data:
            pos += self.data[i].count
            if pos >= random_int:
                return self.data[i].name
