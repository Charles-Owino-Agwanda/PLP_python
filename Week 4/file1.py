with open("input.txt", "r") as file:
        data = file.read()
        print(data)
        
word_count = len(data.split())
print(f"The word_count is: {word_count}")

upper_case = data.upper()

with open("output.txt", "w") as output_file:
    output_file.write(upper_case)
    output_file.write(f"\n")
    output_file.write(f"\n The word count is: {word_count}")

        

#for i in data:
    #print(i)
    
#print(data)