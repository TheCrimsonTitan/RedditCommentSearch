import praw


reddit=praw.Reddit(

        client_id='',
        client_secret='',
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

