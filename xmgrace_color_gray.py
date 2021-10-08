###!/usr/bin/python                                                                                                                                            
### This is obtained from :http://lptms.u-psud.fr/wiki/index.php/Generating_color_palette_for_Xmgrace


def LinearGray(num):
    print "@map color 0 to (255, 255, 255), \"white\""
    print "@map color 1 to (0, 0, 0), \"black\""
    N=int(255/num)
    for i in range(1,num):
        n = str(N*i)
        print "@map color "+str(i+1)+" to ("+n+','+n+','+n+"), \"gray"+str(i)+"\""

LinearGray(int(input("##How many number of gray shades?")))
