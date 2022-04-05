import praw
import tkinter
import PySimpleGUI as sg



#Reddit set up
def Search():
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


sg.theme('DarktanBlue')

layout = [
        [sg.Text("Welcome")],
        [sg.Button("Search")],
        [sg.Button("Exit")],
        
]


window=sg.Window("Reddit Comment Search", layout, size=(800,600), resizable=True).Finalize()
#window.Maximize()

while True:
    event, values=window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Search":
        Search()
window.close()



