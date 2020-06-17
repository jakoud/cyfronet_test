from pymongo import MongoClient
from pprint import pprint

client = MongoClient(port=27017)
db=client.grades
  
score_subject=0
weights=0
score_total=0
grade_total=0
class_counter=0
subjects_list=[]
grades={}

for student_number in range(50):
    class_counter=0
    grade_total=0
    score_total=0
    for class_number in range(31):
        cursor=db.grades.find({"student_id":student_number, "class_id":class_number})
        
        for element in cursor:
            
            score_subject=0
            weights=0
            for score in element['scores']:
                if score['type']=="homework":
                    score_subject+=score['score']*20
                    weights+=20
                elif score['type']=="exam":
                    score_subject+=score['score']*60
                    weights+=60
                elif score['type']=='quiz':
                    score_subject+=score['score']*20
                    weights+=20
                
            score_subject=score_subject/weights
            score_total+=score_subject
            class_counter+=1
   
    grade_total+=score_total/class_counter
    grades[student_number]=grade_total

pprint(grades)