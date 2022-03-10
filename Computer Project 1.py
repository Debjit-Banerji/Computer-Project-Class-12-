import mysql.connector as ms
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def Modify_Report_Card():
    global mc,a
    m=int(input("Enter the Student ID (whose data is to be modified): "))
    if m>=1 and m<=20:
        if a[0]=='T':
            b="select SUBJECT,SS,CLASS_TEACHER from t_details where ID="+str(a[1:])
            mc.execute(b)
            t=mc.fetchall()
            if t[0][2]!='NO':
                f=True
                while f:
                    print('---------------------------------------------------------------------------------------------------------------')
                    print('''\t\t\t\tMODIFY REPORT CARD
(Choose your preferred option by entering the number assigned beside the option)''')
                    print("\t\t1) Modify Comments")
                    print("\t\t2) Modify ",t[0][0]," Marks")
                    print("\t\t3) Main Menu")
                    print('---------------------------------------------------------------------------------------------------------------')
                    e=int(input("Enter your choice: "))
                    if e==1:
                        g=input("Enter new comments: ")
                        p="update std_details SET COMMENTS= "+g+" WHERE ID= "+m
                        mc.execute(p)
                        print("Comments Updated Successfully!!")
                    elif e==2:
                        f1=True
                        while f1:
                            print('---------------------------------------------------------------------------------------------------------------')
                            print('''\t\t\t\tMODIFY MARKS
(Choose your preferred option by entering the number assigned beside the option)''')
                            print("\t\t1) Modify PT-1 Marks")
                            print("\t\t2) Modify PT-2 Marks")
                            print("\t\t3) Modify Pre-Board Marks")
                            print("\t\t4) Return To Sub-Menu")
                            print('---------------------------------------------------------------------------------------------------------------')
                            q=int(input("Enter your choice: "))
                            if q==1:
                                g=input("Enter new "+t[0][0]+" marks: ")
                                p="UPDATE std_marks_T1 SET "+str(t[0][1])+"="+g+" WHERE ID= "+str(m)
                                mc.execute(p)
                                print("Marks Updated Successfully!!")
                            elif q==2:
                                g=input("Enter new "+t[0][0]+" marks: ")
                                p="UPDATE std_marks_T2 SET "+str(t[0][1])+"= "+g+" WHERE ID= "+str(m)
                                mc.execute(p)
                                print("Marks Updated Successfully!!")
                            elif q==3:
                                f2=True
                                while f2:
                                    print('---------------------------------------------------------------------------------------------------------------')
                                    print("\t\t\t1) Modify Theory Marks")
                                    print("\t\t\t2) Modify Practical Marks")
                                    print("\t\t\t3) Return To Sub-Menu")
                                    print('---------------------------------------------------------------------------------------------------------------')
                                    n=int(input("Enter your choice: "))
                                    if n==1:
                                        g=input("Enter new theory marks: ")
                                        p="update std_marks_PB SET "+str(t[0][1])+"T= "+g+" WHERE ID= "+str(m)
                                        mc.execute(p)
                                        print("Marks Updated Successfully!!")
                                    elif n==2:
                                        g=input("Enter new practical marks: ")
                                        p="update std_marks_PB SET "+str(t[0][1])+"P= "+g+" WHERE ID= "+str(m)
                                        mc.execute(p)
                                        print("Marks Updated Successfully!!")
                                    elif n==3:
                                        f2=False
                                    else:
                                        print("Oops!! Invalid Choice.\nPlease enter a valid choice.")
                            elif q==4:
                                f1=False
                            else:
                                print("Oops!! Invalid Choice.\nPlease enter a valid choice.")
                    elif e==3:
                        f=False
                        Teacher_Menu()
                    else:
                        print('Oops!! Invalid Choice.\nPlease enter a valid choice. (1 or 2 or 3)')                
            else:
                f=True
                while f:
                    print('---------------------------------------------------------------------------------------------------------------')
                    print('''\t\t\t\tMODIFY REPORT CARD
(Choose your preferred option by entering the number assigned beside the option)''')
                    print("\t\t1) Modify ",t[0][0]," Marks")
                    print("\t\t2) Main Menu")
                    print('---------------------------------------------------------------------------------------------------------------')
                    e=int(input("Enter your choice: "))
                    if e==1:
                        f1=True
                        while f1:
                            print('---------------------------------------------------------------------------------------------------------------')
                            print('''\t\t\t\tMODIFY MARKS
(Choose your preferred option by entering the number assigned beside the option)''')
                            print("\t\t1) Modify PT-1 Marks")
                            print("\t\t2) Modify PT-2 Marks")
                            print("\t\t3) Modify Pre-Board Marks")
                            print("\t\t4) Return To Sub-Menu")
                            print('---------------------------------------------------------------------------------------------------------------')
                            q=int(input("Enter your choice: "))
                            if q==1:
                                g=input("Enter new "+t[0][0]+" marks: ")
                                p="update std_marks_T1 SET "+str(t[0][1])+"= "+g+" WHERE ID= "+str(m)
                                mc.execute(p)
                                print("Marks Updated Successfully!!")
                            elif q==2:
                                g=input("Enter new "+t[0][0]+" marks: ")
                                p="update std_marks_T2 SET "+str(t[0][1])+"= "+g+" WHERE ID= "+str(m)
                                mc.execute(p)
                                print("Marks Updated Successfully!!")
                            elif q==3:
                                f2=True
                                while f2:
                                    print('---------------------------------------------------------------------------------------------------------------')
                                    print("\t\t1) Modify Theory Marks")
                                    print("\t\t2) Modify Practical Marks")
                                    print("\t\t3) Return To Sub-Menu")
                                    print('---------------------------------------------------------------------------------------------------------------')
                                    n=int(input("Enter your choice: "))
                                    if n==1:
                                        g=input("Enter new theory marks: ")
                                        p="update std_marks_PB SET "+str(t[0][1])+"T= "+g+" WHERE ID= "+str(m)
                                        mc.execute(p)
                                        print("Marks Updated Successfully!!")
                                    elif n==2:
                                        g=input("Enter new practical marks: ")
                                        p="update std_marks_PB SET "+str(t[0][1])+"P= "+g+" WHERE ID= "+str(m)
                                        mc.execute(p)
                                        print("Marks Updated Successfully!!")
                                    elif n==3:
                                        f2=False
                                    else:
                                        print("Oops!! Invalid Choice.\nPlease enter a valid choice.")
                            elif q==4:
                                f1=False
                            else:
                                print("Oops!! Invalid Choice.\nPlease enter a valid choice.")
                    elif e==2:
                        f=False
                        Teacher_Menu()
                    else:
                        print('Oops!! Invalid Choice.\nPlease enter a valid choice. (1 or 2)')
                
        elif a[0]=='A':
            f=True
            while f:
                print('---------------------------------------------------------------------------------------------------------------')
                print('''\t\t\t\tMODIFY REPORT CARD
(Choose your preferred option by entering the number assigned beside the option)''')
                print("\t\t1) Modify Student Biodata")
                print("\t\t2) Main menu")
                print('---------------------------------------------------------------------------------------------------------------')
                e=int(input("Enter your choice: "))
                if e==1:
                    g=int(input('Enter the Field Name to be updated:\nField Names: NAME, FATHERS_NAME, MOTHERS_NAME, ROLL_NO, SECTION, ATTENDANCE, CLASS_TEACHER, D_O_B'))
                    h=input("Enter the new data: ")
                    p="update std_details SET "+g+"= "+h+" WHERE ID= "+str(m)
                    mc.execute(p)
                    print("Biodata Updated Successfully!!")
                elif e==2:
                    f=False
                    Admin_Menu()
                else:
                    print('Oops!! Invalid Choice.\nPlease enter a valid choice(1 or 2)')
    else:
        print("Oops!! Invalid Student ID.\nPlease enter a valid Student ID.")
        Modify_Report_Card()

