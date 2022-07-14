import psutil
import numpy as np
import smtplib
import shutil



import datetime
pol=datetime.datetime.now()
print(pol)


def fredkin(f0,f1,f2):
    a=f0;
    b=(not f0 and f1) ^ (f0 and f2)
    c=(not f0 and f2) ^ (f0 and f1)
    return (a,b,c)
    
def fy(q,w,e):
    
    r=q
    s=q ^w
    t=q^e
    return(r,s,t)
    
def nft(k,l,z):
    
    f=k ^l;
    g=int((not l and z) ^ (k and not(z)))
    v=(l and z) ^ (k and (not(z)))
    return(f,g,v)
    
ma=input("enter mail:")
server_location=input("Please enter the location of the file that u want to copy:")
recv_location=input("Please enter the location where u want to copy:")
filename=input("Enter the filenmae with extension:")   

a=int(psutil.cpu_percent());
print("The CPU Percentage is:",a)
d=format(a, '09b')     
x=d.zfill(10)
def designa(x)  :
    
    
    
    #fredkin 1
    (OA1,o1,OA2)=fredkin(int(x[0]),int(x[1]),int(x[2]))
    
    #fyen 1
    (o2,o3,OA3)=fy(int(x[3]),int(x[4]),int(x[5]))
    
    #fyen2
    (OA4,OA5,o4)=fy(OA1,o2,o3)
    
    #fredkin2
    (I1,I2,I3)=fredkin(int(x[6]),int(x[7]),int(x[8]))

    #fyenman3
    (OA6,OA7,I4)=fy(o4,I1,I2)

    #not gate
    no=int(not(int(x[9])))
    #fyenman4
    (OA8,OA9,OA10)=fy(I4,I3,no)
    
    
    

    o_pA=np.array([OA1,OA2,OA3,OA4,OA5,OA6,OA7,OA8,OA9,OA10        ])
    print("The Output of TRNG a:",o_pA)
   
        
    
    return (OA1,OA2,OA3,OA4,OA5,OA6,OA7,OA8,OA9,OA10)


(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)=designa(x)

outa=np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])




def designb(x):
    
    
    
    
    
    #fy 1
    (OB1,o1,OB2)=fredkin(int(x[0]),int(x[1]),int(x[2]))
    
    #fy 2
    (o2,o3,OB3)=nft(int(x[3]),int(x[4]),int(x[5]))
    
    #fr 1
    (OB4,OB5,o4)=fredkin(OB1,o2,o3)
  
    #fy3
    (I1,I2,I3)=nft(int(x[6]),int(x[7]),int(x[8]))
   
    #fy4
    (OB6,OB7,I4)=fredkin(o4,I1,I2)
    
    
    no=int(not(int(x[9])))
    
    (OB8,OB9,OB10)=nft(I4,I3,no)
 
    
   
    o_pB=np.array([OB1,OB2,OB3,OB4,OB5,OB6,OB7,OB8,OB9,OB10])
    print("The Output of TRNG b:",o_pB)
    
        
        
    return (OB1,OB2,OB3,OB4,OB5,OB6,OB7,OB8,OB9,OB10)


(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10)=designb(x)

outb=np.array([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10])













def designc(x):
    
    
    
    
    
    #fy 
    (OC1,o1,OC2)=nft(int(x[0]),int(x[1]),int(x[2]))
    
    #fy 2
    (o2,o3,OC3)=nft(int(x[3]),int(x[4]),int(x[5]))
    
    #fr 1
    (OC4,OC5,o4)=nft(OC1,o2,o3)
    
    #fy3
    (I1,I2,I3)=nft(int(x[6]),int(x[7]),int(x[8]))
    
    #fy4
    (OC6,OC7,I4)=fy(o4,I1,I2)
    
    no=int(not(int(x[9])))
    
    (OC8,OC9,OC10)=fy(I4,I3,no)
    
    
    o_pC=np.array([OC1,OC2,OC3,OC4,OC5,OC6,OC7,OC8,OC9,OC10    ])
    print("The Output of TRNG c:",o_pC)
    
    return (OC1,OC2,OC3,OC4,OC5,OC6,OC7,OC8,OC9,OC10)

(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)=designc(x)

outc=np.array([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10])



def designd(x):
    
    #fy 
    (OD1,o1,OD2)=fy(int(x[0]),int(x[1]),int(x[2]))
    
    #fy 2
    (o2,o3,OD3)=nft(int(x[3]),int(x[4]),int(x[5]))
    
    #fr 1
    (OD4,OD5,o4)=fredkin(OD1,o2,o3)
    
    #fy3
    (I1,I2,I3)=fy(int(x[6]),int(x[7]),int(x[8]))
    
    #fy4
    (OD6,OD7,I4)=nft(o4,I1,I2)
    
    no=int(not(int(x[9])))
    
    (OD8,OD9,OD10)=nft(I4,I3,no)
    
    
    o_pD=np.array([OD1,OD2,OD3,OD4,OD5,OD6,OD7,OD8,OD9,OD10    ])
    print("The Output of TRNG d:",o_pD)
    
    return (OD1,OD2,OD3,OD4,OD5,OD6,OD7,OD8,OD9,OD10)

