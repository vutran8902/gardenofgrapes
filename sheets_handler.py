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

def update_subscribers_file():
    """Retrieve all subscribers from the Google Sheet and write to a text file"""
    # Get all values from the sheet
    values = sheet.get_all_values()
    
    # Skip the header row if it exists
    if values and values[0] == ['Name', 'Email']:
        values = values[1:]
    
    # Write to subscribers.txt
    with open('subscribers.txt', 'w') as f:
        f.write("# Subscriber List\n")
        f.write("# Format: Name,Email\n")
        for row in values:
            f.write(f"{row[0]},{row[1]}\n")