def Class_Toppers():
    global mc
    print('---------------------------------------------------------------------------------------------------------------')
    print("\tSubject Toppers:\n")
    b="select MAX(ENGTOT),MAX(MATHSTOT),MAX(PHYTOT),MAX(CHEMTOT),MAX(BIOTOT),MAX(CSTOT),MAX(PERCENTAGE) from std_marks_PB"
    mc.execute(b)
    t=mc.fetchall()
    j=0
    l=['ENGTOT','MATHSTOT','PHYTOT','CHEMTOT','BIOTOT','CSTOT']
    m=['English','Maths','Physics','Chemistry','Biology','Computer Science']
    for i in t[0]:
        if j!=6:
            d="select NAME,SECTION,PERCENTAGE from std_details,std_marks_PB where std_details.ID=std_marks_PB.ID AND "+l[j]+'='+str(i)
            mc.execute(d)
            t1=mc.fetchall()
            print("\t\t"+m[j]+"Topper:")
            print('\t\t\tName: ',t1[0][0],'\tClass and Section: XII -'+t1[0][1],'\tMarks: ',str(i),'\n')
        else:
            d="select NAME,SECTION,ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,BIOTOT,CSTOT from std_details,std_marks_PB where std_details.ID=std_marks_PB.ID AND PERCENTAGE="+str(i)
            mc.execute(d)
            t1=mc.fetchall()
            print('---------------------------------------------------------------------------------------------------------------')
            print("\n\tClass XII Overall Pre-Board Topper:\n")
            print("\t\tName: ",t1[0][0])
            print("\t\tClass and Section: XII-"+t1[0][1])
            print("\t\tEnglish Marks: ",t1[0][2])
            print("\t\tMaths Marks: ",t1[0][3])
            print("\t\tPhysics Marks: ",t1[0][4])
            print("\t\tChemistry Marks: ",t1[0][5])
            if t1[0][1]=='A':
                print("\t\tBiology Marks: ",t1[0][6])
                print("\t\tPercentage: ",str((t1[0][2]+t1[0][3]+t1[0][4]+t1[0][5]+t1[0][6])/5))
            elif t1[0][1]=='B':
                print("\t\tComputer Science Marks: ",t1[0][7])
                print("\t\tPercentage: ",str((t1[0][2]+t1[0][3]+t1[0][4]+t1[0][5]+t1[0][7])/5))
            print('---------------------------------------------------------------------------------------------------------------')
        j+=1

    c="select NAME,ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,BIOTOT,PERCENTAGE from std_details,std_marks_PB where std_details.ID=std_marks_PB.ID AND std_details.ID between 1 AND 10 AND PERCENTAGE=(select MAX(PERCENTAGE) from std_marks_PB where ID between 1 and 10)"
    mc.execute(c)
    t=mc.fetchall()
    print("\tClass XII-A Pr-Board Topper:\n")
    print("\t\tName: ",t[0][0])
    print("\t\tEnglish Marks: ",t[0][1])
    print("\t\tMaths Marks: ",t[0][2])
    print("\t\tPhysics Marks: ",t[0][3])
    print("\t\tChemistry Marks: ",t[0][4])
    print("\t\tBiology Marks: ",t[0][5])
    print("\t\tPercentage: ",str((t[0][1]+t[0][2]+t[0][3]+t[0][4]+t[0][5])/5))
    print('---------------------------------------------------------------------------------------------------------------')

    c="select NAME,ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,CSTOT,PERCENTAGE from std_details,std_marks_PB where std_details.ID=std_marks_PB.ID AND std_details.ID between 11 AND 20 AND PERCENTAGE=(select MAX(PERCENTAGE) from std_marks_PB where ID between 11 and 20)"
    mc.execute(c)
    t=mc.fetchall()
    print("\tClass XII-B Pre-Board Topper:\n")
    print("\t\tName: ",t[0][0])
    print("\t\tEnglish Marks: ",t[0][1])
    print("\t\tMaths Marks: ",t[0][2])
    print("\t\tPhysics Marks: ",t[0][3])
    print("\t\tChemistry Marks: ",t[0][4])
    print("\t\tComputer Science Marks: ",t[0][5])
    print("\t\tPercentage: ",str((t[0][1]+t[0][2]+t[0][3]+t[0][4]+t[0][5])/5))
    print('---------------------------------------------------------------------------------------------------------------')

    if a[0]=='S':
        Student_Menu()
    elif a[0]=='T':
        Teacher_Menu()
    elif a[0]=='A':
        Admin_Menu()

