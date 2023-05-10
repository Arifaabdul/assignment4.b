
# Tasks:

# 1. Create a 10 variables with your friend names?
lalitha="Lalitha"
mounika="Mounika"
harsha="Harsha"
saiLakshmi="SaiLakshami"
supriya="Supriya"
bindu="Bindu"
anusha="Anusha"
sowmya="Sowmya"
raji="Raji"
kamala="Kamala"

# 2. Create a 10 variables with your family member names?
samad="Samad"
aktharunnisa="Aktharunnisa"
anwar="Anwar"
arifa="Arifa"
asma="Asma"
sheerin="Sheerin"
azeem="Azeem"
fazeelath="Fazeelath"
fareed="Fareed"
ayaan="Ayaan"

# 3. Create a 10 variables with favorite food names?
friedRice="friedRice"
noodles="noodles"
chicken_biryani="chicken Biryani"
mutton_biryani="mutton Biryani"
chicken_fry="chicken Fry"
chicken_manchurian="chicken Manchurian"
veg_biryani="veg biryani"
veg_manchurian="veg Manchurian"
butter_naan="butter Naan"
egg_curry="egg Curry"

# 4. Create a 10 variables with colour  names?
red="Red"
blue="Blue"
green="Green"
orange="Orange"
purple="purple"
yellow="Yellow"
maroon="Maroon"
pink="Pink"
violet="Violet"
sky_blue="sky Blue"

# 5. Create a 12 variables with month  names?
january="January"
february="February"
march="March"
april="April"
may="May"
june="June"
july="July"
august="August"
september="September"
october="October"
november="November"
december="December"

# 6. Create a 10 variables with game names?
cricket="Cricket"
volleyball="Volleyball"
freefire="Freefire"
pubg="PUBG"
candy_crush="Candy Crush"
temple_run="Temple run"
angry_birds="Angry Birds"
subway_surfers="Subway Surfers"
carroms="Carroms"
puzzle_game="Puzzle Game"

# 7. Create a 10 variables with city  names?
Hyderabad="Hyderabad"
Visakhapatnam="Visakhapatnam"
Bangalore="Bangalore"
Mumbai="Mumbai"
Delhi="Delhi"
Chennai="Chennai"
Vijayawada="Vijayawada"
Guntur="Guntur"
Nellore="Nellore"
Kakinada="Kakinada"

# 8. Create a list (friend_names) with your friend names (10 names)?
friend_names=["Lalitha","Mounika","Harsha","Bindu","Anusha","Pravallika","Raji","Kamala","Supriya","Sai Lakshmi"]
print(friend_names)

# 9. Create a tuple (family_members) with your family members?
family_members=("Samad","Anwar","Azeem")
print(family_members)

# 10. Create a set (colours) with colour names(10 names)?
colours={"Red","Blue","Green","Orange","purple","Yellow","Maroon","Pink","Violet","sky Blue"}
print(colours)

# 11. month_names=[1,9,10,5,3,2,7,8,6,4] , sort the list--> write a program?
# expected output: month_names=[1,2,3,4,5,6,7,8,9,10]
month_names=[1,9,10,5,3,2,7,8,6,4]
def month_namess(month_names):   
    sett=set(month_names)    
    lst=list(sett)
    print(lst)
month_namess(month_names)

# 12. tollywood_heros=["chiru", "balaya", "nag","venky","powerstar","superstar","ntr","ramcharan"], write a program?
# expected output:tollywood_heros=["chiranjeevi","balakrishan","nagarjuna","venky","pawan kalyan","maheshbabu","NT rama rao","ramcharan"]
tollywood_heross=["chiranjeevi","balakrishan","nagarjuna","venky","pawan kalyan","maheshbabu","NT rama rao","ramcharan"]
def tollywood_heros(tollywood_heross):
    list=[]
    for hero in tollywood_heross:        
        list.append(hero)
        print(list)
tollywood_heros(tollywood_heross)

# 13. bollywood_heros=["sharukkhan", "salmankhan", "salmankhan","amirkhan","HrithikRoshan","Amitabh Bachchan","Akshay Kumar","amirkhan"],
#  write a program to remove duplicates?
bollywood_heross=["sharukkhan", "salmankhan", "salmankhan","amirkhan","HrithikRoshan","Amitabh Bachchan","Akshay Kumar","amirkhan"]
def bollywood_heros(bollywood_heross):
    sett=set(bollywood_heross)
    print(sett)
bollywood_heros(bollywood_heross)

# 14. breakfast_items=["upma","dosa","idly","puri","punugulu","roti","chapathi", "parota","mysoor baji","minapa baji"], print your favorite breakfast itme?
# example: My Favorite breakfast time is mysoor baji
breakfast_items=["upma","dosa","idly","puri","punugulu","roti","chapathi", "parota","mysoor baji","minapa baji"]
def breakfast_itemss(breakfast_items):
    for item in breakfast_items:
        print("My Favorite breakfast item is", item)
breakfast_itemss(breakfast_items)

'''15. What is function in python?'''
'''A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.'''

'''16. What is type function in python?'''
'''The type() function is mostly used for debugging purposes. Two different types of arguments can be passed to type() function, 
single and three arguments. If a single argument type(obj) is passed, it returns the type of the given object. 
If three arguments type(object, bases, dict) is passed, it returns a new type object. '''

'''17. what is print function in python?'''
'''The print() function prints the specified message to the screen, or other standard output device.
The message can be a string, or any other object, the object will be converted into a string before written to the screen.'''

'''18. what is overwriting in python?'''
'''Overwriting is the process of replacing old data with new data. It involves altering the pre-written data in a file. 
Overwriting a file can be understood as deleting an existing file and replacing it with a new one with the same name.
You must not confuse 'overwriting' and 'deleting' a file in Python with the same operations.
A deleted file can be recovered from the computer's memory, however, an overwritten file cannot. 
This occurs because an overwritten file replaces the original content of that file, causing the file to alter physically. 
As a result, retrieving data in this circumstance has less probability.'''