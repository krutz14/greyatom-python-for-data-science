# --------------
#Code starts here

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    fileopen=open(path,"r")
    #Reading of the first line of the file and storing it in a variable
    sentence=fileopen.readline()
    #Closing of the file
    fileopen.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message=read_file(file_path)
#Printing the line of the file


message_1=read_file(file_path_1)
message_2=read_file(file_path_2)

#Function to fuse message

def fuse_msg(message_a,message_b):

    #Integer division of two numbers
    quot=int(message_b)//int(message_a)

    #Returning the quotient in string format
    quotient=str(quot)
    return quotient
#Calling the function to read file  
secret_msg_1=fuse_msg(message_1,message_2)


message_3=read_file(file_path_3)

#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c=='Red':
        sub='Army General'
    elif message_c=='Green':
        sub='Data Scientist'
    elif message_C=='Blue':
        sub='Marine Biologist'
    return sub
    
    
secret_msg_2= substitute_msg(message_3)

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
#Function to compare message

def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split(" ")
    b_list=message_e.split(" ")    
    c_list=[]
    #Comparing the elements from both the lists
    for i in a_list:
        if i not in b_list:
            c_list.append(i)
    final_msg=" ".join(c_list)
    #Combining the words of a list back to a single string sentence
    return final_msg
    
    #Returning the sentence
    
secret_msg_3=compare_msg(message_4,message_5)   

#Calling the function to read file

message_6=read_file(file_path_6)

def extract_msg(message_f):
    a_list=message_f.split(" ")
    
    
    even_word=lambda y:(len(y)%2==0)

    b_list=list(filter(even_word,a_list))
    final_msg=" ".join(b_list)
    return final_msg
    

secret_msg_4=extract_msg(message_6)

message_parts=[secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
secret_msg=" ".join(message_parts)
print(secret_msg)
def write_file(secret_msg,path):
    fileopen=open(path,"a+")
    fileopen.write(secret_msg)
    fileopen.close()
final_path= user_data_dir + '/secret_message.txt'
write_file(secret_msg,final_path)