def Term_Wise_Individual_Performance():
    global mc,a
    if a[0]=='S':
        m=int(a[1:])
    else:
        f1=True
        while f1:
            m=int(input("Enter the Student ID: "))
            if m>=1 and m<=20:
                f1=False
            else:
                print("Oops!! Invalid Student ID entered.\n Please enter a valid Student ID")
        
    f=True
    while f:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print('''\t\t\t\tTERM-WISE PERFORMANCE
(Choose your preferred option by entering the number assigned beside the option)''')
        print("\t\t1) View Term-1 Performance")
        print("\t\t2) View Term-2 Performance")
        print("\t\t3) View Pre-Board Performance")
        print("\t\t4) Return to Sub-Menu")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        e=int(input("Enter your choice: "))
        if e==1:
            if m>=1 and m<=10:
                b="select ENG,MATHS,PHY,CHEM,BIO from std_marks_T1 where ID="+str(m)
                c="select MAX(ENG),AVG(ENG),MAX(MATHS),AVG(MATHS),MAX(PHY),AVG(PHY),MAX(CHEM),AVG(CHEM),MAX(BIO),AVG(BIO) from std_marks_T1"
                p=['English','Maths','Physics','Chemistry','Biology']
            elif m>=11 and m<=20:
                b="select ENG,MATHS,PHY,CHEM,CS from std_marks_T1 where ID="+str(m)
                c="select MAX(ENG),AVG(ENG),MAX(MATHS),AVG(MATHS),MAX(PHY),AVG(PHY),MAX(CHEM),AVG(CHEM),MAX(CS),AVG(CS) from std_marks_T1"
                p=['English','Maths','Physics','Chemistry','CS']
            v='Term-1 Performance'
        elif e==2:
            if m>=1 and m<=10:
                b="select ENG,MATHS,PHY,CHEM,BIO from std_marks_T2 where ID="+str(m)
                c="select MAX(ENG),AVG(ENG),MAX(MATHS),AVG(MATHS),MAX(PHY),AVG(PHY),MAX(CHEM),AVG(CHEM),MAX(BIO),AVG(BIO) from std_marks_T2"
                p=['English','Maths','Physics','Chemistry','Biology']
            elif m>=11 and m<=20:
                b="select ENG,MATHS,PHY,CHEM,CS from std_marks_T2 where ID="+str(m)
                c="select MAX(ENG),AVG(ENG),MAX(MATHS),AVG(MATHS),MAX(PHY),AVG(PHY),MAX(CHEM),AVG(CHEM),MAX(CS),AVG(CS) from std_marks_T2"
                p=['English','Maths','Physics','Chemistry','CS']
            v='Term-2 Performance'
        elif e==3:
            if m>=1 and m<=10:
                b="select ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,BIOTOT from std_marks_PB where ID="+str(m)
                c="select MAX(ENGTOT),AVG(ENGTOT),MAX(MATHSTOT),AVG(MATHSTOT),MAX(PHYTOT),AVG(PHYTOT),MAX(CHEMTOT),AVG(CHEMTOT),MAX(BIOTOT),AVG(BIOTOT) from std_marks_PB" 
                p=['English','Maths','Physics','Chemistry','Biology']
            elif m>=11 and m<=20:
                B="select ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,CSTOT from std_marks_PB where ID="+str(m)
                c="select MAX(ENGTOT),AVG(ENGTOT),MAX(MATHSTOT),AVG(MATHSTOT),MAX(PHYTOT),AVG(PHYTOT),MAX(CHEMTOT),AVG(CHEMTOT),MAX(CSTOT),AVG(CSTOT) from std_marks_PB"
                p=['English','Maths','Physics','Chemistry','CS']
            v='Pre-Board Performance'
        elif e==4:
            f=False
            Progress_Report()                
        else:
            print("Oops!! Invalid Choice.\nPlease enter a valid choice.")

        mc.execute(b)
        t1=mc.fetchall()
        mc.execute(c)
        t2=mc.fetchall()

        h=[t2[0][0],t2[0][2],t2[0][4],t2[0][6],t2[0][8]]
        y=[t1[0][0],t1[0][1],t1[0][2],t1[0][3],t1[0][4]]
        avg=[t2[0][1],t2[0][3],t2[0][5],t2[0][7],t2[0][9]]
        br1=np.arange(len(h))
        br2=[x+0.2 for x in br1]
        br3=[x+0.2 for x in br2]
        plt.bar(br1,h,color='r',width=0.2,label='Highest Marks')
        if a[0]=='S':
            plt.bar(br2,y,color='g',width=0.2,label='Your Marks')
        else:
            plt.bar(br2,y,color='g',width=0.2,label="Student's Marks")
        plt.bar(br3,avg,color='b',width=0.2,label='Average Marks')
        plt.xlabel('Subjects',fontweight='bold',fontsize='12')
        plt.ylabel('Marks',fontweight='bold',fontsize='12')
        plt.xticks([r+0.2 for r in range(len(h))],p)
        plt.legend()
        plt.title(v,fontweight='bold',fontsize='15')
        plt.show()

