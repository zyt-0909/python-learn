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
    if (player_choice!="ʯͷ")and(player_choice!="ʷ����")and(player_choice!="ֽ")and(player_choice!="����")and(player_choice!="����"):
        print("Error: No Correct Name")         #�������Ĳ�����Ϸ������ݣ������Ѵ���
    else:
        print("����ѡ��Ϊ"+player_choice)         # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

        number=name_to_number(player_choice)          # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

        comp_number=random.randrange(0,4,1)         # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

        computer_choice=number_to_name(comp_number)  # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

        print("�����ѡ����"+computer_choice)  # ����Ļ����ʾ�����ѡ����������
        
        if number==comp_number:
            print("���ͼ��������һ����")             #����һ�������
            
        elif (number==0 and comp_number==3)or(number==0 and comp_number==4)or(number==1 and comp_number==0)or(number==1 and comp_number==4)or(number==2 and comp_number==0)or(number==2 and comp_number==1)or(number==3 and comp_number==1)or(number==3 and comp_number==2)or(number==4 and comp_number==2)or(number==4 and comp_number==3):
            print("��Ӯ��")                         #���Ӯ���������
            
        else:
            print("�����Ӯ��")                        #�����Ӯ�����
        

    
    
    
   
                                                   # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

                                                 # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
player_choice=input("���������ѡ��")

rpsls(player_choice)


