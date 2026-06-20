import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

df = pd.DataFrame(columns=['subject', 'mark', 'mistakes'])
df.to_csv('progress.csv', index=False)


root=tk.Tk()
root.title('Exam Progress Tracker')
root.geometry('1000x800')

subject=tk.Label(root,text='Subject',font=('Arial',12))
subject_entry=tk.Entry(root,width=20,font=('Arial',12))
subject.pack()
subject_entry.pack()
mark=tk.Label(root,text='Mark',font=('Arial',12))
mark_entry=tk.Entry(root,width=20,font=('Arial',12))
mark.pack()
mark_entry.pack()
mistakes_label = tk.Label(root, text='Mistakes', font=('Arial', 12))
mistakes_label.pack()

mistake_vars = {
    'c': tk.IntVar(),
    'p': tk.IntVar(),
    'n': tk.IntVar(),
    'l': tk.IntVar(),
    'x': tk.IntVar()
}

tk.Checkbutton(root, text='c - conceptual', variable=mistake_vars['c']).pack()
tk.Checkbutton(root, text='p - exam pressure', variable=mistake_vars['p']).pack()
tk.Checkbutton(root, text='n - not studied', variable=mistake_vars['n']).pack()
tk.Checkbutton(root, text='l - lack of practise', variable=mistake_vars['l']).pack()
tk.Checkbutton(root, text='x - nothing', variable=mistake_vars['x']).pack()

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
            mistakes = [code for code, var in mistake_vars.items() if var.get() == 1]
            if not mistakes:
             output.delete('1.0', 'end')
             output.insert('end', 'Please select at least one mistake.')
             return
            new_row={'subject':subject,'mark':mark,'mistakes':mistakes}
            self.df.loc[len(self.df)]=new_row
            self.df.to_csv('progress.csv',index=False)
            subject_entry.delete(0,'end')
            mark_entry.delete(0,'end')  
            
            for var in mistake_vars.values():
             var.set(0)
            output.insert('end','👍'
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
        if self.df.empty:
            output.delete('1.0','end')
            output.insert('end','No data available to analyze.')
            return
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
        self.df.plot(x='mark', y='subject', kind='bar')
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

