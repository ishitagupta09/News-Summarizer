from tkinter import *
#import nltk
from textblob import TextBlob
from newspaper import Article

root=Tk()

root.title('News Summary')
root.geometry('650x350')

def summarize():
    text=entry_url.get()
    article=Article(text)
    article.download()
    article.parse()
    article.nlp()
    
    entry_url.delete(0,END)
    
    title=Label(root,text=f'Title:{article.title}',font='Calibri 14 bold')
    author=Label(root,text=f'Authors:{article.authors}')
    publication_date=Label(root,text=f'Publication date:{article.publish_date}')
    summary=Label(root,text=f'Summary:{article.summary}',font='Calibri 14 italic')
    
    title.pack()
    author.pack()
    publication_date.pack()
    summary.pack()

label_url=Label(root,text='Enter news url:',font='Calibri 24')
label_url.pack()
entry_url=Entry(root,font='Calibri 14 italic')
entry_url.pack(fill=X)
btn=Button(root,text='Summarize',font='Calibri 14 italic',command=lambda:summarize())
btn.pack()

root.mainloop()
