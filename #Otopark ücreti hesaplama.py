#Otopark ücreti hesaplama
saat=int(input("Kaldğınız süreyi sisteme girin:"))
ucret=10
if saat<=1:
    ucret<=20
elif saat<=5:
    ucret=10*saat
else:
    ucret=10*saat
print("ödemeniz gereken tutar {}".format(ucret))