from Language_Modeling import get_features
import math


yoruba_data = get_features("yoruba.txt")
igbo_data = get_features("igbo.txt")
hausa_data = get_features("hausa.txt")

Language_Lists = [yoruba_data, igbo_data, hausa_data]


def compare(test_file):
    #test_data = Project_code.lang_model(test_file)
    #print("CURRENT_LOG",test_file)
    test_data = get_features(test_file)
    #for element in test_data:
        #print element
        
    result = [0,0,0]
    for index,language in enumerate(Language_Lists):
        for ngram,prob in language:
            for ng,pb in test_data:
                if ngram == ng:
                    sim = float((prob * float(math.log(pb))) + (pb * float(math.log(prob))))
                    result[index]+=sim                 
    
    if result[0] < result[1] and result[0] < result[2]:
        print "Language is Yoruba"
    elif result[1] < result[0] and result[1] < result[2]:
        print "Language is Igbo"
    elif result[2] < result[0] and result[2] < result[1]:
        print "Language is Hausa"
    else:
        print "Not in database"

compare("hausa.txt")

    
        
            

