import requests
import json
from bs4 import BeautifulSoup
def parseme(url):
    print('parsing')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
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
        print(answerString.replace(",", "").replace(" ","").replace("Answer", "").replace("Correctanswer:", "").strip())
        # print(answerString)
        
        prompt = elemP.string
        for o in elemLi:
            options.append(o.string[3:])

        findString = 'Choose TWO'
        if findString in prompt:
            correctAnswer.append(answerString[1].upper())
            correctAnswer.append(answerString[2].upper())
        else:
            correctAnswer.append(answerString[1].upper())

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
 
    
    