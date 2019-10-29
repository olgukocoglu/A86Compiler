# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:54:41 2017

@author: Olgu
"""





class assembly(object):
    
    def __init__(self,mystring):
        
        self.commands=[] #array for assembly codes for input
        
        self.variables=[] #array for variables of input
        
        self.mystring=mystring #input string
        
        self.parsedarray=[] #array of the input after parsing
        
        self.funcno=0 #number to increment for different functions
        
    def showcommands(self): #it returns the assembly code for the input
        
        if len(self.commands)==0:
        
            self.parsing()
        
            self.opt_stms(self.parsedarray)
            
            self.commands=self.definevariables(self.commands)
        
        return self.commands
        
    def showvariables(self): #it returns the variables of the input
        
        if len(self.commands)==0:
            
            self.parsing()
        
            self.opt_stms(self.parsedarray)
        
        return self.variables
        
    def definevariables(self,myarray): #adds commands for defining variables at the beggining of the code
        
        vararray=[]
        
        for i in self.variables:
            
            vararray.append(str(i) + " dw 0")
            
        myarray=vararray+myarray
        
        myarray.append("RET")
        
        return myarray
        
    def parsing(self): #It parses the whole inputs, seperates the integers, expressions, variables and statements and puts them in an array
    
        myarray=self.mystring.split()
        
        self.parsedarray=[]
        
        flag_previous="" #Boolean for previous token if it is integer, statement or noninteger
        flag_current="" #Boolean for current token if it is integer, statement or noninteger
        
        par_counter1=0
        par_counter2=0
        
        for array in myarray:
            
            try:
                        
                int(array) #Look if the element is an integer
                
                self.parsedarray+=[array]
                        
                flag_current="int"
                        
            except ValueError:
            
                if array=="print" or array=="if" or array=="then" or array=="while" or array=="do" or array=="begin" or array=="end" or array==":=": #Look if the element is an statement
                    
                    self.parsedarray+=[array]
                    
                    flag_current="statement"
                    
                elif array=="+" or array=="-" or array=="*" or array=="/" or array=="mod" or array=="(" or array==")": #Look if the element is an noninteger
                    
                    self.parsedarray+=[array]
                    
                    flag_current="notint"
                    
                else:
            
                    for i in range(len(array)):  #Look all tokens of the element and distinguish them by being an integer, statement, variable or expression
                        
                        flag_previous=flag_current
                        
                        try:
                            
                            int(array[i])
                            
                            flag_current="int"
                            
                        except ValueError:
                            
                            flag_current="notint"
                        
                        if flag_previous=="int" and flag_current=="notint":
                            
                            self.parsedarray+=array[i]
                        
                        elif  flag_previous=="int" and flag_current=="statement":
                            
                            self.parsedarray+=array[i]
                                
                        elif flag_previous=="int" and flag_current=="int":
                            
                            self.parsedarray[-1]=self.parsedarray[-1]+array[i]
                        
                        elif flag_previous=="notint" and flag_current=="int":
                            
                            if self.parsedarray[-1]=="+" or self.parsedarray[-1]=="-" or self.parsedarray[-1]=="*" or self.parsedarray[-1]=="/" or self.parsedarray[-1]=="(" or self.parsedarray[-1]==":=" or self.parsedarray[-1]=="mod":
                            
                                self.parsedarray+=array[i]
                                
                            else:
                                
                                self.parsedarray[-1]=self.parsedarray[-1]+array[i]
                            
                        elif flag_previous=="notint" and flag_current=="statement":
                            
                            if self.parsedarray[-1]=="print" or self.parsedarray[-1]=="if" or self.parsedarray[-1]=="then" or self.parsedarray[-1]=="while" or self.parsedarray[-1]=="do" or self.parsedarray[-1]=="begin" or self.parsedarray[-1]=="end" or self.parsedarray[-1]==":=":
                                
                                raise ValueError('Syntax Error.')
                            
                            elif self.parsedarray[-1]=="+" or self.parsedarray[-1]=="-" or self.parsedarray[-1]=="*" or self.parsedarray[-1]=="/" or self.parsedarray[-1]=="(" or self.parsedarray[-1]=="mod":
                            
                                raise ValueError('Syntax Error.')
                            
                            else:
                            
                                self.parsedarray+=array[i]
                                
                        elif flag_previous=="notint" and flag_current=="notint":
                            
                            if self.parsedarray[-1]==";" and array[i]==";":
                                
                                pass
                            
                            elif array[i]==";":
                                
                                self.parsedarray+=array[i]
                                
                                flag_previous=flag_current
                                
                            elif self.parsedarray[-1]==";":
                                
                                self.parsedarray+=array[i]
                                
                            elif array[i]=="+" or array[i]=="-" or array[i]=="*" or array[i]=="/" or array[i]=="mod":
                                
                                if self.parsedarray[-1]=="(" or self.parsedarray[-1]=="+" or self.parsedarray[-1]=="-" or self.parsedarray[-1]=="*" or self.parsedarray[-1]=="/" or self.parsedarray[-1]=="mod":
                                    
                                    raise ValueError('Syntax Error.')
                                    
                                else:
                            
                                    self.parsedarray+=array[i]
                                    
                            elif array[i]==")":
                                
                                if self.parsedarray[-1]=="+" or self.parsedarray[-1]=="-" or self.parsedarray[-1]=="*" or self.parsedarray[-1]=="/" or self.parsedarray[-1]=="(" or self.parsedarray[-1]=="mod":
                                    
                                    raise ValueError('Syntax Error.')
                            
                                else:
                                    
                                    self.parsedarray+=array[i]
                                    
                            elif array[i]=="(":
                                
                                if self.parsedarray[-1]==")":
                                    
                                    raise ValueError('Syntax Error.')
                            
                                else:
                                    
                                    self.parsedarray+=array[i]
                            
                            elif array[i]=="=":
                                
                                if self.parsedarray[-1][-1]==":":
                                    
                                    if len(self.parsedarray[-1])==1:
                                    
                                        self.parsedarray[-1]=self.parsedarray[-1]+array[i]
                                    
                                    else:
                                        
                                        self.parsedarray[-1]=self.parsedarray[-1][:-1]
                                        
                                        self.parsedarray+=[":="]
                                        
                                        flag_current=="statement"
                                        
                                    if self.parsedarray[-2]=="print" or self.parsedarray[-2]=="if" or self.parsedarray[-2]=="then" or self.parsedarray[-2]=="while" or self.parsedarray[-2]=="do" or self.parsedarray[-2]=="begin" or self.parsedarray[-2]=="end" or self.parsedarray[-2]=="+" or self.parsedarray[-2]=="-" or self.parsedarray[-2]=="*" or self.parsedarray[-2]=="/" or self.parsedarray[-2]=="(" or self.parsedarray[-2]==")" or self.parsedarray[-2]==":=" or self.parsedarray[-2]=="mod":
                                            
                                            raise ValueError('Syntax Error.')
                                            
                                    try:
                                            
                                        int(self.parsedarray[-2])
                                            
                                        raise ValueError('Syntax Error.')
                                            
                                    except ValueError:
                                        
                                        pass
                                        
                                else:
                                    
                                    raise ValueError('Syntax Error.')
                                    
                            else:
                                
                                if self.parsedarray[-1]=="+" or self.parsedarray[-1]=="-" or self.parsedarray[-1]=="*" or self.parsedarray[-1]=="/" or self.parsedarray[-1]=="(" or self.parsedarray[-1]==")" or self.parsedarray[-1]==":=" or self.parsedarray[-1]=="mod" or self.parsedarray[-1]==";" or self.parsedarray[-1]=="print" or self.parsedarray[-1]=="if" or self.parsedarray[-1]=="then" or self.parsedarray[-1]=="do" or self.parsedarray[-1]=="begin" or self.parsedarray[-1]=="end":
                                    
                                    self.parsedarray+=array[i]
                                    
                                else:
                                    
                                    if i==0 and array[i]!=":": #for if it is a ':=' statement with no whitespace
                                    
                                        raise ValueError('Syntax Error.')
                                        
                                    else:
                                        
                                        self.parsedarray[-1]=self.parsedarray[-1]+array[i]
                                
                        elif flag_previous=="" and flag_current=="int":
                            
                            self.parsedarray+=array[i]
                            
                        elif flag_previous=="" and flag_current=="notint":
                            
                            self.parsedarray+=array[i]
                            
                        elif flag_previous=="" and flag_current=="statement":
                            
                            self.parsedarray+=array[i]
                            
                        elif flag_previous=="statement" and flag_current=="int":
                            
                            self.parsedarray+=array[i]
                        
                        elif flag_previous=="statement" and flag_current=="notint":
                            
                            if array[i]=="+" or array[i]=="-" or array[i]=="*" or array[i]=="/" or array[i]==")" or array[i]==":=" or array[i]=="mod":
                                
                                raise ValueError('Syntax Error.')
                                
                            else:
                            
                                self.parsedarray+=array[i]
                            
                        elif flag_previous=="statement" and flag_current=="statement":
                            
                            raise ValueError('Syntax Error.')
                        
                        else:
                            
                            raise ValueError('Syntax Error.')
                            
                        if array[i]=="(":
                            
                            par_counter1+=1
                        
                        elif array[i]==")":
                            
                            par_counter2+=1
                
        if par_counter1!=par_counter2:
                    
            raise ValueError('Syntax Error.')
            
#        print (self.parsedarray)
    
    def expr(self,myarray): #Look for the expressions in parsedarray
        
        token=0
        
        while token!=len(myarray):
            
            if myarray[token]=="(":
                
                parantesecount1=1
                
                parantesecount2=0
                
                while parantesecount1!=parantesecount2:
                    
                    token+=1
                    
                    if myarray[token]=="(":
                        
                        parantesecount1+=1
                        
                    elif myarray[token]==")":
                        
                        parantesecount2+=1
            
            elif myarray[token]=="*" or myarray[token]=="/" or myarray[token]=="mod":
                
                self.term(myarray,token)
                
                myarray[token]=" " #make the expression element blank to mark it has already processed
                
                myarray[token-1]=" "
                
                myarray[token+1]=" "
                
                token+=1
                
            else:
                
                token+=1
                
        token=0
            
        while token!=len(myarray):
            
            if myarray[token]=="(":
                
                parantesecount1=1
                
                parantesecount2=0
                
                while parantesecount1!=parantesecount2:
                    
                    token+=1
                    
                    if myarray[token]=="(":
                        
                        parantesecount1+=1
                        
                    elif myarray[token]==")":
                        
                        parantesecount2+=1
            
            elif myarray[token]=="+" or myarray[token]=="-":
                
                self.term(myarray,token)
                
                self.moreterms(myarray,token)
                
                myarray[token]=" " #make the expression element blank to mark it has already processed
                
                myarray[token+1]=" "
                
                myarray[token-1]=" "
                
                token+=1
                
            else:
                
                token+=1
        
        if len(myarray)==1: #if the expression is just an integer or variable
            
            try:
                
                int(myarray[0])
                
                self.commands.append("PUSH "+str(myarray[0]))
                
                return
                
            except ValueError:
                
                if myarray[0] in self.variables:
            
                    self.commands.append("PUSH "+str(myarray[0]))
                    
                    return
                    
                else:
                    
                    raise ValueError('Variable is not assigned.')
        
        elif myarray[0]=="(" and myarray[-1]==")":
            
            myarray=myarray[1:-1]
            
            self.expr(myarray)
            
            return
                
    def term(self,myarray,token): #it calls factor function for the element before the expression element and morefactor function for the expression element
            
        self.factor(myarray,token-1)
                
        self.morefactors(myarray,token)
            
    def moreterms(self,myarray,index): #it looks if the expression is '+' or '-', and adds necessary assembly code to the commands array

        if myarray[index]=="+":
            
            self.commands.append("POP BX")
            
            self.commands.append("POP AX")
            
            self.commands.append("ADD AX,BX")
            
            self.commands.append("PUSH AX")
        
        elif myarray[index]=="-":
            
            self.commands.append("POP BX")
            
            self.commands.append("POP AX")
            
            self.commands.append("SUB AX,BX")
            
            self.commands.append("PUSH AX")
            
    def factor(self,myarray,index): #it looks for the element if it is an integer, variable or parantese. If it is a parantese it calls expr function for inside of the paranteses.
                                    #then it adds necessary assembly code to the commands array
        try:
                
            int(myarray[index])
            
            self.commands.append("PUSH "+str(myarray[index]))
            
        except ValueError:
            
            if myarray[index]=="(":
                
                temp_array=[]
                
                parantesecount1=1
                
                parantesecount2=0
                
                token=index
                
                myarray[token]=" "
                
                while parantesecount1!=parantesecount2:
                    
                    token+=1
                    
                    if myarray[token]==")":
                        
                        parantesecount2+=1
                        
                    if myarray[token]=="(":
                        
                        parantesecount1+=1
                        
                    if parantesecount1==parantesecount2:
                        
                        break
                    
                    temp_array.append(myarray[token])
                    
                    myarray[token]=" "
                    
                myarray[token]=" "
                        
                self.expr(temp_array)
                
            elif myarray[index]==")":
                
                temp_array=[]
                
                parantesecount1=1
                
                parantesecount2=0
                
                token=index
                
                myarray[token]=" "
                
                while parantesecount1!=parantesecount2:
                    
                    token-=1
                    
                    if myarray[token]=="(":
                        
                        parantesecount2+=1
                        
                    if myarray[token]==")":
                        
                        parantesecount1+=1
                        
                    if parantesecount1==parantesecount2:
                        
                        break
                    
                    temp_array.append(myarray[token])
                        
                    myarray[token]=" "
                    
                myarray[token]=" "
                        
                self.expr(temp_array[::-1])
                
            elif myarray[index] in self.variables:
                
                self.commands.append("PUSH "+str(myarray[index]))
                
            elif myarray[index]==" ":
                
                pass
                
            else:
                
                raise ValueError('Variable is not assigned.')
    
    def morefactors(self,myarray,index):  #it looks if the expression is '*', '/' or 'mod', if it is, it calls factor element for the previous element and adds necessary assembly code to the commands array
        
        if myarray[index]=="*":
            
            self.factor(myarray,index+1)
            
            self.commands.append("POP BX")
            
            self.commands.append("POP AX")
            
            self.commands.append("IMUL BX")
            
            self.commands.append("PUSH AX")
        
        elif myarray[index]=="/":
            
            self.factor(myarray,index+1)
            
            self.funcno+=1
            
            self.commands.append("POP BX")
            
            self.commands.append("POP AX")
            
            self.commands.append("TEST AX,AX")
            
            self.commands.append("JNS posdiv" + str(self.funcno))
            
            self.commands.append("NEG AX")
            
            self.commands.append("NEG BX")
            
            self.commands.append("posdiv" + str(self.funcno) + ":")
            
            self.commands.append("XOR DX,DX")
            
            self.commands.append("IDIV BX")
            
            self.commands.append("PUSH AX")
            
        elif myarray[index]=="mod":
            
            self.factor(myarray,index+1)
            
            self.commands.append("POP BX")
            
            self.commands.append("POP AX")

            self.commands.append("XOR DX,DX")
                        
            self.commands.append("DIV BX")
            
            self.commands.append("PUSH DX")
            
        elif myarray[index]=="+": #if the expression element is '+', it only calls factor element for the previous element.
            
            self.factor(myarray,index+1)
            
        elif myarray[index]=="-": #if the expression element is '-', it only calls factor element for the previous element.
            
            self.factor(myarray,index+1)
            
    def opt_stms(self,myarray): #it looks for the statements in the parsedarray. If there is no statement, it raises an error.
        
        correct=False
        
        for index in range(len(myarray)):
            
            if self.stmt_list(myarray,index)==True:
            
                correct=True
            
        if correct!=True:
            
            raise ValueError('Syntax Error.')
            
    def stmt_list(self,myarray,index): #it looks for the statements in the parsedarray and calls the stm function if there is one.
        
        if myarray[index]=="print" or myarray[index]=="if" or myarray[index]=="then" or myarray[index]=="while" or myarray[index]=="do" or myarray[index]=="begin" or myarray[index]=="end" or myarray[index]==":=":
            
            self.stm(myarray,index)
            
            return True
        
        else:
            
            return False
            
    def stm(self,myarray,index): #it looks the element and distinguish which statement it is.Then it adds necessary assembly code to the commands array and make the statement element blank to mark it has already processed
            
        if myarray[index]==":=":
            
            myarray[index]=" "
            
            temp_array=[]
            
            for i in range(index+1,len(myarray)):
                
                if myarray[i]=="print" or myarray[i]=="if" or myarray[i]=="then" or myarray[i]=="while" or myarray[i]=="do" or myarray[i]=="begin" or myarray[i]=="end" or myarray[i]==":=":
                    
                    raise ValueError('Syntax Error.')
                
                elif myarray[i]==";":
                                            
                    break
                
                else:
                    
                    temp_array.append(myarray[i])
                    
            if len(temp_array)==0:
                
                raise ValueError('Syntax Error.')
                
            self.expr(temp_array)
            
            self.commands.append("POP AX")
            
            self.commands.append("MOV [" + str(myarray[index-1]) + "],AX")
            
            if myarray[index-1] not in self.variables:
                
                self.variables.append(str(myarray[index-1]))
            
        elif myarray[index]=="print":
            
            myarray[index]=" "
            
            temp_array=[]
            
            self.funcno+=1
            
            for i in range(index+1,len(myarray)):
                
                if myarray[i]=="print" or myarray[i]=="if" or myarray[i]=="then" or myarray[i]=="while" or myarray[i]=="do" or myarray[i]=="begin" or myarray[i]=="end" or myarray[i]==":=":
                    
                    raise ValueError('Syntax Error.')
                
                elif myarray[i]==";":
                                            
                    break
                
                else:
                    
                    temp_array.append(myarray[i])
                    
            if len(temp_array)==0:
                
                raise ValueError('Syntax Error.')
                
            self.expr(temp_array)
            
            self.commands.append("POP AX")
            
            self.commands.append("TEST AX,AX")
            
            self.commands.append("JNS nonneg" + str(self.funcno))
            
            self.commands.append("PUSH AX")
            
            self.commands.append("MOV DX,'-'")
            
            self.commands.append("MOV AH,02h")
            
            self.commands.append("INT 21h")
            
            self.commands.append("POP AX")
            
            self.commands.append("NEG AX")
            
            self.commands.append("nonneg" + str(self.funcno) + ":")
            
            self.commands.append("MOV SI,10d")
            
            self.commands.append("XOR DX,DX")
            
            self.commands.append("MOV CX,0")
            
            self.commands.append("nonzero" + str(self.funcno) + ":")
            
            self.commands.append("DIV SI")
            
            self.commands.append("ADD DX,48d")
            
            self.commands.append("PUSH DX")
            
            self.commands.append("INC CX")
            
            self.commands.append("XOR DX,DX")
            
            self.commands.append("CMP AX,0h")
            
            self.commands.append("JNE nonzero" + str(self.funcno))
            
            self.commands.append("writeloop" + str(self.funcno) + ":")
            
            self.commands.append("POP DX")
            
            self.commands.append("MOV AH,02h")
            
            self.commands.append("INT 21h")
            
            self.commands.append("DEC CX")
            
            self.commands.append("JNZ writeloop" + str(self.funcno))
            
            self.commands.append("MOV DX,' '")
            
            self.commands.append("MOV AH,02h")
            
            self.commands.append("MOV DX,0 ")
            
            self.commands.append("INT 21h")
            
        elif myarray[index]=="if":
            
            myarray[index]=" "
            
            temp_array=[]
            
            self.funcno+=1
            
            funcno=self.funcno
            
            stm_index=0
            
            correct=False
            
            for i in range(index+1,len(myarray)):
                
                if myarray[i]=="print" or myarray[i]=="if" or myarray[i]==";" or myarray[i]=="while" or myarray[i]=="do" or myarray[i]=="begin" or myarray[i]=="end" or myarray[i]==":=":
                    
                    raise ValueError('Syntax Error.')
                
                elif myarray[i]=="then":
                    
                    myarray[i]=" "
                    
                    stm_index=i
                    
                    correct=True
                                            
                    break
                
                else:
                    
                    temp_array.append(myarray[i])
                    
                    stm_index=i
                
            self.expr(temp_array)
            
            self.commands.append("POP AX")
            
            self.commands.append("CMP AX,0")
            
            self.commands.append("JZ outlabel" + str(funcno))
                
            if myarray[stm_index+1]==";":
                
                if myarray[stm_index+2]=="print" or myarray[stm_index+2]=="if" or myarray[stm_index+2]=="while" or myarray[stm_index+2]=="begin":
                    
                    self.stm(myarray,stm_index+2)
                    
                elif myarray[stm_index+3]==":=":
                    
                    self.stm(myarray,stm_index+3)
                    
                else:
                    
                    raise ValueError('Syntax Error.')
            
            elif myarray[stm_index+1]=="print" or myarray[stm_index+1]=="if" or myarray[stm_index+1]=="while" or myarray[stm_index+1]=="begin":
                
                self.stm(myarray,stm_index+1)
                
            elif myarray[stm_index+2]==":=":
            
                self.stm(myarray,stm_index+2)
                
            else:
                
                raise ValueError('Syntax Error.')
                
            self.commands.append("outlabel" + str(funcno) + ":")
            
        elif myarray[index]=="while":
            
            myarray[index]=" "
            
            temp_array=[]
            
            self.funcno+=1
            
            funcno=self.funcno
            
            stm_index=0
            
            correct=False
            
            self.commands.append("testlabel" + str(funcno) + ":")
            
            for i in range(index+1,len(myarray)):
                
                if myarray[i]=="print" or myarray[i]=="if" or myarray[i]=="then" or myarray[i]=="while" or myarray[i]==";" or myarray[i]=="begin" or myarray[i]=="end" or myarray[i]==":=":
                    
                    raise ValueError('Syntax Error.')
                
                elif myarray[i]=="do":
                    
                    myarray[i]=" "
                    
                    stm_index=i
                    
                    correct=True
                                            
                    break
                
                else:
                    
                    temp_array.append(myarray[i])
                    
                    stm_index=i
                
            self.expr(temp_array)
            
            self.commands.append("POP AX")
            
            self.commands.append("CMP AX,0")
            
            self.commands.append("JZ outlabel" + str(funcno) + ":")
                
            if myarray[stm_index+1]==";":
                
                if myarray[stm_index+2]=="print" or myarray[stm_index+2]=="if" or myarray[stm_index+2]=="while" or myarray[stm_index+2]=="begin":
                    
                    self.stm(myarray,stm_index+2)
                    
                elif myarray[stm_index+3]==":=":
                    
                    self.stm(myarray,stm_index+3)
                    
                else:
                    
                    raise ValueError('Syntax Error.')
            
            elif myarray[stm_index+1]=="print" or myarray[stm_index+1]=="if" or myarray[stm_index+1]=="while" or myarray[stm_index+1]=="begin":
                
                self.stm(myarray,stm_index+1)
                
            elif myarray[stm_index+2]==":=":
            
                self.stm(myarray,stm_index+2)
                
            else:
                
                raise ValueError('Syntax Error.')
                
            self.commands.append("JMP testlabel" + str(funcno))
            
            self.commands.append("outlabel" + str(funcno) + ":")
            
        elif myarray[index]=="begin": #if the statement is a 'begin', it calls opt_stms function for inside of the 'begin' and 'end' statements
            
            myarray[index]=" "
            
            temp_array=[]
            
            counter_begin=1
            
            counter_end=0
            
            correct=False
            
            for i in range(index+1,len(myarray)):
                
                if myarray[i]=="end":
                    
                    counter_end+=1
                    
                    if counter_begin==counter_end:
                        
                        myarray[i]=" "
                        
                        correct=True
                        
                        break
                    
                    else:
                    
                        temp_array.append(myarray[i])
                        
                        myarray[i]=" "
                    
                    
                elif myarray[i]=="begin":
                    
                    counter_begin+=1
                    
                    temp_array.append(myarray[i])
                    
                    myarray[i]=" "
                
                else:
                    
                    temp_array.append(myarray[i])
                    
                    myarray[i]=" "
                    
            if correct!=True:
                
                raise ValueError('Syntax Error.')
            
            self.opt_stms(temp_array)
            
        elif myarray[index]=="then" or myarray[index]=="do" or myarray[index]=="end":
            
            raise ValueError('Syntax Error.')





myinput=input("Please type your input file with extension in the program directory.\n\n")

f = open(myinput,"r")

y=assembly(f.read().lower().replace("\t"," ").replace("\n",";"))

#print (y.showcommands())

#print (y.showvariables())

#print (y.parsedarray)

for i in range(len(myinput)):
    
    if myinput[i]==".":
        
        myinput=myinput[:i]
        
        break

file = open(myinput + ".asm","w")

for line in y.showcommands():

    file.write(line)
    
    file.write("\n")

f.close()

file.close()

print ("\n.asm file is created.")


