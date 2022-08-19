#hanoi_tower

import numpy as np


def top_3_n(col1,col2,col3):

    #top number for each column

    primo_col2=0
    primo_col1=0
    primo_col3=0
    for i in range(len(col1)):
        if col1[i] !=0:  
            primo_col1=col1[i]
            break
    for i in range(len(col2)):
        if col2[i] !=0:
            primo_col2=col2[i]
            break
    for i in range(len(col3)):
        if col3[i] !=0:
            primo_col3=col3[i]
            break   
    return primo_col1,primo_col2,primo_col3


def moving(n1,n2,n3,p_o_d,col1,col2,col3,prev_move):

    #which number to move?
    m_n1=2
    m_n2=2
    m_n3=2
    if p_o_d=='p' and n1%2==0 and n1!=prev_move and n1!=0:
        m_n1=1

    if p_o_d=='d' and n1%2!=0 and n1!=prev_move and n1!=0:
        m_n1=1

    if p_o_d=='p' and n2%2==0 and n2!=prev_move and n2!=0:
        m_n2=1

    if p_o_d=='d' and n2%2!=0 and n2!=prev_move and n2!=0:
        m_n2=1

    if p_o_d=='p' and n3%2==0 and n3!=prev_move and n3!=0:
        m_n3=1

    if p_o_d=='d' and n3%2!=0 and n3!=prev_move and n3!=0:
        m_n3=1


    if n1!=0 and n2!=0 and n3!=0 and n1 == max(n1, n2,n3) and ((m_n1==1 and m_n2==1) or (m_n1==1 and m_n3==1) or (m_n2==1 and m_n3==1)):
        m_n1=2
    if n1!=0 and n2!=0 and n3!=0 and n2 == max(n1, n2,n3) and ((m_n1==1 and m_n2==1) or (m_n1==1 and m_n3==1) or (m_n2==1 and m_n3==1)):
        m_n2=2
    if n1!=0 and n2!=0 and n3!=0 and n3 == max(n1, n2,n3) and ((m_n1==1 and m_n2==1) or (m_n1==1 and m_n3==1) or (m_n2==1 and m_n3==1)):
        m_n3=2
    
    #where to move the number ?
    move_1on2=2
    move_1on3=2
    move_2on1=2
    move_2on3=2
    move_3on1=2
    move_3on2=2
    if m_n1 ==1 and p_o_d=='p' and ((n2%2!=0 and n2>n1) or n2==0) :
        move_1on2=1

    if m_n1 ==1 and p_o_d=='d' and ((n2%2==0 and n2>n1) or n2==0) :
        move_1on2=1

    if m_n1 ==1 and p_o_d=='p' and ((n3%2!=0 and n3>n1) or n3==0) :
        move_1on3=1

    if m_n1 ==1 and p_o_d=='d' and ((n3%2==0 and n3>n1) or n3==0) :
        move_1on3=1

    if m_n2 ==1 and p_o_d=='p' and ((n1%2!=0 and n1>n2) or n1==0) :
        move_2on1=1

    if m_n2 ==1 and p_o_d=='d' and ((n1%2==0 and n1>n2) or n1==0) :
        move_2on1=1

    if m_n2 ==1 and p_o_d=='p' and ((n3%2!=0 and n3>n2) or n3==0) :
        move_2on3=1

    if m_n2 ==1 and p_o_d=='d' and ((n3%2==0 and n3>n2) or n3==0) :
        move_2on3=1

    if m_n3 ==1 and p_o_d=='p' and ((n1%2!=0 and n1>n3) or n1==0) :
        move_3on1=1

    if m_n3 ==1 and p_o_d=='d' and ((n1%2==0 and n1>n3) or n1==0) :
        move_3on1=1

    if m_n3 ==1 and p_o_d=='p' and ((n2%2!=0 and n2>n3) or n2==0) :
        move_3on2=1

    if m_n3 ==1 and p_o_d=='d' and ((n2%2==0 and n2>n3) or n2==0) :
        move_3on2=1

    if move_1on2 == move_3on2 and n3>n1:
        move_1on2=2
    if move_1on2 == move_3on2 and n3<n1:
        move_3on2=2

    if move_2on1 == move_3on1 and n3>n2:
        move_2on1=2
    if move_2on1 == move_3on1 and n3<n2:
        move_3on1=2

    if move_2on3 == move_1on3 and n1>n2:
        move_2on3=2
    if move_2on3 == move_1on3 and n1<n2:
        move_1on3=2

