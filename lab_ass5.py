# # Simple CPU instruction interpreter. Direct instruction interpretation.
# # Class 0: no operand NOP
# # Class 1: register,literal LDRL r2,1
# # Class 2: register,register MOV r1,r2
# # Class 3: register,[register] LDRI r1,[r2]

# #1
# sfile = ['LDRL r2,1','LDRL r0,4','NOP','STRI r0,[r2]','LDRI r3,[r2]', 'MOV r1,r2','STOP']

# codes = {'NOP':[0],'STOP':[0],'LDRL':[1],'MOV':[2],'LDRI':[3],'STRI':[3]}
# reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}
# reg2 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}
# r = [0] * 4
# r[0],r[1],r[2],r[3] = 1,2,3,4
# m = [0] * 8
# pc = 0
# go = 1
# z = 0
# while go == 1:
#     thisline = sfile[pc]
#     pc = pc+1
#     pcOld = pc
#     temp = thisline.replace(',',' ')
#     print(temp)
#     tokens = temp.split(' ')
#     mnemonic = tokens[0]
#     opClass = codes[mnemonic][0]
#     print(f'opcode Class:{opClass}')
    
#     rD, rDval, rS1, rS1val, rS2, rS2val, lit, rPnt, rPntv = 0,0,0,0,0,0,0,0,0

#     if opClass in [0]:
#         pass
    
#     if opClass in [1,2,3]:
#         rD = reg1[tokens[1]]
#         print(f'Destination Register:{rD}')
#         rDval = r[rD]
        
#     if opClass in [1]:
#         lit = int(tokens[-1])
#         print(f'literal is:{lit}')
            
#     if opClass in [2]:
#         rS1 = reg1[tokens[2]]
#         print(f'rS1 register number and then contents')
        
#     if opClass in [3]:
#         rPntv = r[rPnt]
#         if mnemonic == 'STOP':
#             go = 0
#             print('Program terminated')
#         elif mnemonic == 'NOP':
#             pass
#         elif mnemonic == 'MOV':
#             r[rD] = rS1val
#         elif mnemonic == 'LDRL':
#             r[rD] = lit
#         elif mnemonic == 'LDRI':
#             r[rD] = m[rPntv]
#         elif mnemonic == 'STRI':
#             m[rPntv] = rDval
        
#         regs = ''.join('%02x' % b for b in r)
#         mem = ' '.join('%02x' % b for b in m)
#         print('pc =','{:<3}'.format(pcOld), '{:<14}'.format(thisline), 'Regs =', regs, 'Mem =', mem, 'Z = ', z)
#         x = input('>>> ')

#2
sfile = ['LDRL r2,1','LDRL r0,4','NOP','STRI r0,[r2]','LDRI r3,[r2]', 'MOV r1,r2','STOP']

codes = {'NOP':[0],'STOP':[0],'LDRL':[1],'MOV':[2],'LDRI':[3],'STRI':[3],'ADDI':[1],'INC':[1],'DEC':[2],'CMP':[1],'BRA':[3],'BRE':[1],'BRN':[1],'ADD':[5],'SUB':[5],'MUL':[5],'AND':[5],'OR':[5]}

reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}
reg2 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}
reg3 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}

m = [0] * 8
r = [0] * 4
r[0],r[1],r[2],r[3] = 1,2,3,4
pc = 0
go = 1
z = 0

while go == 1:
    thisline = sfile[pc]
    pc = pc + 1
    pcOld = pc
    temp = thisline.replace(',',' ')
    print(temp)
    tokens = temp.split(' ')
    mnemonic = tokens[0]
    opClass = codes[mnemonic][0]
    print(f'opcode Class:{opClass}')
    
    rD, rDval, rS1, rS1val, rS2, rS2val, lit, rPnt, rPntv = 0,0,0,0,0,0,0,0,0
    
    if opClass in [0]:
        pass
    
    if opClass in [1,2,3]:
        rD = reg1[tokens[1]]
        print(f'Destination Register:{rD}')
        rDval = r[rD]
    
    if opClass in [1]:
        lit = int(tokens[-1])
        print(f'literal is:{lit}')
    
    if opClass in [2]:
        rS1 = reg1[tokens[2]]
        print(f'rS1 register number and then contents')
    
    if opClass in [3]:
        rPnt = reg1[tokens[2]]
        rPntv = r[rPnt]
        if mnemonic == 'STOP':
            go = 0
            print('Program terminated')
        elif mnemonic == 'NOP':
            pass
        elif mnemonic == 'MOV':
            r[rD] = rS1val
        elif mnemonic == 'LDRL':
            r[rD] = lit
        elif mnemonic == 'LDRI':
            r[rD] = m[rPntv]
        elif mnemonic == 'STRI':
            m[rPntv] = rDval
    
    regs = ''.join('%02x' % b for b in r)
    mem = ' '.join('%02x' % b for b in m)
    print(f'pc =','{:<3}'.format(pcOld), '{:<14}'.format(thisline), 'Regs =', regs, 'Mem =', mem, 'Z = ', z)
    x = input('>>> ')