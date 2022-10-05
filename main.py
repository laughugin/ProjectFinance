import time


def get_back(x,y):
    print("\033[%d;%dH" % (x, y))

s = "  "
f = ["XX","YY","YY","yy","NN","  "]
k = [
    0,0,5,  #                     ####                        
    0,0,5,5,#                 ####                            
    0,5,    #               ##                                        
    0,5,    #             ##                                           
    1,4,    #             &&                  ::               
    1,4,    #           &&                      ::               
    1,4,    #           &&                      ::               
    1,4,    #           &&                      ::                  
    1,4,    #             &&                  ::            
    2,3,    #             {}                  //             
    2,3,    #               {}              //                   
    2,2,3,3,#                 {}{}      ////               
    2,3,3   #                     {}////                       
    ]   

while 1:
    i = 0
    get_back(0,0)
    print(".\n")                                            
    print(5*s+f[k[0]]+f[k[1]]+f[k[2]])                      
    print(3*s+f[k[3]]+f[k[4]]+3*s+f[k[5]]+f[k[6]])          
    print(2*s+f[k[7]]+7*s+f[k[8]])                          
    print(1*s+f[k[9]]+9*s+f[k[10]])                         
    print(1*s+f[k[11]]+9*s+f[k[12]])                        
    print(0*s+f[k[13]]+11*s+f[k[14]])                       
    print(0*s+f[k[15]]+11*s+f[k[16]])                       
    print(0*s+f[k[17]]+11*s+f[k[18]])                       
    print(1*s+f[k[19]]+9*s+f[k[20]])                        
    print(1*s+f[k[21]]+9*s+f[k[22]])                        
    print(2*s+f[k[23]]+7*s+f[k[24]])                        
    print(3*s+f[k[25]]+f[k[26]]+3*s+f[k[27]]+f[k[28]])      
    print(5*s+f[k[29]]+f[k[30]]+f[k[31]])                   
    while i < 31:
        if k[i] < 5:
            k[i] = k[i] + 1
        else:
            k[i] = 0
        i = i + 1
    time.sleep(0.15)
    print("fdas")