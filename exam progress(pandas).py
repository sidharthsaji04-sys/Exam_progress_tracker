import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

df=pd.read_csv('progress.csv')
df['mistakes']=df['mistakes'].str.split(',')

root=tk.Tk()
root.title('Exam Progress Tracker')
root.geometry('1000x500')

title=tk.Label(root,text='Exam Progress Tracker',font=('Arial',16,'bold'))
title.pack(pady=10)

output=tk.Text(root,width=70,height=8,font=('Consolas',10))
output.pack(padx=10,pady=10)

class Progress:
    def __init__(self,df):
        self.df=df

    def calculate(self,mistake,mark):
        mistake_values = {'c': 3, 'a': 4, 'n': 2, 'p': 1, 'x': 0}
        mark_gap = ((25 - mark) / 25) * 10
        total = 0
        for m in mistake:
            total=total+mistake_values[m]
        mistake_weight=min(total/10*10,10)
        score=(mark_gap * 0.5) + (mistake_weight * 0.5)
        return score

    def band(self,scores):
        if scores>=4:
            return 'Needs serious study'
        elif scores>=3:
            return 'Need improvement'
        else:
            return 'Keep this momentum'

    def analyse(self):
        results = []
        for _, row in df.iterrows():
            subject= row['subject']
            marks = row['mark']
            mistake= row['mistakes']
            scores= self.calculate(mistake,marks)
            results.append({
                'Subject': subject,
                'Marks': marks,
                'Points': scores,
                'suggestion': self.band(scores)
            })

        result=pd.DataFrame(results).to_string(index=False)
        output.delete('1.0','end')
        output.insert('end',result)


    def graph(self):
        df.plot(x='subject', y='mark', kind='bar')
        plt.title('Progress Graph')
        plt.xlabel('Subject')
        plt.ylabel('Marks')
        plt.show()


p=Progress(df)

button_frame=tk.Frame(root)
button_frame.pack(pady=5)

button1=tk.Button(button_frame,text='Result',command=p.analyse,width=12)
button1.pack(side='left',padx=5)
button2=tk.Button(button_frame,text='Graph',command=p.graph,width=12)
button2.pack(side='left',padx=5)
root.mainloop()

