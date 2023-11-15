import requests
from bs4 import BeautifulSoup

base_url = 'https://www.jpnshiken.com'

# 問題一覧を取得
url = base_url + '/shiken/ServiceNow.CSA-JPN.v2023-09-05.q157.html'
response = requests.get(url)
cookies = response.cookies
soup = BeautifulSoup(response.text, 'html.parser')
questions = soup.select('.barlist > dd > a')

# 問題を取得
datas  = '<!DOCTYPE html>\n'
datas += '<html lang="ja">\n'
datas += '<head>\n'
datas += '    <script src="main.js"></script>\n'
datas += '    <link rel="stylesheet" href="main.css" type="text/css">\n'
datas += '</head>\n'
datas += '<body>\n'
count = 0
for question in questions:
    count += 1
    print(f'{count}/{len(questions)}')
    data = {}
    response = requests.get(base_url + question.get('href'), cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.select('.qa-question')
    for element in elements:
        data['question'] = element.text.strip()
    elements = soup.select('.qa-options')
    for element in elements:
        data['options'] = '            '.join(str(element) for element in element.contents).strip()
    elements = soup.select('.qa-answerexp > div > span')
    for element in elements:
        data['answer'] = element.text.strip()
    datas += '    <div class="qa">\n'
    datas += '        <div class="qa-number">\n'
    datas += '            質問 ' + str(count) + '/' + str(len(questions)) + '\n'
    datas += '        </div>\n'
    datas += '        <div class="qa-question">\n'
    datas += '            ' + data["question"] + '\n'
    datas += '        </div>\n'
    datas += '        <div class="qa-options">\n'
    datas += '            ' + data["options"] + '\n'
    datas += '        </div>\n'
    datas += '        <div class="qa-answer">\n'
    datas += '            ' + data["answer"] + '\n'
    datas += '        </div>\n'
    datas += '        <div class="qa-button">\n'
    datas += '            解答表示\n'
    datas += '        </div>\n'
    datas += '    </div>\n'
datas += '</body>\n'
datas += '</html>\n'

# ファイル出力
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(datas)
