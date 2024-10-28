from helper import parseme
import json
questionUrls = [
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-1.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-2.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-3.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-4.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-5.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-7.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-8.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-9.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-10.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-11.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-12.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-13.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-12.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-13.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-14.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-15.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-16.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-17.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-18.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-19.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-20.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-21.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-22.md',
    'https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-23.md',
    
]
questionDict = {'questions': []}
# test = parseme('https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md')

for targetUrl in questionUrls:
    test = parseme(targetUrl)
    for item in test:
        questionItem = {'prompt': '', 'options': [], 'correctAnswer': []}
        questionItem['prompt'] = item.prompt
        
        for opts in item.options:
            questionItem['options'].append(opts)
        
        for ans in item.correctAnswer:
            questionItem['correctAnswer'].append(ans)
        questionDict['questions'].append(questionItem)
    
json_question = json.dumps(questionDict, indent=4)
# print(json_question)
with open("questions.json", "w") as outfile :
    outfile.write(json_question)