def Annual_Class_Performance():
    global mc,a
    if a[0]=='S':
        if a[1:]>='1' and a[1:]<='10':
            b="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T1 where ID between 1 AND 10"
            c="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T2 where ID between 1 AND 10"
            d="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_PB where ID between 1 AND 10"
            v='Section A Annual Performance'
        elif a[1:]>='11' and a[1:]<='20':
            b="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T1 where ID between 11 AND 20"
            c="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T2 where ID between 11 AND 20"
            d="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_PB where ID between 11 AND 20"
            v='Section B Annual Performance'
        p=['Term-1','Term-2','Pre-Board']    
        mc.execute(b)
        t1=mc.fetchall()
        mc.execute(c)
        t2=mc.fetchall()
        mc.execute(d)
        t3=mc.fetchall()
        h=list(t1[0])
        avg=list(t2[0])
        l=list(t3[0])
        br1=np.arange(len(h))
        br2=[x+0.2 for x in br1]
        br3=[x+0.2 for x in br2]

        plt.bar(br1,h,color='r',width=0.2,label='Highest Marks')
        plt.bar(br2,avg,color='g',width=0.2,label='Average Marks')
        plt.bar(br3,l,color='b',width=0.2,label='Lowest Marks')
        plt.xlabel('Exams',fontweight='bold',fontsize='12')
        plt.ylabel('Percentage',fontweight='bold',fontsize='12')
        plt.xticks([r+0.2 for r in range(len(h))],p)
        plt.legend()
        plt.title(v,fontweight='bold',fontsize='15')
        plt.show()
        Progress_Report()
    else:
        upper=['10','20']
        lower=['1','11']
        s=['A','B']
        for i in range(2):
            b="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T1 where ID between "+lower[i]+" AND "+upper[i]
            c="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_T2 where ID between "+lower[i]+" AND "+upper[i]
            d="select MAX(PERCENTAGE),AVG(PERCENTAGE),MIN(PERCENTAGE) from std_marks_PB where ID between "+lower[i]+" AND "+upper[i]
            p=['Term-1','Term-2','Pre-Board']    
            mc.execute(b)
            t1=mc.fetchall()
            mc.execute(c)
            t2=mc.fetchall()
            mc.execute(d)
            t3=mc.fetchall()
            h=list(t1[0])
            avg=list(t2[0])
            l=list(t3[0])
            br1=np.arange(len(h))
            br2=[x+0.2 for x in br1]
            br3=[x+0.2 for x in br2]

            plt.bar(br1,h,color='r',width=0.2,label='Highest Marks')
            plt.bar(br2,avg,color='g',width=0.2,label='Average Marks')
            plt.bar(br3,l,color='b',width=0.2,label='Lowest Marks')
            plt.xlabel('Exams',fontweight='bold',fontsize='12')
            plt.ylabel('Percentage',fontweight='bold',fontsize='12')
            plt.xticks([r+0.2 for r in range(len(h))],p)
            plt.legend()
            plt.title("Section "+s[i]+" Annual Performance",fontweight='bold',fontsize='15')
            plt.show()
        Progress_Report()

