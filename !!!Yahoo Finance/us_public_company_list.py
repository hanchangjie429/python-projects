import requests
import pymysql


# url = https://www.nyse.com/listings_directory/stock
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'origin': 'https://www.nyse.com',
    'referer': 'https://www.nyse.com/listings_directory/stock'
}

url = 'https://www.nyse.com/api/quotes/filter'

data = {
    'filterToken': "",
    'instrumentType': "EQUITY",
    'maxResultsPerPage': 6527,
    'pageNumber': 1,
    'sortColumn': "NORMALIZED_TICKER",
    'sortOrder': "ASC"
}
response = requests.post(url, json=data, headers=headers)

# config your database here.
db_info = {
    'host': 'localhost',
    'db': 'cmind',
    'port': 3306,
    'user': 'root',
    'password': '******'
}

conn = pymysql.connect(**db_info)
cur = conn.cursor()


for i in response.json():
    url = i['url']
    exchangeId = i['exchangeId']
    instrumentType = i['instrumentType']
    symbol = i['normalizedTicker']
    instrumentName = i['instrumentName']
    micCode = i['micCode']
    sql = 'replace into us_public_company_list (symbol, instrumentName,instrumentType,exchangeId,micCode,url) values (%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (symbol, instrumentName,
                      instrumentType, exchangeId, micCode, url))
    conn.commit()
    print(i, '\n')
