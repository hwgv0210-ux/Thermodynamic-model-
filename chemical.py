print("歡迎使用")
print('以下請輸入您想求得的單原子理想氣體熱力學性質')
print(' ')
print('a. 熱量 q')
print('b. 功 w')
print('c. 內能變化 ΔＵ')
print('d. 焓變化 ΔＨ')
print('e. 吉布斯自由能 ΔＧ')
print('f. 熵變 ΔS ')
print(' ')
x=input('我想得到：')

import math
if x=='a':
    print('狀態：')
    print('1.constant volume')
    print('2.constant pressure')
    print('3.isothermal')
    print('4.adiabatic')
    

    state=input('狀態(請輸入1~4):')
    R=8.314
    Cv=1.5*R
    Cp=2.5*R

    if state=='1':
        T1=float(input('初溫度(K):'))
        T2=float(input('末溫度(K):'))
        n=float(input('莫耳數(mol):'))
        q=n*Cv*(T2-T1)
        print("q=",q,"J")
    elif state=='2':
        T1=float(input('初溫度(K):'))
        T2=float(input('末溫度(K):'))
        n=float(input('莫耳數(mol):'))
        q=n*Cp*(T2-T1)
        print("q==",q,"J")
    elif state=='3':
        T=float(input('初溫度(K):'))
        V1=float(input('初體積:'))
        V2=float(input('末體積：'))
        n=float(input('莫耳數(mol):'))
        q=n*R*T*math.log(V2/V1)
        print('q==',q,'J')
    else:
        print('q==0')



elif x=='b':
    print('狀態：')
    print('1.constant volume')
    print('2.constant pressure')
    print('3.isothermal')
    print('4.adiabatic')
    
    state=input('狀態(請輸入1~4):')
    
    R=8.314
    Cv=1.5*R
    Cp=2.5*R

    if state=='1':
        print("w=0")
    elif state=='2':
        V1=float(input('初體積:'))
        V2=float(input('末體積：'))
        p=float(input('您的外壓 Pext(Pa):'))
        w=-p*(V2-V1)
        print("w==",w,'J')
    elif state=='3':
        T=float(input('末溫度(K):'))
        V1=float(input('初體積:'))
        V2=float(input('末體積：'))
        n=float(input('莫耳數(mol):'))
        T=T1
        w=-n*R*T*math.log(V2/V1)
        print("w==",w,'J')
    else:
        T1=float(input('初溫度(K):'))
        T2=float(input('末溫度(K):'))
        n=float(input('莫耳數(mol):'))
        w=n*Cv*(T2-T1)
        print("w==",w,'J')
    
elif x=='c':
    T1=float(input('初溫度(K):'))
    T2=float(input('末溫度(K):'))
    n=float(input('莫耳數(mol):'))

    R=8.314
    Cv=1.5*R
   
    U=n*Cv*(T2-T1)
    print('ΔU=',U,'J')

elif x=='d':
    T1=float(input('初溫度(K):'))
    T2=float(input('末溫度(K):'))
    n=float(input('莫耳數(mol):'))

    R=8.314
    Cp=2.5*R
   
    H=n*Cp*(T2-T1)
    print('ΔH=',H,'J')


elif x=='e':
    T1=float(input('初溫度(K):'))
    T2=float(input('末溫度(K):'))
    n=float(input('莫耳數(mol):'))

    R=8.314
    Cp=2.5*R
   
    H=n*Cp*(T2-T1)
    s=n*Cp*math.log(T2/T1)
    G=H-T1*s
    print("ΔG =",G, "J")
    
elif x=='f':
    print('狀態：')
    print('1.constant volume')
    print('2.constant pressure')
    print('3.reversible isothermal ')
    print('4.reversible adiabatic')
    print('5.free expension (adiabatic irreversible)')


    state=input('狀態(請輸入1~5):')
    

    R=8.314
    Cv=1.5*R
    Cp=2.5*R

    if state=='1':
        T1=float(input('初溫度(K):'))
        T2=float(input('末溫度(K):'))
        T3=float(input('環境溫度(K);'))
        n=float(input('莫耳數(mol):'))
        Ssys=n*Cv*math.log(T2/T1)
        qsys=n*Cv*(T2-T1)
        Ssurr=-qsys/T3
        Suniv=Ssys+Ssurr
        print("Ssys =", Ssys, "J/K")
        print("Ssurr =", Ssurr, "J/K")
        print("Suniv =", Suniv, "J/K")



    elif state=='2':
        T1=float(input('初溫度(K):'))
        T2=float(input('末溫度(K):'))
        T3=float(input('環境溫度(K);'))
        n=float(input('莫耳數(mol):'))
        Ssys=n*Cp*math.log(T2/T1)
        qsys=n*Cp*(T2-T1)
        Ssurr=-qsys/T3
        Suniv=Ssys+Ssurr
        print("Ssys =", Ssys, "J/K")
        print("Ssurr =", Ssurr, "J/K")
        print("Suniv =", Suniv, "J/K")

    
    elif state=='3':
        T3=float(input('環境溫度(K);'))
        V1=float(input('初體積:'))
        V2=float(input('末體積：'))
        n=float(input('莫耳數(mol):'))
        Ssys=n*R*math.log(V2/V1)
        qsys=n*R*T1*math.log(V2/V1)
        Ssurr=-qsys/T3
        Suniv=0
        print("Ssys =", Ssys, "J/K")
        print("Ssurr =", Ssurr, "J/K")
        print("Suniv =", Suniv, "J/K")
    
    elif state=='4':
        Ssys=0.0
        Ssurr=0.0
        Suniv=0.0
        print("Ssys =", Ssys, "J/K")
        print("Ssurr =", Ssurr, "J/K")
        print("Suniv =", Suniv, "J/K")
  
    else:
        V1=float(input('初體積:'))
        V2=float(input('末體積：'))
        n=float(input('莫耳數(mol):'))
        Ssys=n*R*math.log(V2/V1)
        Ssurr=0.0
        Suniv=Ssys+Ssurr
        print("Ssys =", Ssys, "J/K")
        print("Ssurr =", Ssurr, "J/K")
        print("Suniv =", Suniv, "J/K")
        


else:
    print('error')
 





