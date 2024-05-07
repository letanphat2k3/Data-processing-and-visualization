import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Bttlpython\ThuyetTrinh\danh_sach_thi_sinh_12_Thai_Nguyen.csv')
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
#diem cua hoc sinh >= 27
A = math + Physic + Chemictry
print('Số học sinh có điểm xuất sắc khối A00 là: ')
print(data_new[A >= 27]['sbd'])
B = math + Chemictry + biology
print('Số học sinh có điểm xuất sắc khối B00 là: ')
print(data_new[B >= 27]['sbd'])
C = literature + History + Geography
print('Số học sinh có điểm xuất sắc khối C00 là: ')
print(data_new[C >= 27]['sbd'])
D = math + literature + English
print('Số học sinh có điểm xuất sắc khối D00 là: ')
print(data_new[D >= 27]['sbd'])
A_greater_than_27 = len(A[A >= 27])
B_greater_than_27 = len(B[B >= 27])
C_greater_than_27 = len(C[C >= 27])
D_greater_than_27 = len(D[D >= 27])
#tong so hoc sinh co diem >= 27
ABCD_greater_than_27 = A_greater_than_27 + B_greater_than_27 + C_greater_than_27 + D_greater_than_27
print(ABCD_greater_than_27)
#ve do thi
labels = 'Khối A00', 'Khối B00', 'Khối C00', 'Khối D00'
sizes = [(A_greater_than_27/ABCD_greater_than_27)*100,(B_greater_than_27/ABCD_greater_than_27)*100, (C_greater_than_27/ABCD_greater_than_27)*100, (D_greater_than_27/ABCD_greater_than_27)*100]
colors = ['red', 'yellow', 'coral', 'blue']
plt.title('Số học sinh có thành tích xuất sắc tỉnh Thái Nguyên(12)')
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
plt.axis('equal')
plt.show()



