import requests
import json
from bs4 import BeautifulSoup
def parseme(url):
    print('parsing: ' + url)
    try:
        r = requests.get(url, timeout=10)
    except:
        print(url+' not parsed time out')

    soup = BeautifulSoup(r.content, 'html.parser')
    pnt = soup.select('ol[dir] > li')

    examList = []
    for item in pnt:
        options = []
        prompt = ''
        correctAnswer = []

        elemP = item.find('p')
        elemLi = item.find_all('li')
        elemDetails = item.find('details')

        answerString = elemDetails.get_text("")
        answer = answerString.replace(",", "").replace(" ","").replace("Answer", "").replace("Correctanswer:", "").strip()
      #  print(answer)

        child = elemDetails.findChildren('p', recursive=False)
        print(child)
        
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

    return examList


#r = requests.get('https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md')
#soup = BeautifulSoup(r.content, 'lxml')
#pnt = soup.select('ol[dir] > li')

class questionItem:
    def __init__(self, prompt, options, correctAnswer):
        self.prompt = prompt
        self.options = options
        self.correctAnswer = correctAnswer

#examList = []
#for item in pnt:
#    options = []
 #   prompt = ''
 #   correctAnswer = []

  #  elemP = item.find('p')
   # elemLi = item.find_all('li')
 #   elemDetails = item.find('details')

 #   answerString = elemDetails.get_text("")
   

  #  prompt = elemP.string
  #  for o in elemLi:
 #       options.append(o.string[3:])
 #   
  #  findString = 'Choose TWO'
  #  if findString in prompt:
  #      correctAnswer.append(answerString[-2])
  #      correctAnswer.append(answerString[-5])
 ##   else:
   #     correctAnswer.append(answerString[-2])
    
  #  examList.append(questionItem(prompt, options, correctAnswer))

#for item in examList:
  #  for opts in item.options:
  #      print(opts)
 
    
    