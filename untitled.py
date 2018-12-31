
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
#


bacaData = pd.read_csv('DataTugas2.csv',header=None)
#FUZZIFICATION

dataGaji=bacaData[1:][1]
dataHutang=bacaData[1:][2]

print(dataGaji
      )
print('Gaji terbesar : ',max(bacaData[1:][1]))
print('Hutang Terbanyak : ',max(bacaData[2:][2]))

print('Gaji terkecil : ',min(bacaData[1:][1]))
print('Hutang Ter-sedikit : ',min(bacaData[2:][2]))

#definisiGaji
def GajiSangatKecil(x):
    if (x<=0.300):
        SangatKecil=1
    elif(x>0.300 and x<0.400):
        SangatKecil=(0.400-x)/(0.400-0.300)
    else:
        SangatKecil=0
    return SangatKecil

def GajiKecil(x):
    if (x>=0.400 and x<=0.700):
        Kecil=1
    elif(x>0.300 and x<0.400):
        Kecil=(x-0.300)/(0.400-0.300)
    elif(x>0.700 and x<0.800):
        Kecil=(0.800-x)/(0.800-0.700)
    else:
        Kecil=0
    return Kecil

def GajiSedang(x):
    if (x>=0.800 and x<=1.100):
        Sedang=1
    elif(x>0.700 and x<0.800):
        Sedang=(x-0.700)/(0.800-0.700)
    elif(x>1.100 and x<1.200):
        Sedang=(1.200-x)/(1.200-1.100)
    else:
        Sedang=0
    return Sedang

def GajiBesar(x):
    if (x>=1.200 and x<=1.500):
        Besar=1
    elif(x>1.100 and x<1.200):
        Besar=(x-1.100)/(1.200-1.100)
    elif(x>1.500 and x<1.600):
        Besar=(1.600-x)/(1.600-1.500)
    else:
        Besar=0
    return Besar

def GajiSangatBesar(x):
    if (x>=1.600):
        SangatBesar=1
    elif(x>1.500 and x<1.600):
        SangatBesar=(x-1.500)/(1.600-1.500)
    else:
        SangatBesar=0
    return SangatBesar

#definisi Hutang
    
def HutangSedikit(x):
    if (x<=33.000):
        Sedikit=1
    elif(x>33.000 and x<44.000):
        Sedikit=(44.000-x)/(44.000-33.000)
    else:
        Sedikit=0
    return Sedikit

def HutangSedang(x):
    if (x>=44.000 and x<=55.000):
        Sedang=1
    elif(x>33.000 and x<44.000):
        Sedang=(x-33.000)/(44.000-33.000)
    elif(x>55.000 and x<66.000):
        Sedang=(66.000-x)/(66.000-55.000)
    else:
        Sedang=0
    return Sedang

def HutangBanyak(x):
   
    if (x>=66):
        SangatBesar=1
    elif(x>55 and x<66):
        SangatBesar=(x-55)/(66-55)
    else:
        SangatBesar=0
    return SangatBesar


#definisiPenerimaBLTinMamdani
    
def BLTRendahMamdani(x):
    if(x<=50):
        RendahMamdani=1
    elif(x>50 and x<80):
        RendahMamdani=(80-x)/(80-50)
    else:
        RendahMamdani=0
    return RendahMamdani

def BLTTinggiMamdani(x):
    if (x>=80):
        TinggiMamdani=1
    elif(x>50 and x<80):
        TinggiMamdani=(x-50)/(80-50)
    else:
        TinggiMamdani=0
    return TinggiMamdani

#definisiPenerimaBLTinSugeno(graph)
 
def BLTRendahSugeno(x):
    if(x==50):
        RendahSugeno=1
    
    else:
        RendahSugeno=0
    return RendahSugeno

def BLTTinggiSugeno(x):
    if (x==80):
        TinggiSugeno=1
    else:
        TinggiSugeno=0
    return TinggiSugeno


