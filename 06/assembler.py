import re

filename=input()

symbol_table={"R0":0,"R1":1,"R2":2,"R3":3,"R4":4,"R5":5,"R6":6,"R7":7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4,"SCREEN":16384,"KBD":24576}

destination_table={"":"000","M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
jump_table={"":"000","JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}
comp_table={"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000","M":"1110000","!D":"0001101","!A":"0110001","!M":"1110001","-D":"0001111","-A":"0110011","-M":"1110011","D+1":"0011111","A+1":"0110111","M+1":"1110111","D-1":"0001110","A-1":"0110010","M-1":"1110010","D+A":"0000010","D+M":"1000010","D-A":"0010011","D-M":"1010011","A-D":"0000111","M-D":"1000111","D&A":"0000000","D&M":"1000000","D|A":"0010101","D|M":"1010101"}

binary_instructions=[]

with open(filename,'r') as file:
    code=[]
    for line in file:
        code.append(line.strip())

    removelist=[]
    for i in code:
        if (i[0:2]=="//") or (i==""):
            removelist.append(i)
    
    for i in removelist:
        code.remove(i)

    code1=[]
    for i in code:
        temp=i.split("//")
        code1.append(temp[0].strip())

code=code1

def decimaltoBinary(n):
    string=""
    while (n>0):
        if n%2==0:
            string="0"+string
        else:
            string="1"+string
        n=n//2
    while(len(string)<15):
        string="0"+string
    
    return string

def firstPass(code):
    global symbol_table
    line_no=0
    remove_labels_list=[]
    for i in code:
        if i[0]=="(":
            symbol_table[i[1:len(i)-1]]=line_no+1
            remove_labels_list.append(i)
        else:
            line_no+=1
        
    for i in remove_labels_list:
        code.remove(i)
    
    return code


def secondPass(code):
    global symbol_table
    global binary_instructions
    global comp_table
    global destination_table
    global jump_table

    variable_address=16

    for i in code:
        if i[0]=="@":
            try:
                var=int(i[1:])
            except ValueError:
                if i[1:] in symbol_table.keys():
                    var=symbol_table[i[1:]] #it is a label/ already encountered variable
                else:
                    symbol_table[i[1:]]=variable_address #it is a variable
                    var=variable_address
                    variable_address+=1
            
            elem="0"+decimaltoBinary(var)
            binary_instructions.append(elem)
    
        else:
            components=re.split("=|;",i)
            instruction="111"
            if len(components)==3:
                instruction=instruction+comp_table[components[1]]+destination_table[components[0]]+jump_table[components[2]]
            else:
                if len(i.split("="))==2:
                    instruction=instruction+comp_table[components[1]]+destination_table[components[0]]+"000"
                else:
                    instruction=instruction+comp_table[components[0]]+"000"+jump_table[components[1]]
            
            binary_instructions.append(instruction)

code=firstPass(code)
secondPass(code)

print(binary_instructions)

with open("program.hack",'w') as file:
    for i in binary_instructions:
        file.write(i)
        file.write("\n")