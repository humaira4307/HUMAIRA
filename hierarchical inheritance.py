class C:
    def X_pattern(self,name):
        self.name=str(input("enter ur name"))
        length=len(name)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(name[j],end=" ")
            else:
                print(" ",end=" ")
        print()
C1=C()


                