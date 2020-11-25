capitals={"maharastra":"mumbai",
          "telugana":"hyderabad",}
print(capitals['maharastra'])
capitals['goa']='panaji'
print(capitals)
del capitals['maharastra']
universe={"star":"night","sun":"day"}
capitals.update(universe)
print(capitals)

college={"name":"mercy","reg.no":"4031","branch":"CSE"}
del college["reg.no"]
print(college)

fruits=["mango","apple","grapes"]
tastes=["texture","sweet","tart"]
dictionary=dict(zip(fruits,tastes))
print(dictionary)

set={1,2,3,4,5,6,7,8,9}
print(len(set))

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Original sets:")
print(set1)
print(set2)
print("Remove the intersection of a 2nd set from the 1st set ")
set1.difference_update(set2)
print(set1)