def Progress_Report():
    global a
    if a[0]=='S':
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print('''\t\t\t\tPROGRESS REPORT
(Choose your preferred option by entering the number assigned beside the option)''')
        print("\t\t\t1) View Term Wise Individual Peformance")
        print("\t\t\t2) View Annual Class Performance")
        print("\t\t\t3) Return Main Menu")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        check='f'
        while check=='f':
            b=int(input("Enter your preferred choice: "))
            if b==1:
                check='t'
                Term_Wise_Individual_Performance()
            elif b==2:
                check='t'
                Annual_Class_Performance()
            elif b==3:
                check='t'
                Student_Menu()
            else:   
                print("Oops!! Invalid Choice.\nPlease enter a valid choice.(1 or 2 or 3)")
    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print('''\t\t\t\tPROGRESS REPORT
(Choose your preferred option by entering the number assigned beside the option)''')
        print("\t\t\t1) View Term Wise Student Peformance")
        print("\t\t\t2) View Annual Class Performance")
        print("\t\t\t3) Return Main Menu")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        check='f'
        while check=='f':
            b=int(input("Enter your preferred choice: "))
            if b==1:
                check='t'
                Term_Wise_Individual_Performance()
            elif b==2:
                check='t'
                Annual_Class_Performance()
            elif b==3:
                check='t'
                if a[0]=='T':
                    Teacher_Menu()
                elif a[0]=='A':
                    Admin_Menu()
            else:   
                print("Oops!! Invalid Choice.\nPlease enter a valid choice.(1 or 2 or 3)")