# 1on2 or 1on3
    if move_1on2 == move_1on3 and p_o_d=='p' and n3!=0 and n3%2!=0:
        move_1on2=2
    if move_1on2 == move_1on3 and p_o_d=='p' and n2!=0 and n2%2!=0:
        move_1on3=2
    if move_1on2 == move_1on3 and p_o_d=='p' and n3!=0 and n3%2==0:
        move_1on3=2
    if move_1on2 == move_1on3 and p_o_d=='p' and n2!=0 and n2%2==0:
        move_1on2=2
    if move_1on2 == move_1on3 and p_o_d=='d' and n3!=0 and n3%2!=0:
        move_1on3=2
    if move_1on2 == move_1on3 and p_o_d=='d' and n2!=0 and n2%2!=0:
        move_1on2=2
    if move_1on2 == move_1on3 and p_o_d=='d' and n3!=0 and n3%2==0:
        move_1on2=2
    if move_1on2 == move_1on3 and p_o_d=='d' and n2!=0 and n2%2==0:
        move_1on3=2

# 2on1 or 2on3
    if move_2on1 == move_2on3 and p_o_d=='p' and n3!=0 and n3%2!=0:
        move_2on1=2
    if move_2on1 == move_2on3 and p_o_d=='p' and n1!=0 and n1%2!=0:
        move_2on3=2
    if move_2on1 == move_2on3 and p_o_d=='p' and n3!=0 and n3%2==0:
        move_2on3=2
    if move_2on1 == move_2on3 and p_o_d=='p' and n1!=0 and n1%2==0:
        move_2on1=2
    if move_2on1 == move_2on3 and p_o_d=='d' and n3!=0 and n3%2!=0:
        move_2on3=2
    if move_2on1 == move_2on3 and p_o_d=='d' and n1!=0 and n1%2!=0:
        move_2on1=2
    if move_2on1 == move_2on3 and p_o_d=='d' and n3!=0 and n3%2==0:
        move_2on1=2
    if move_2on1 == move_2on3 and p_o_d=='d' and n1!=0 and n1%2==0:
        move_2on3=2

    # 3on1 or 3on2
    if move_3on1 == move_3on2 and p_o_d=='p' and n2!=0 and n2%2!=0:
        move_3on1=2
    if move_3on1 == move_3on2 and p_o_d=='p' and n1!=0 and n1%2!=0:
        move_3on2=2
    if move_3on1 == move_3on2 and p_o_d=='p' and n2!=0 and n2%2==0:
        move_3on2=2
    if move_3on1 == move_3on2 and p_o_d=='p' and n1!=0 and n1%2==0:
        move_3on1=2
    if move_3on1 == move_3on2 and p_o_d=='d' and n2!=0 and n2%2!=0:
        move_3on2=2
    if move_3on1 == move_3on2 and p_o_d=='d' and n1!=0 and n1%2!=0:
        move_3on1=2
    if move_3on1 == move_3on2 and p_o_d=='d' and n2!=0 and n2%2==0:
        move_3on1=2
    if move_3on1 == move_3on2 and p_o_d=='d' and n1!=0 and n1%2==0:
        move_3on2=2

    #move the number

    if m_n1==1 and move_1on2==1 :
        col2[int(n1-1)]=n1
        col1[int(n1-1)]=0
        prev_move=n1
    if m_n1==1 and move_1on3==1 :
        col3[int(n1-1)]=n1
        col1[int(n1-1)]=0
        prev_move=n1

    if m_n2==1 and move_2on1==1 :
        col1[int(n2-1)]=n2
        col2[int(n2-1)]=0
        prev_move=n2
    if m_n2==1 and move_2on3==1 :
        col3[int(n2-1)]=n2
        col2[int(n2-1)]=0
        prev_move=n2

    if m_n3==1 and move_3on2==1 :
        col2[int(n3-1)]=n3
        col3[int(n3-1)]=0
        prev_move=n3
    if m_n3==1 and move_3on1==1 :
        col1[int(n3-1)]=n3
        col3[int(n3-1)]=0
        prev_move=n3

    return col1,col2,col3,prev_move


n=int(input('how tall u want ur tower to be ? '))
col1=np.linspace(1, n,n)
col2=np.zeros((n,1))
col3=np.zeros((n,1))
col_temp=np.zeros((n,1))
mat_game=[[col1],[col2],[col3]]
d=list('d')
p=list('p')
temp=list()
prev_move=1
mosse=0

    #list of moves

for i in range(1,n+1):
    if (i)%2!=0:
        temp=temp+d+temp
    else:
        temp=temp+p+temp
pd_list=[temp[i] for i in range(1,len(temp))]

    #first move 

if n%2!=0:
    col3[0]=col1[0]
    col1[0]=col_temp[0]
else:
    col2[0]=col1[0]
    col1[0]=col_temp[0]

    #other moves   
     
for i in pd_list:
    primo_col1,primo_col2,primo_col3=top_3_n(col1=col1,col2=col2,col3=col3)
    col1,col2,col3,prev_move=moving(int(primo_col1), int(primo_col2), int(primo_col3), i, col1, col2, col3, prev_move)
    mosse=mosse+1
mosse=mosse+1

print('colonna 3',col3,'numero di mosse',mosse)