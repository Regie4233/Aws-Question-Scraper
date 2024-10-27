from helper import parseme
import json
questionUrls = [
    
]
questionDict = {'questions': []}
test = parseme('https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md')

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