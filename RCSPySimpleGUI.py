import praw
import tkinter
import PySimpleGUI as sg
import xlsxwriter as excel


#Reddit set up
def Search(RedditorName, TermtoSearch):

    #print(RedditorName)
    reddit=praw.Reddit(

            client_id='sO1ypuzMA0DRwgD8aLcHCQ',
            client_secret='AAfpbdUosIlYfaxSjWuYzPDJ8rzqQA',
            username='',
            password='',
            user_agent='RedditCommentSearch'

            )

    RedditorToSearch=RedditorName
    Term=TermtoSearch

    #Setting up the excel workbook
    workbook = excel.Workbook('1.xlsx')


    for comment in reddit.redditor(RedditorToSearch).comments.new(limit=None):
        CommentContents=comment.body
       
       # print(CommentContents)
        if Term in CommentContents: 
             print(comment.submission.title)
           # print(CommentContents)


sg.theme('DarktanBlue')

layout = [
        [sg.Text("Welcome")],
        [sg.Text("Name of Redditor:"), sg.InputText(key="Name")],
        [sg.Text("Term to Search"),sg.InputText(key="Term")],
        [sg.Button("Search")],
        [sg.Button("Exit")],
        
]


window=sg.Window("Reddit Comment Search", layout, size=(400,600), resizable=True).Finalize()
#window.Maximize()

while True:
    event, values=window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Search":
        Search(values['Name'],values['Term'])
window.close()



