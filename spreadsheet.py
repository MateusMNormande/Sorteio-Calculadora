import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sorteio import functions

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Example-9999999999.json', scope)
client = gspread.authorize(creds)

nota = client.open('ProjetoCalculadora').sheet1

i = 0
j = 2
while True:
    f1, f2, f3 = functions[i]
    fun = f1 + " " + f2 + " " + f3
    nota.update_acell('C%i' % j, fun)
    i += 1
    j += 1
    if nota.acell('B%i' % j).value == '':
        break
