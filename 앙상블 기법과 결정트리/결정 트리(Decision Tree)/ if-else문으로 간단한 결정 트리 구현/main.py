def survival_classifier(seat_belt, highway, speed, age):
    if seat_belt == True:
        return 0
    else :
        if highway == True : 
            if speed > 100 : 
                if age > 50 :
                    return 1 
                else : 
                    return 0
            else : 
                return 0
        else : 
            return 0
    

print(survival_classifier(False, True, 110, 55))
print(survival_classifier(True, False, 40, 70))
print(survival_classifier(False, True, 80, 25))
print(survival_classifier(False, True, 120, 60))
print(survival_classifier(True, False, 30, 20))