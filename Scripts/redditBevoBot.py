import praw
import time

_author_ = 'bevo'

# Spellcheck settings
words_to_match = ['collorado', 'collaredo']
correct_spelling = "Colorado"
correction_comment = f'I think you meant to write "{correct_spelling}"'

# Subreddit settings
subreddit_to_grab = "test"
#reddit_user = ""
#reddit_passwd = ""

# Program settings
checkedCommentsCache = []

r = praw.Reddit(user_agent="TutorialBot to CheckSpelling /u/SpellCheckBevo1Bot")
print("")
# r.login(reddit_user, reddit_passwd, disable_warning=True)
r.login(disable_warning=True)

def post_correction_comment(comment):
    ''' Post comment to correct incorrect spelling'''
    comment.reply(correction_comment)
    print("          * Correction posted *")

def run_bot():
    ''' Grab comments from a subreddit and post spelling correction to a configured word'''
    correctionsPosted = 0
    commentsChecked = 0
    commentsAlreadyChecked = 0
    print(f"Grabbing subreddit '{subreddit_to_grab}'...")
    subreddit = r.get_subreddit(subreddit_to_grab)
    print ("Grabbing comments...")
    comments = subreddit.get_comments(limit=25)
    print ("Checking comments.")
    for comment in comments:
        if comment.id not in checkedCommentsCache:
            comment_text = comment.body.lower()
            isMatch = any(string in comment_text for string in words_to_match)
            if isMatch:
                print(f'Match found! Comment ID: {comment.id}')
                comment.refresh()
                doPostCorrection = True
                print("  Comment not checked.")
                print(f'    Is_Root    : {str(comment.is_root)}')
                print(f'    Replies#   : {str(len(comment.replies))}')
                for reply in comment.replies:
                    print("      Checking reply for correction")
                    if reply.body == correction_comment:
                        print(f'        Comment already corrected in reply : {reply.id}')
                        doPostCorrection = False
                        break
                if doPostCorrection:
                    correctionsPosted += 1
                    post_correction_comment(comment);
            print("    Adding comment to checked Cache.")
            commentsChecked += 1
            checkedCommentsCache.append(comment.id)
        else:
            commentsAlreadyChecked += 1
    print ("Comments loop finished:")
    print (f'   Comments already checked   : {str(commentsAlreadyChecked)}')
    print (f'   Comments newly checked     : {str(commentsChecked)}')
    print (f'   Corrections posted         : {str(correctionsPosted)}')
    print ("  time to sleep")
    print


while True:
    run_bot()
    time.sleep(10)