#print('Gajinya kecil ga ?',GajiSangatKecil(float(dataGaji[83])))
#GrafikGaji
Gaji = np.arange(0,2,0.05)
plot.plot(Gaji,[GajiSangatKecil(x) for x in Gaji],color='red')
plot.plot(Gaji,[GajiKecil(x) for x in Gaji],color='orange')
plot.plot(Gaji,[GajiSedang(x) for x in Gaji],color='yellow')
plot.plot(Gaji,[GajiBesar(x) for x in Gaji],color='green')
plot.plot(Gaji,[GajiSangatBesar(x) for x in Gaji],color='blue')
plot.legend()
plot.show()

#GrafikUtang
Utang = np.arange(0,100,0.05)
plot.plot(Utang,[HutangSedikit(x) for x in Utang],color='red')
plot.plot(Utang,[HutangSedang(x) for x in Utang],color='green')
plot.plot(Utang,[HutangBanyak(x) for x in Utang],color='blue')
plot.legend()
plot.show()

#GrafikPenerimainSugeno
penerimaBLT = np.arange(0,100,0.05)
plot.plot(penerimaBLT,[BLTRendahSugeno(x) for x in penerimaBLT],color='red')
plot.plot(penerimaBLT,[BLTTinggiSugeno(x) for x in penerimaBLT],color='green')
plot.legend()
plot.show()
#GrafikPenerimainMamdani
#penerimaBLT = np.arange(0,100,0.05)
#plot.plot(penerimaBLT,[BLTRendahMamdani(x) for x in penerimaBLT],color='red')
#plot.plot(penerimaBLT,[BLTTinggiMamdani(x) for x in penerimaBLT],color='green')
#plot.legend()
#plot.show()

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
h1=[]
h2=[]
h3=[]
j=1
i = len(dataGaji)

temp_tinggi=[]
temp_rendah=[]
arrTinggi=[]
arrRendah=[]

while j<=i :
#    append data gaji ke array
    p1.append(GajiSangatKecil(float(dataGaji[j])))
    p2.append(GajiKecil(float(dataGaji[j])))
    p3.append(GajiSedang(float(dataGaji[j])))
    p4.append(GajiBesar(float(dataGaji[j])))
    p5.append(GajiSangatBesar(float(dataGaji[j])))
#    append data hutang ke 
    h1.append(HutangSedikit((float(dataHutang[j]))))
    h2.append(HutangSedang((float(dataHutang[j]))))
    h3.append(HutangBanyak((float(dataHutang[j]))))
    
   
    
    j=j+1
    

#INFERENCE
dataGajixHutang = pd.DataFrame({'0':p1,
                                '1':p2,
                                '2':p3,
                                '3':p4,
                                '4':p5,
                                '5':h1,
                                '6':h2,
                                '7':h3,})


rules = pd.read_excel('rules.xlsx',sheet_name='Sheet1')

print(dataGajixHutang)

for k in range(0,100):
    for m in range(0,5):
        for n in range(0,3):
#            print(rules[m][n])
            if (rules[m][n]=='Tinggi'):
             temp_tinggi.append(min(dataGajixHutang[str(m)][k],dataGajixHutang[str(n+5)][k]))
            else:
             temp_rendah.append(min(dataGajixHutang[str(m)][k],dataGajixHutang[str(n+5)][k]))
    arrTinggi.append(max(temp_tinggi))
    arrRendah.append(max(temp_rendah))
    temp_tinggi=[]
    temp_rendah=[]
    



##DEFUZZIFICATION
    
#yaMamdani=10+20+30+40+50+60
#ybMamdani=70+80+90+100
#ystarMamdani=[]
ystarSugeno=[]
for k in range(0,100): 
    ystarSugeno.append(((50)*arrRendah[k])+((80)*arrTinggi[k])/((arrRendah[k])+(arrTinggi[k])))

#print(ystarSugeno)
#print(ystarMamdani)
rang=range(1,101)
dataSugeno = pd.DataFrame({'no':rang,
                           'Hasil Perhitungan Sugeno':ystarSugeno,})

#ImportToCSV
print(dataSugeno)
sugenoSorted=dataSugeno.sort_values(by='Hasil Perhitungan Sugeno',ascending=False)
print(sugenoSorted)
sugenoSorted['no'][:20].to_csv('TebakanTugas2.csv',index = False,header=False)

