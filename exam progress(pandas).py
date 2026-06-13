import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

df=pd.read_csv('progress.csv')
df['mistakes']=df['mistakes'].str.split(',')

root=tk.Tk()
root.title('Exam Progress Tracker')
root.geometry('1000x500')

subject=tk.Label(root,text='Subject',font=('Arial',12))
subject_entry=tk.Entry(root,width=20,font=('Arial',12))
subject.pack()
subject_entry.pack()
mark=tk.Label(root,text='Mark',font=('Arial',12))
mark_entry=tk.Entry(root,width=20,font=('Arial',12))
mark.pack()
mark_entry.pack()
mistakes=tk.Label(root,text='Mistakes (c-conceptual,p-exam pressure,n-not studied,l- lack of practise,x-nothing)',font=('Arial',12))
mistakes_entry=tk.Entry(root,width=20,font=('Arial',12))
mistakes.pack()
mistakes_entry.pack()

title=tk.Label(root,text='Exam Progress Tracker',font=('Arial',16,'bold'))
title.pack(pady=10)

output=tk.Text(root,width=90,height=10,font=('Consolas',10))
output.pack(padx=10,pady=10)

class Progress:
    def __init__(self,df):
        self.df=df
      

    def input_data(self):
            subject=subject_entry.get()
            try:
                mark=int(mark_entry.get())
            except ValueError:
                output.delete('1.0','end')
                output.insert('end','Please enter a valid integer for mark.')
                return
            mistake_values = {'c': 4, 'n': 3,'l': 2,'p': 1, 'x': 0}
            valid_mistakes = mistake_values.keys()  
            mistakes = mistakes_entry.get().split(',')
            for m in mistakes:
                if m not in valid_mistakes:
                    output.insert('end', f'Invalid mistake: {m}. Use c, n, l, p, or x only.')
                    return  
            new_row={'subject':subject,'mark':mark,'mistakes':mistakes}
            self.df.loc[len(self.df)]=new_row
            self.df.to_csv('progress.csv',index=False)
            subject_entry.delete(0,'end')
            mark_entry.delete(0,'end')  
            mistakes_entry.delete(0,'end')
            output.insert('end','Subject added successfully!'
            ) 
            return


    def calculate(self,mistake,mark):
        mistake_values = {'c': 4, 'n': 3,'l': 2,'p': 1, 'x': 0}
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
        for _, row in self.df.iterrows():
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
        if self.df.empty:
            output.delete('1.0','end')
            output.insert('end','No data available to plot.')
            return
        self.df.plot(x='subject', y='mark', kind='bar')
        plt.title('Progress Graph')
        plt.ylabel('Subject')
        plt.xlabel('Marks')
        plt.show()


p=Progress(df)

button_frame=tk.Frame(root)
button_frame.pack(pady=5)
button3=tk.Button(button_frame,text='Add Subject',command=p.input_data,width=12)
button3.pack(side='left',pady=5)
button1=tk.Button(button_frame,text='Result',command=p.analyse,width=12)
button1.pack(side='left',padx=5)
button2=tk.Button(button_frame,text='Graph',command=p.graph,width=12)
button2.pack(side='left',padx=5)
root.mainloop()

