import requests
import json
import time
import html5lib
from bs4 import BeautifulSoup
def parseme(url):
    print('parsing: ' + url)
    
    r = requests.get(url, timeout=10)
    
    if r.status_code != 200:
        print('error')
        return
    
    soup = BeautifulSoup(r.content, 'html.parser')
 
    pnt = soup.select('ol[dir] > li')
    
    if(len(pnt) <= 0):
        return []

    examList = []
    for item in pnt:
        options = []
        prompt = ''
        correctAnswer = []

        elemP = item.find('p')
        elemLi = item.select('ul > li:not(details > ul li)')
        elemDetails = item.find('details')
        # print(elemP.string)
        # print(elemLi)
      
      #  print(answer)
        answer = ''
        countAnsElement = elemDetails.findChildren('p', recursive=False)
        # print(countAnsElement)
        if len(countAnsElement) >= 1:
            child = elemDetails.find('p')
            answer = child.string.replace(",", "").replace(" ","").replace("Answer", "").replace("Correctanswer:", "").replace("Correct:", "").strip()
            print(answer)
        else:
            answerString = elemDetails.get_text("")
            answer = answerString.replace(",", "").replace(" ","").replace("Answer", "").replace("Correctanswer:", "").strip()
            print(answer)
       
        
        prompt = elemP.string
        for o in elemLi:
            options.append(o.string[3:])

       # findString = 'Choose TWO'
        ansLength = len(answer)
        if ansLength > 1:
            correctAnswer.append(answer[0].upper())
            correctAnswer.append(answer[1].upper())
        else:
            correctAnswer.append(answer[0].upper())

        examList.append(questionItem(prompt, options, correctAnswer))
    print('done parsing')
    return examList


#r = requests.get('https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md')
#soup = BeautifulSoup(r.content, 'lxml')
#pnt = soup.select('ol[dir] > li')

class questionItem:
    def __init__(self, prompt, options, correctAnswer):
        self.prompt = prompt
        self.options = options
        self.correctAnswer = correctAnswer

    