def Report_Card():
    global mc,a
    if a[0]=='S':
        v=str(a[1:])
    else:
        f=True
        while f:
            print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            print('''\t\t\t\tSEARCH STUDENT REPORT CARD
(Choose your preferred option by entering the number assigned beside the option)''')
            print("\t1) Search with Student ID")
            print("\t2) Return to Menu")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            d=int(input("Enter your choice: "))
            if d==1:
                f1=True
                while f1:
                    m=int(input("Enter Student's ID: "))
                    b="select ID from std_details"
                    mc.execute(b)
                    t=mc.fetchall()
                    if (m,) in t:
                        v=str(m)
                        f1=False
                        f=False
                    else:
                        print("Oops!! Invalid Student ID.\nPlease enter a valid Student ID.")
            elif d==2:
                f=False
                Teacher_Menu()
            else:
                print("Oops!! Invalid Choice.\nPlease enter a valid choice")

    b="select * from std_details where ID="+v
    mc.execute(b)
    t=mc.fetchall()
    b="select BLOOD_GROUP,ORAL_HYGIENE,BMI from std_h_details where ID="+v
    mc.execute(b)
    w=mc.fetchall()
    if int(v)>=1 and int(v)<=10:
        b="select ENG,MATHS,PHY,CHEM,BIO from std_marks_T1 where ID="+v
        mc.execute(b)
        t1=mc.fetchall()
        b="select MAX(ENG),MAX(MATHS),MAX(PHY),MAX(CHEM),MAX(BIO) from std_marks_T1"
        mc.execute(b)
        t2=mc.fetchall()
        b="select ENG,MATHS,PHY,CHEM,BIO from std_marks_T2 where ID="+v
        mc.execute(b)
        t3=mc.fetchall()
        b="select MAX(ENG),MAX(MATHS),MAX(PHY),MAX(CHEM),MAX(BIO) from std_marks_T2"
        mc.execute(b)
        t4=mc.fetchall()
        b="select ENGT,ENGP,MATHST,MATHSP,PHYT,PHYP,CHEMT,CHEMP,BIOT,BIOP,ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,BIOTOT,PERCENTAGE from std_marks_PB where ID="+v
        mc.execute(b)
        t5=mc.fetchall()
        b="select MAX(ENGT),MAX(ENGP),MAX(MATHST),MAX(MATHSP),MAX(PHYT),MAX(PHYP),MAX(CHEMT),MAX(CHEMP),MAX(BIOT),MAX(BIOP) from std_marks_PB"
        mc.execute(b)
        t6=mc.fetchall()
        rc=[['English Theory\nEnglish Practical',str(t1[0][0])+'\n ---',str(t2[0][0])+'\n ---',str(t3[0][0])+'\n ---',str(t4[0][0])+'\n ---',str(t5[0][0])+'\n'+str(t5[0][1]),str(t6[0][0])+'\n'+str(t6[0][1])],
        ['Maths Theory\nMaths Practical',str(t1[0][1])+'\n ---',str(t2[0][1])+'\n ---',str(t3[0][1])+'\n ---',str(t4[0][1])+'\n ---',str(t5[0][2])+'\n'+str(t5[0][3]),str(t6[0][2])+'\n'+str(t6[0][3])],
        ['Physics Theory\nPhysics Practical',str(t1[0][2])+'\n ---',str(t2[0][2])+'\n ---',str(t3[0][2])+'\n ---',str(t4[0][2])+'\n ---',str(t5[0][4])+'\n'+str(t5[0][5]),str(t6[0][4])+'\n'+str(t6[0][5])],
        ['Chemistry Theory\nChemistry Practical',str(t1[0][3])+'\n ---',str(t2[0][3])+'\n ---',str(t3[0][3])+'\n ---',str(t4[0][3])+'\n ---',str(t5[0][6])+'\n'+str(t5[0][7]),str(t6[0][6])+'\n'+str(t6[0][7])],
        ['Biology Theory\nBiology Practical',str(t1[0][4])+'\n ---',str(t2[0][4])+'\n ---',str(t3[0][4])+'\n ---',str(t4[0][4])+'\n ---',str(t5[0][8])+'\n'+str(t5[0][9]),str(t6[0][8])+'\n'+str(t6[0][9])]]
    elif int(v)>=11 and int(v)<=20:
        b="select ENG,MATHS,PHY,CHEM,CS from std_marks_T1 where ID="+v
        mc.execute(b)
        t1=mc.fetchall()
        b="select MAX(ENG),MAX(MATHS),MAX(PHY),MAX(CHEM),MAX(CS) from std_marks_T1"
        mc.execute(b)
        t2=mc.fetchall()
        b="select ENG,MATHS,PHY,CHEM,BIO from std_marks_T2 where ID="+v
        mc.execute(b)
        t3=mc.fetchall()
        b="select MAX(ENG),MAX(MATHS),MAX(PHY),MAX(CHEM),MAX(CS) from std_marks_T2"
        mc.execute(b)
        t4=mc.fetchall()
        b="select ENGT,ENGP,MATHST,MATHSP,PHYT,PHYP,CHEMT,CHEMP,CST,CSP,ENGTOT,MATHSTOT,PHYTOT,CHEMTOT,CSTOT,PERCENTAGE from std_marks_PB where ID="+v
        mc.execute(b)
        t5=mc.fetchall()
        b="select MAX(ENGT),MAX(ENGP),MAX(MATHST),MAX(MATHSP),MAX(PHYT),MAX(PHYP),MAX(CHEMT),MAX(CHEMP),MAX(CST),MAX(CSP) from std_marks_PB"
        mc.execute(b)
        t6=mc.fetchall()
        rc=[['English Theory\nEnglish Practical',str(t1[0][0])+'\n ---',str(t2[0][0])+'\n ---',str(t3[0][0])+'\n ---',str(t4[0][0])+'\n ---',str(t5[0][0])+'\n'+str(t5[0][1]),str(t6[0][0])+'\n'+str(t6[0][1])],
        ['Maths Theory\nMaths Practical',str(t1[0][1])+'\n ---',str(t2[0][1])+'\n ---',str(t3[0][1])+'\n ---',str(t4[0][1])+'\n ---',str(t5[0][2])+'\n'+str(t5[0][3]),str(t6[0][2])+'\n'+str(t6[0][3])],
        ['Physics Theory\nPhysics Practical',str(t1[0][2])+'\n ---',str(t2[0][2])+'\n ---',str(t3[0][2])+'\n ---',str(t4[0][2])+'\n ---',str(t5[0][4])+'\n'+str(t5[0][5]),str(t6[0][4])+'\n'+str(t6[0][5])],
        ['Chemistry Theory\nChemistry Practical',str(t1[0][3])+'\n ---',str(t2[0][3])+'\n ---',str(t3[0][3])+'\n ---',str(t4[0][3])+'\n ---',str(t5[0][6])+'\n'+str(t5[0][7]),str(t6[0][6])+'\n'+str(t6[0][7])],
        ['Computer Science Theory\nComputer Science Practical',str(t1[0][4])+'\n ---',str(t2[0][4])+'\n ---',str(t3[0][4])+'\n ---',str(t4[0][4])+'\n ---',str(t5[0][8])+'\n'+str(t5[0][9]),str(t6[0][8])+'\n'+str(t6[0][9])]]

    hc=[[w[0][0],w[0][1],w[0][2]]]
    h1=['Subjects','Term-1','Highest Marks in the Class','Term-2','Highest Marks in the Class','Pre-Board','Highest Marks in the Class']
    h2=['BLOOD GROUP','ORAL HYGIENE','BMI']
    if t5[0][15]>=90:
        c='Excellent!!'
    elif t5[0][15]>=80:
        c='Very Good! Keep It Up!!'
    elif t5[0][15]>=70:
        c='Good!!'
    elif t5[0][15]>=50:
        c="You can do much better!"
    elif t5[0][15]<50:
        c="Needs to really work hard"
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print('''\t\t\t\t\t\t\t\tDON BOSCO SCHOOL
\t\t\t\t\t\t\t      ALAKNANDA, NEW DELHI
\t\t\t\t\t\t\t   ACADEMIC SESSION : 2021-22\n\n''')
    print("\t\tName: "+t[0][1],"\t\t\t\t\tRoll No. : "+str(t[0][4]),"\t\t\t\t\tD.O.B.: "+t[0][8])
    print("\t\tClass And Section: XII-"+t[0][5],"\t\t\t\tID: "+str(t[0][0]))
    print("\t\tFather's Name: "+t[0][2],"\t\t\t\tAcademic Session: 2021-2022")
    print("\t\tMother's Name: "+t[0][3])
    print(tabulate(rc,headers=h1,tablefmt='grid',numalign='center',stralign='center'))
    print("\n\t\tAttendance: "+str(t[0][6])+" / 230","\t\t\t\t\t\t\tPercentage: "+str((t5[0][10]+t5[0][11]+t5[0][12]+t5[0][13]+t5[0][14])/5)+'\n')
    print(tabulate(hc,headers=h2,tablefmt='grid',numalign='center',stralign='center'))
    print("\n\t\tComments: "+c)
    print("\n\t\tAdditional Comments From Class Teacher: "+str(t[0][9]),'\n\n')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    if a[0]=='S':
        Student_Menu()
    elif a[0]=='T':
        Teacher_Menu()
    elif a[0]=='A':
        Admin_Menu()

