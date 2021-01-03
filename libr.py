import sys

arguments = sys.argv
print(f"We've recieved the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We're running on a '{sys.platform}' machine")



# import os

# my_folder = os.getcwd()
# print(f"Here are the files in {my_folder}")

# with os.scandir(my_folder) as folder:
#     for entry in folder:
#         print(f"- {entry.name}")

