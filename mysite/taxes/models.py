from django.db import models

class Client(models.Model):
    firstName= models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    taxYear = models.CharField(max_length=100)
    grossSalary = models.IntegerField()
    tax = models.IntegerField(default=0)
    

    def setFirstName(self,firstName):
        self.firstName=firstName
    def setLastName(self,lastName):
        self.lastName=lastName
    def setEmail(self,email):
        self.email=email
    def setTaxYear(self,taxYear):
        self.taxYear=taxYear
    def setGrossSalary(self,grossSalary):
        self.grossSalary=grossSalary
    def __str__(self):
        return self.email
    
    def calculateTax(self):
        
        tempSalary=int(self.grossSalary)
        
        if(self.taxYear=="2014/2015"):
 
            if (tempSalary > 10000):
                    tempSalary -= 10000
                    if (tempSalary > 31865):
                
                        self.tax += 31865 * 0.2
                        tempSalary -= 31865
                        if (tempSalary > 108135):
                            self.tax += 108135 * 0.4
                            tempSalary -= 108135
                            self.tax += tempSalary * 0.45

                            #return tax

                        else:                       
                         self.tax += tempSalary * 0.4
                         #return tax                  
                    else: 
                        self.tax =tempSalary * 0.2
                

            else:
                
                self.tax= 0
            
        else:
            if (tempSalary > 10600):
                tempSalary -= 10600
                if (tempSalary > 31785):
                    
                    self.tax += 31785 * 0.2
                    tempSalary -= 31785
                    
                    if (tempSalary > 107615):
                        
                        self.tax += 107615 * 0.4
                        tempSalary -= 107615
                        self.tax += tempSalary * 0.45
                        #return tax

                    else:                        
                        self.tax += tempSalary * 0.4
                        #return tax
                    
                else:                    
                    self.tax =tempSalary * 0.2
                

            else:
                self.tax= 0
        