def Student_Menu():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print('''\t\t\t\tSTUDENT MENU
(Choose your preferred option by entering the number assigned beside the option)

\t\t\t1)View Your Report Card
\t\t\t2)View Your Progress Report
\t\t\t3)Viewing Class Toppers
\t\t\t4)Exit''')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    check='f'
    while check=='f':
        b=int(input("Enter your preferred choice: "))
        if b==1:
            check='t'
            Report_Card()
        elif b==2:
            check='t'
            Progress_Report()
        elif b==3:
            check='t'
            Class_Toppers()
        elif b==4:
            check='t'
            Login_ID()
        else:   
            print("Oops!! Invalid Choice. Please enter a valid choice by entering the number mentioned before the choice.")

def Teacher_Menu():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print('''\t\t\t\tTEACHER MENU
(Choose your preferred option by entering the number assigned beside the option)

\t\t\t1)Search A Student's Report Card
\t\t\t2)Modify A Student's Report Card
\t\t\t3)View Class Performance And Progress Report
\t\t\t4)View Class Toppers
\t\t\t5)Exit''')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    check='f'
    while check=='f':
        b=int(input("Enter your preferred choice: "))
        if b==1:
            check='t'
            Report_Card()
        elif b==2:
            check='t'
            Modify_Report_Card()
        elif b==3:
            check='t'
            Progress_Report()
        elif b==4:
            check='t'
            Class_Toppers()
        elif b==5:
            check='t'
            Login_ID()
        else:   
            print("Oops!! Invalid Choice. Please enter a valid choice by entering the number mentioned before the choice.")

