#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        return "Error: No Correct Name"


    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��



def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    elif number==4:
        return "����"

	    

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    


    print("-------- ")                          # ���"-------- "���зָ�
    print("����ѡ��Ϊ"+player_choice)         # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    number=name_to_number(player_choice)          # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    comp_number=random.randrange(0,4,1)         # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    computer_choice=number_to_name(comp_number)  # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    print("�����ѡ����"+computer_choice)  # ����Ļ����ʾ�����ѡ����������

    if comp_number==4 and number==2:
        print("�����Ӯ��")
    elif comp_number==2 and number==0:
        print("�����Ӯ��")
    elif comp_number==0 and number==4:
        print("�����Ӯ��")
    elif comp_number==0 and number==3:
        print("�����Ӯ��")
    elif comp_number==3 and number==1:
        print("�����Ӯ��")
    elif comp_number==1 and number==4:
        print("�����Ӯ��")
    elif comp_number==1 and number==0:
        print("�����Ӯ��")
    elif comp_number==4 and number==3:
        print("�����Ӯ��")  
    elif comp_number==2 and number==1:
        print("�����Ӯ��")
    elif comp_number==3 and number==2:
        print("�����Ӯ��")                                     
    elif number==4 and comp_number==2:
        print("��Ӯ��")
    elif number==2 and comp_number==0:
        print("��Ӯ��")
    elif number==0 and comp_number==4:
        print("��Ӯ��")
    elif number==0 and comp_number==3:
        print("��Ӯ��")        
    elif number==3 and comp_number==1:
        print("��Ӯ��")
    elif number==1 and comp_number==4:
        print("��Ӯ��")
    elif number==1 and comp_number==0:
        print("��Ӯ��")
    elif number==4 and comp_number==3:
        print("��Ӯ��")
    elif number==2 and comp_number==1:
        print("��Ӯ��")
    elif number==3 and comp_number==2:
        print("��Ӯ��")                                       
    elif comp_number==number:
        print("���ͼ��������һ����") 
    
    
   
                                                   # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

                                                 # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("���������ѡ��")

rpsls(player_choice)


