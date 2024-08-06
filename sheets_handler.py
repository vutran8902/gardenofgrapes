import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("GardenOfGrapes_Subscribers").sheet1

def add_subscriber(name, email):
    """Add a new subscriber to the Google Sheet"""
    row = [name, email]
    sheet.append_row(row)
