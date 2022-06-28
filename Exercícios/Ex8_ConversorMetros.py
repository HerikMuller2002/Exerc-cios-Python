#ConversorMetros

m = float(input('Uma distância em metros: '))
km = float(m/1000)
hm = float(m/100)
dam = float(m/10)
dm = m*10
cm = m*100
mm = m*1000

print('\nA medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm' .format(m, km, hm, dam, dm, cm, mm))