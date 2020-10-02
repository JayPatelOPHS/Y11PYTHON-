print("welcome to a new game")       # welcomes players to game
age=int(input("enter your age"))
gender=str(input("enter your gender"))        
email=str(input("enter your email address"))  #lines 4-7 ask user to input info
name=str(input("enter your player name"))
print("age:", age)
print("gender:", gender)     # check if info is correct
print("email:", email)
print(" player name:", name)
check=str(input("is all of this info correct enter y for yes and n for no"))
while check == "n":
  age=int(input("enter your age"))
  gender=str(input("enter your gender"))        
  email=str(input("enter your email address"))  
  name=str(input("enter your player name"))
end while check == "y":
  print ("you can now play this game")
  print(age,gender,email,name)
