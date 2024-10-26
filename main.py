from helper import parseme

questionUrls = [
    
]
dict = {questionnaire: []}
test = parseme('https://github.com/kananinirav/AWS-Certified-Cloud-Practitioner-Notes/blob/master/practice-exam/practice-exam-6.md')

for item in test:
    for opts in item.options:
        print(opts)