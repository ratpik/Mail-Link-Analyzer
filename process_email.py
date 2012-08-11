import imaplib
from pattern import urlpattern
from diffbot import DiffBot

email = raw_input("Enter gmail id: ")
password = raw_input("Enter Password: ")
diffbot_api_key = "c539badebc2f19f621f616c52a0399d0"


#From http://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email, password)
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.uid('search', None, "ALL") # search and return uids instead
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]

#print raw_email

#TODO: Process email

urls_in_email = urlpattern.findall(raw_email)
api = DiffBot(diffbot_api_key)
extracted_content = []

for urlitem in urls_in_email:
    content = api.article(urlitem[0], summary=True)
    extracted_content.append(content)

print extracted_content
