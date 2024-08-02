class operations():
    num=int(input("Enter a number:"))
    def OddEven():
        if((num%2)==0):
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
            
     def EligibilityForMarriage():
         gender=input("Your gender:")
         age=int(input("Your age:"))
         if(gender=='male'):
             if(age>=21):
                 print("eligible")
             else:
                 print("not eligible")
          if(gender=='female'):
              if(age>=18):
                  print("eligible")
              else:
                  print("not eligible")
                  
      def Percentage():
          a=int(input("Subject1:"))
          b=int(input("Subject2:"))
          c=int(input("Subject3:"))
          d=int(input("Subject4:"))
          e=int(input("Subject5:"))
          total=a+b+c+d+e
          print("total:",total)
          per=float(total)*(100/500)
          print("Percentage:",per)
          
       def triangle():
           height=int(input("height:"))
           breadth=int(input("breadth:"))
           area=breadth*height/2
           print("Area formula:(height*breadth)/2")
           print("Area:",area)
           height1=int(input("height1:"))
           height2=int(input("height2:"))
           breadth=int(input("breadth:"))
           perimeter=height1+height2+breadth
           print("perimeter formula:height1+height2+breadth")
           print("Perimeter of Triangle:",perimeter)
           
        def SubfieldsInAI():
            fields=['Machine Learning', 'Neural Networks', 'vision, Robotics', 'Speech Processing', 'Natural Language Processing']
            print("Sub-fields in AI are:")
            for char in fields:
                print(char)