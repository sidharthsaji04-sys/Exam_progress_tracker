marks={'english':24,
       'maths':17,
       'chemistry':22,
       'physics':18,
       'biology':22}

#conceptual[c],avoided[a],not studied[n],exam pressure[p],nothing[x]
mistakes={'english':['c'],
           'maths':['c','p'],
           'chemistry':['c','a'],
          'biology':['a','n'],
          'physics':['a','c']}

mistake_values={'c':3,'a':4,'n':2,'p':1,'x':0}

class Progress:
    def calculate(self,mistake,mark):
        mark_gap=((25-mark)/25)*10
        total=0
        for m in mistake:
            total=total+mistake_values[m]
        mistake_weight=min(total/10*10,10)
        score=(mark_gap * 0.5) + (mistake_weight * 0.5)
        return score

    def band(self,scores):
        if scores>=4:
            return'Need serious study'
        elif scores>=3:
            return 'Some more effort is needed'
        else:
            return'Keep this momentum'

    def analyse(self):
        for subject, mark in marks.items():
            scores = self.calculate(mistakes[subject], mark)
            print(f'Subject:{subject}, mark:{mark}, score:{scores} - {self.band(scores)}')


p=Progress()
p.analyse()
