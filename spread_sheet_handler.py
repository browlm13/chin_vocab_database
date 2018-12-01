import gspread
from oauth2client.service_account import ServiceAccountCredentials
import character_searcher
import pandas as pd

CLIENT_SECRET_FILE = 'client_data/client_secret.json'
DATA_DIRECTORY = 'data'
CHIN_VOCAB_CSV_FILE = 'data/vocab_01.csv'
SPREAD_SHEET_NAME = "Chinese Vocab"
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#
# init client
#

creds = ServiceAccountCredentials.from_json_keyfile_name(CLIENT_SECRET_FILE, SCOPE)
client = gspread.authorize(creds)
sheet = client.open(SPREAD_SHEET_NAME).sheet1

# 
# update sheet
#
chin_vocab_df = pd.read_csv(CHIN_VOCAB_CSV_FILE)
COLUMN_HEADERS = list(chin_vocab_df.columns)

#
# helper functions
#

def char_position(letter):
    return ord(letter.lower()) - 97

def pos_to_char(pos):
    return chr(pos + 97).upper()

def header_2_cell(header,row):
	""" column header and row index to cell index """
	global COLUMN_HEADERS

	return "%s%s"% (pos_to_char(COLUMN_HEADERS.index(header)), row)

# testing
for h in COLUMN_HEADERS:
	print(header_2_cell(h,2))

def create_column_headers(COLUMN_HEADERS, sheet):

	range_string = 'A1:%s1' % pos_to_char(len(COLUMN_HEADERS))
	cell_list = sheet.range(range_string)

	for i, header in enumerate(COLUMN_HEADERS):
		cell_list[i].value = header

	# Update in batch
	sheet.update_cells(cell_list)

# create column header
#create_column_headers(COLUMN_HEADERS, sheet)


#cs = character_searcher.CharacterSearcher()
#results = cs.search_character('的')
