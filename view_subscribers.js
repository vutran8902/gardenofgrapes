// Your Google Sheets API key
const API_KEY = 'YOUR_API_KEY_HERE';
// Your Google Sheets ID
const SHEET_ID = 'YOUR_SHEET_ID_HERE';
// The range of cells to fetch (adjust as needed)
const RANGE = 'Sheet1!A2:B';

function initClient() {
    gapi.client.init({
        'apiKey': API_KEY,
        'discoveryDocs': ["https://sheets.googleapis.com/$discovery/rest?version=v4"],
    }).then(function() {
        fetchSubscribers();
    }, function(error) {
        console.error('Error initializing Google Sheets API client', error);
    });
}

function fetchSubscribers() {
    gapi.client.sheets.spreadsheets.values.get({
        spreadsheetId: SHEET_ID,
        range: RANGE,
    }).then(function(response) {
        const subscribers = response.result.values;
        displaySubscribers(subscribers);
    }, function(response) {
        console.error('Error fetching subscribers', response.result.error.message);
    });
}

function displaySubscribers(subscribers) {
    const listElement = document.getElementById('subscriber-list');
    if (subscribers && subscribers.length > 0) {
        const list = subscribers.map(subscriber => `<p>${subscriber[0]} - ${subscriber[1]}</p>`).join('');
        listElement.innerHTML = list;
    } else {
        listElement.innerHTML = '<p>No subscribers found.</p>';
    }
}

gapi.load('client', initClient);
