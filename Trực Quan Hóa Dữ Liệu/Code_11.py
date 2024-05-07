import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Bttlpython\ThuyetTrinh\danh_sach_thi_sinh_11_Bac_Kan.csv')
data_new=data.fillna(-1)
math=data_new[data_new['toan']>=0].count()['toan']
#tinh tong so hoc sinh thi mon Văn
literature=data_new[data_new['ngu_van']>=0].count()['ngu_van']
#tinh tong so hoc sinh thi mon Ngoai Ngu
English=data_new[data_new['ngoai_ngu']>=0].count()['ngoai_ngu']
#tinh tong so hoc sinh thi mon Vat ly
Physic=data_new[data_new['vat_li']>=0].count()['vat_li']
#tinh tong so hoc sinh thi mon Hoa hoc
Chemictry=data_new[data_new['hoa_hoc']>=0].count()['hoa_hoc']
#tinh tong so hoc sinh thi mon Sinh hoc
biology=data_new[data_new['sinh_hoc']>=0].count()['sinh_hoc']
#tinh tong so hoc sinh thi mon Lich su
History=data_new[data_new['lich_su']>=0].count()['lich_su']
#tinh tong so hoc sinh thi monDia li
Geography=data_new[data_new['dia_li']>=0].count()['dia_li']
#tinh tong so hoc sinh thi mon GDCD
GDCD=data_new[data_new['gdcd']>=0].count()['gdcd']
#data cho truc x
trucX=['Toan','Ngu Van', 'Ngoai Ngu', 'Vat li', 'Hoa hoc','Sinh hoc', 'Lich su', 'Dia li','GDCD']

#data cho truc y
trucY=[math,literature,English,Physic,Chemictry,biology,History,Geography,GDCD]

total_student=data_new.count()['sbd']
print(total_student)
phan_tram=(trucY/total_student)*100

#Ve bieu do:
plt.bar(trucX,phan_tram)
plt.title('Tổng số học sinh thi mỗi môn ở tỉnh Bắc Kạn(11)')
plt.xlabel('Môn học')
plt.ylabel('Số lượng thí sinh')
for index, value in enumerate(phan_tram):
    plt.text(index, value, f'{value:.2f}%', ha='center', va='bottom')
plt.show()
