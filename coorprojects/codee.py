# f =  open('data.txt','r')
# data = f.readlines()
# print(data)
# f.close()

#This Code are Same

with open('data.txt', 'r') as f:
    data = f.read()
    print(data)



with open('dataplusdata.txt', 'w') as f:
    f.write("I Add Some Line To Here")
    f.write("I Add another File In Python")
    