import csv
baslik = ["sicaklik", "nem", "basinc"]
veri = [[15, 25.5, 10], [15.7, 42, 3]]
with open('sensor_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)