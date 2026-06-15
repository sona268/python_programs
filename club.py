# Student Information (String)

club_name=input("Enter Club Name: ")
print(club_name.upper())
print(club_name.lower())
print(club_name.title())
old_word=input("Enter the word: ")
new_word=input("Enter new word: ")
print("Replaced Word: ",club_name.replace(old_word,new_word))
position=input("Enter word to find: ")
print("Position: ",club_name.find(position))
occurrence=input("Enter the character: ")
print("Character to count: ",club_name.count(occurrence))
start=input("Enter starting letter: ")
print("Starts With: ",club_name.startswith(start))
end=input("Enter ending letter: ")
print("Ends With: ",club_name.endswith(end))
print(club_name.split())
print(club_name.strip())


# Club Activities (Tuple)

activities=("Coding","Quiz","Workshop","Hackathon","Quiz")
print("Club Activities: ",activities)
print("First Activity: ",activities[0])
print("Last Activity: ",activities[-1])
print("Slicing: ",activities[1:4])
print("Occurence: ",activities.count("Workshop"))
print("Index: ",activities.index("Hackathon"))


# Club Members (List)

members=["Anju","Raju","Manu"]
members.append("Arun")
members.extend(["Anil","Neha"])
members.insert(1,"Ramu")
members.remove("Anju")
members.pop(-1)
members.sort()
members.reverse()
print("Index: ",members.index("Manu"))
print("Count: ",members.count("Manu"))
print(members)


# Club Event Participation (Set)

student1={"Appu","Ramu","Dona"}
student2={"Ammu","Dona","Raju"}
student1.add("Sona")
student1.update(["Anu","Manu"])
student1.remove("Ramu")
student1.discard("Sona")
print(student1)
print(student1.union(student2))
print(student1.intersection(student2))
print(student1.symmetric_difference(student2))