(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10)=designd(x)

outd=np.array([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10])

no=int(not(int(x[9])))
i_p=np.array([ int(x[0],2), int(x[1],2) ,int(x[2],2),int(x[3],2),int(x[4],2),int(x[5],2),int(x[6],2),int(x[7],2),int(x[8],2),no])

a_stat=int((i_p[0] ^ i_p[1] ^ i_p[2] ^ i_p[3]  ^ i_p[4] ^ i_p[5] ^ i_p[6] ^ i_p[7] ^ i_p[8] ^ i_p[9] == outa[0] ^ outa[1] ^ outa[2] ^ outa[3] ^ outa[4]  ^ outa[5] ^ outa[6] ^ outa[7]  ^ outa[8] ^ outa[9]  ))
b_stat=int((i_p[0] ^ i_p[1] ^ i_p[2] ^ i_p[3]  ^ i_p[4] ^ i_p[5] ^ i_p[6] ^ i_p[7] ^ i_p[8] ^ i_p[9] == outb[0] ^ outb[1] ^ outb[2] ^ outb[3] ^ outb[4]  ^ outb[5] ^ outb[6] ^ outb[7]  ^ outb[8] ^ outb[9]  ))
c_stat=int((i_p[0] ^ i_p[1] ^ i_p[2] ^ i_p[3]  ^ i_p[4] ^ i_p[5] ^ i_p[6] ^ i_p[7] ^ i_p[8] ^ i_p[9] == outc[0] ^ outc[1] ^ outc[2] ^ outc[3] ^ outc[4]  ^ outc[5] ^ outc[6] ^ outc[7]  ^ outc[8] ^ outc[9]  ))
d_stat=int((i_p[0] ^ i_p[1] ^ i_p[2] ^ i_p[3]  ^ i_p[4] ^ i_p[5] ^ i_p[6] ^ i_p[7] ^ i_p[8] ^ i_p[9] == outd[0] ^ outd[1] ^ outd[2] ^ outd[3] ^ outd[4]  ^ outd[5] ^ outd[6] ^ outd[7]  ^ outd[8] ^ outd[9]  ))

if(a_stat==1 and b_stat==1 and c_stat==1 and d_stat==1):
    
    
    config=input("enter the config:")
    config_array=list(config)
    otp=''
    for opt in config_array:
        
        switch={'A':designa,
                'B':designb,
                'C':designc,
                'D':designd}
        function=switch.get(opt)
        output=function(x)
        for a in output:
            otp+=str(a)
        print('the otp is:',otp)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login("sender email id", "password") 
    # message to be sent 
    message = otp
    # sending the mail 
    s.sendmail("receiver email", ma, otp) 
    print('mail sent')
    s.quit()
    
    otp1=input('enter the otp:')
    otp2=input('reconfirm the otp:')
    
    if(otp1 == otp  and otp2!=otp1):
        while(otp1 != otp2):
            print('check passsword')
            otp1=input('enter the otp:')
            otp2=input('reconfirm the otp:')
        print('file trasfer after otp correcy')
        src =server_location+'\\'+filename
        dst = recv_location
        shutil.copy(src, dst)
        print("file transfered")
        
        
    elif(otp2==otp and otp1!=otp2):
        while(otp2!=otp1):
            print('check passsword')
            otp1=input('enter the otp:')
            otp2=input('reconfirm the otp:')
        print('file transferred after')
        src =server_location+'\\'+filename
        dst = recv_location
        shutil.copy(src, dst)
        print("file transfered")
        
        
        
    elif(otp1==otp and otp2==otp):
        star=datetime.datetime.now()
        print(star)
            
        src =server_location+'\\'+filename
        dst = recv_location
        shutil.copy(src, dst)
        
        
        e_n=datetime.datetime.now()
        print(e_n)
        
        
        
    elif(otp1!=otp and otp2!=otp and otp1==otp2):
        star=datetime.datetime.now()
        print(star)
        
        file=open(filename,'r+')
        content=file.readlines()
        content1=content
        content1=list(content1[0])
        length=len(content1)
        otp_len=len(otp)
        rem=length % otp_len
        list_otp=list(otp)
        
        for i in range(0,length,1):
            
            
            if(int (list_otp[i %  otp_len])==1):
                
                content1[i]= str(int((not(int(content1[i])))))
                
        scramble=''
        for j in content1:
            
            scramble+=str(j)
        file.close()
        
        f = open(recv_location+'\\'+filename, "w")
        f.write(scramble)
        f.close()
        e_n=datetime.datetime.now()
        print(e_n)
        
            
        
    
  
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

else:
    
    
    print('failed')











    
