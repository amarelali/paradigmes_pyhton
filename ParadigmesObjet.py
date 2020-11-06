class Polynomial:
    def __init__(self,coeficient =0 ):
        if coeficient == 0 :
            print("le polynome est null") 
        else:
            self.coeficient = coeficient
            self.degree = len(coeficient) - 1

    def derivative(self):

        equationDerivee =[]
        
        for coeficient in self.coeficient:
            equationDerivee.append(coeficient * (self.degree))
            self.degree -= 1 
        p = Polynomial(equationDerivee)
        return p
        
    def __call__(self,valeurDeX):
        resultat = 0
        for coeficient in self.coeficient:
            resultat += int(coeficient) * valeurDeX
        print("P(",valeurDeX,") == " ,resultat) 
         
def afficheEquation(listEq):
        String_eq = "P(X)= "
        length = len(listEq)
        for coeficient in listEq :
            
            if (length - listEq.index(coeficient) -1) == 0 : 
               
                if str(coeficient) == "1":
                    String_eq += str(coeficient) + "X"
                else:
                    String_eq += str(coeficient) + "X"
            else:
                
                String_eq += str(coeficient) + " X^" + str(length-listEq.index(coeficient) -1)  + " + " 
        print(String_eq)        

def afficheEquationDerivee(listEqderivee):
        String_eq = "P'(X)= "
        length = len(listEqderivee)
        for coeficient in listEqderivee :
            
            if (length - listEqderivee.index(coeficient) -1) == 0 : 
               
                if str(coeficient) == "1":
                    String_eq += str(coeficient) + "X"
                else:
                    String_eq += str(coeficient) + "X"
            else:
                
                String_eq += str(coeficient) + " X^" + str(length-listEqderivee.index(coeficient) -2)  + " + " 
        print(String_eq)
            
        
if __name__ == "__main__":
    p = Polynomial() 
    p2 = Polynomial(0) 
    #p3 = Polynomial([1,2]) 
    p3 = Polynomial([3,2,1]) 
    p4 = Polynomial([3,2,1,0,0])
    afficheEquation(p4.coeficient)
    p5 = p4.derivative()
    afficheEquationDerivee(p5.coeficient)
    # print("coeficient du derivee ", p5.coeficient)
    p5(1)
    
