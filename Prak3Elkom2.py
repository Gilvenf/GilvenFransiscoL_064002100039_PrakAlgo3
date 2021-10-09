a= ("@@@@  @  @     @       @ @@@@ @@    @")
b= ("@     @  @      @     @  @    @ @   @")
c= ("@ @@  @  @       @   @   @@@@ @  @  @")
d= ("@  @  @  @        @ @    @    @   @ @")
e= ("@@@@  @  @@@@      @     @@@@ @     @ ")
print(a)
print(b)
print(c)
print(d)
print(e)
totalHarga =int(input("masukan total harga belanjaan anda : "))
uangAnda =int(input("masukan jumlah uang anda : "))
kembalian = uangAnda - totalHarga
lembar100000 = 0
lembar50000 = 0
lembar20000 = 0
lembar10000 = 0
lembar5000 = 0
lembar2000 = 0
lembar1000 = 0
koin500 = 0
koin200 = 0
koin100 = 0
koin50  = 0
print ("kembalian anda  ", kembalian)
if kembalian < 0 : 
    print("DUIT ANDA KURANG")
else:
    while kembalian > 0 : 
        if  kembalian > 100000 : 
            kembalian = kembalian - 100000
            lembar100000 += 1
            print(kembalian)
        elif kembalian >= 50000 :
            kembalian = kembalian - 50000
            lembar50000 += 1
        elif kembalian >= 20000 :
            kembalian = kembalian - 20000
            lembar20000 += 1
        elif kembalian >= 10000 :
            kembalian = kembalian - 10000
            lembar10000 += 1
        elif kembalian >= 5000 :
            kembalian = kembalian - 5000
            lembar5000 +=1
        elif kembalian >= 2000 :
            kembalian = kembalian - 2000
            lembar2000 += 1
        elif kembalian >= 1000 :
            kembalian + kembalian - 1000
            lembar1000 += 1
        elif kembalian >= 500  :
            kembalian > kembalian -  500
            koin500 += 1
        elif kembalian >= 200  :
            kembalian > kembalian - 200
            koin200 += 1
        elif kembalian >= 100  :
            kembalian > kembalian - 100
            koin100 +=1
        elif kembalian >= 50 :
            kembalian > 50 - 50 
            koin50 +=1  
        else :
            kembalian = 0
    else :

        if lembar100000 != 0 :       
            print("lembar 100000 =" ,lembar100000, "lembar" )
        if lembar50000 != 0 :        
            print("lembar 50000 =" ,lembar50000, "lembar" )
        if lembar20000 != 0 :        
            print("lembar 20000 =" ,lembar20000, "lembar" )
        if lembar10000 != 0 :       
            print("lembar 10000 =" ,lembar10000, "lembar" )
        if lembar5000!= 0 :          
            print("lembar 5000 =" ,lembar5000, "lembar" )
        if lembar2000 != 0 :        
            print("lembar 2000 =" ,lembar2000, "lembar" )
        if lembar1000 != 0 :        
            print("lembar 1000 =" ,lembar1000, "lembar" )
        if koin500 != 0 :           
            print("koin 500 =" ,koin500, "koin" )
        if koin200 != 0 :            
            print("koin 200 =" ,koin200, "koin" )
        if koin100 != 0 :           
            print("koin 100 =" ,koin100, "koin" )
        if koin50 != 0 :             
            print("koin 50 =" ,koin50, "koin" ) 