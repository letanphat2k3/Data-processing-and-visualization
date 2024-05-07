import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Bttlpython\ThuyetTrinh\Tep_so_21_da_loc.csv')
list = ['toan','ngu_van','ngoai_ngu','vat_li','hoa_hoc','sinh_hoc','lich_su','dia_li','gdcd']
data['so_mon_thi'] = data[list].notna().sum(axis=1).to_list() # tính tổng số môn thi và gán vào cột 'so_mon_thi'

data_new=data.fillna(-1)
print(data_new.head())
#tính tổng số học sinh thi môn Toán
math=data_new[data_new['toan']>=0].count()['toan']
#print(math)
#tính tổng số học sinh thi môn Văn
literature=data_new[data_new['ngu_van']>=0].count()['ngu_van']
#print(literature)
#tinh tong so hoc sinh thi mon Ngoai Ngu
English=data_new[data_new['ngoai_ngu']>=0].count()['ngoai_ngu']
#print(English)
#Vat ly
Physic=data_new[data_new['vat_li']>=0].count()['vat_li']
#print(Physic)
#Hoa hoc
Chemictry=data_new[data_new['hoa_hoc']>=0].count()['hoa_hoc']
#print(Chemictry)
#Sinh hoc
biology=data_new[data_new['sinh_hoc']>=0].count()['sinh_hoc']
#print(biology)
#Lich su
History=data_new[data_new['lich_su']>=0].count()['lich_su']
#print(History)
#Dia li
Geography=data_new[data_new['dia_li']>=0].count()['dia_li']
#print(Geography)
#GDCD
GDCD=data_new[data_new['gdcd']>=0].count()['gdcd']
#print(GDCD)

#data cho truc x
trucX=['Toan','Ngu Van', 'Ngoai Ngu', 'Vat li', 'Hoa hoc','Sinh hoc', 'Lich su', 'Dia li','GDCD']

#data cho truc y
trucY=[math,literature,English,Physic,Chemictry,biology,History,Geography,GDCD]

total_student=data_new.count()['sbd']
print(total_student)
phan_tram=(trucY/total_student)*100

#Ve bieu do:
plt.bar(trucX,phan_tram)
plt.title('Tổng số học sinh thi mỗi môn')
plt.xlabel('Môn học')
plt.ylabel('Số lượng thí sinh')
for index, value in enumerate(phan_tram):
    plt.text(index, value, f'{value:.1f}%', ha='center', va='bottom')
plt.show()
plt.savefig('percent_student8.png')

