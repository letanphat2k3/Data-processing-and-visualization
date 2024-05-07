import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Bttlpython\ThuyetTrinh\danh_sach_thi_sinh_14_Son_La.csv')
data_new=data.fillna(0)
print(data_new.head())
math=data_new['toan']
#tinh tong so hoc sinh thi mon Văn
literature=data_new['ngu_van']
#tinh tong so hoc sinh thi mon Ngoai Ngu
English=data_new['ngoai_ngu']
#tinh tong so hoc sinh thi mon Vat ly
Physic=data_new['vat_li']
#tinh tong so hoc sinh thi mon Hoa hoc
Chemictry=data_new['hoa_hoc']
#tinh tong so hoc sinh thi mon Sinh hoc
biology=data_new['sinh_hoc']
#tinh tong so hoc sinh thi mon Lich su
History=data_new['lich_su']
#tinh tong so hoc sinh thi mon Dia li
Geography=data_new['dia_li']
#tinh tong so hoc sinh thi mon GDCD
GDCD=data_new['gdcd']
#data cho bieu do
#diem cua hoc sinh < 15
A = math + Physic + Chemictry
print('Số học sinh có thành tích kém khối A là: ')
print(data_new[A < 15]['sbd'])
B = math + Chemictry + biology
print('Số học sinh có thành tích kém khối B là: ')
print(data_new[B < 15]['sbd'])
C = literature + History + Geography
print('Số học sinh có thành tích kém khối C là: ')
print(data_new[C < 15]['sbd'])
D = math + literature + English
print('Số học sinh có thành tích kém khối D là: ')
print(data_new[D < 15]['sbd'])
A_lower_than_15 = len(A[A < 15])
B_lower_than_15 = len(B[B < 15])
C_lower_than_15 = len(C[C < 15])
D_lower_than_15 = len(D[D < 15])
#tong so hoc sinh
ABCD_lower_than_15 = A_lower_than_15 + B_lower_than_15 + C_lower_than_15 + D_lower_than_15
print(ABCD_lower_than_15)
#ve do thi
labels = 'Khối A00', 'Khối B00', 'Khối C00', 'Khối D00'
sizes = [(A_lower_than_15/ABCD_lower_than_15)*100,(B_lower_than_15/ABCD_lower_than_15)*100, (C_lower_than_15/ABCD_lower_than_15)*100, (D_lower_than_15/ABCD_lower_than_15)*100]
colors = ['red', 'yellow', 'coral', 'blue']
plt.title('Số học sinh có thành tích kém tỉnh Sơn La(14)')
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
plt.axis('equal')
plt.show()



