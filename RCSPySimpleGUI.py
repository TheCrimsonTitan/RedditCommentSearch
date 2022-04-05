import praw
import tkinter
import PySimpleGUI as sg


layout = [
        [sg.Text("Test")],
        [sg.Button("Search")]

]


window=sg.Window("Reddit Comment Search", layout).Finalize()
window.Maximize()

while True:
    event, values=window.read()
    if event == "Search" or event == sg.WIN_CLOSED:
        break
window.close()



#Reddit set up
reddit=praw.Reddit(

        client_id='sO1ypuzMA0DRwgD8aLcHCQ',
        client_secret='AAfpbdUosIlYfaxSjWuYzPDJ8rzqQA',
        username='',
        password='',
        user_agent='RedditCommentSearch'

        )

RedditorToSearch=input(" Input The Redditor")
Term=input("Input the Phrase: ")


for comment in reddit.redditor(RedditorToSearch).comments.new(limit=None):
    CommentContents=comment.body
   
   # print(CommentContents)
    if Term in CommentContents: 
        print(comment.submission.title)
        print(CommentContents)