def Admin_Menu():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print('''\t\t\t\tADMIN MENU
(Choose your preferred option by entering the number assigned beside the option)

\t\t\t1)Search A Student's Report Card
\t\t\t2)Modify A Student's Repport Card
\t\t\t3)View Class Performance And Progress Report
\t\t\t4)View Class Toppers
\t\t\t5)Exit''')
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    check='f'
    while check=='f':
        b=int(input("Enter your preferred choice: "))
        if b==1:
            check='t'
            Report_Card()
        elif b==2:
            check='t'
            Modify_Report_Card()
        elif b==3:
            check='t'
            Progress_Report()
        elif b==4:
            check='t'
            Class_Toppers()
        elif b==5:
            check='t'
            Login_ID()
        else:   
            print("Oops!! Invalid Choice.\nPlease enter a valid choice by entering the number mentioned before the choice.")
    
def Login_ID():
    global a,mc
    f=True
    while f:
        b=input("Enter Login ID (Enter '0' to end program): ")
        a=b
        if b=='0':
            print("Program Terminated")
            break
        elif b[0]=='S':
            e=int(b[1:])
            t=(e,)
            c="select ID from std_details"
        elif b[0]=='T':
            e=int(b[1:])
            t=(e,)
            c="select ID from t_details"
        elif b[0]=='A':
            e=int(b[1:])
            t=(e,)
            c="select ID from a_details"
        else:
            print('Oops!! Invalid Login ID.\nPlease Enter Valid Login ID')
            Login_ID()
        mc.execute(c)
        d=mc.fetchall()
        if (t in d):    
            if b[0]=='S':            
                Student_Menu()
            elif b[0]=='T':
                Teacher_Menu()
            elif b[0]=='A':
                Admin_Menu()
        else:
            print('Oops!! Invalid Login ID.\nPlease enter valid Login ID')

a=0
m=ms.connect(host='localhost',user='root',passwd='Bdebjit1103',database='Report_Card')
mc=m.cursor()
Login_ID()
