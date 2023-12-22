class grandfather:
    def gf_quality(self):
        print("insidgf class")
        print("gf is honest person")
        print("/n")
ganesh=grandfather()

class father(grandfather):
    def father_quality(self):
        print("inside father class")
        print("father is good person")
        
rajesh=father()
class son(father):
    def aim(self):
        print("inside son class")
        print("child wants to be a developer")
ritu=son()
ritu.gf_quality()
ritu.father_quality()
ritu.aim()

