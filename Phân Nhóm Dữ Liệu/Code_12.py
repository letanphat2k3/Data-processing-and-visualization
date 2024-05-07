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
#diem cua hoc sinh
A = math + Physic + Chemictry
B = math + Chemictry + biology
C = literature + History + Geography
D = math + literature + English
#so hoc sinh co diem trung binh > 27
A_greater_than_27 = len(A[A >= 27])
B_greater_than_27 = len(B[B >= 27])
C_greater_than_27 = len(C[C >= 27])
D_greater_than_27 = len(D[D >= 27])
#so hoc sinh co diem trung binh kha 15 <= diemtb < 24
A_medium_score = len(A[(A >= 15) & (A < 24)])
B_medium_score = len(A[(A >= 15) & (A < 24)])
C_medium_score = len(A[(A >= 15) & (A < 24)])
D_medium_score = len(A[(A >= 15) & (A < 24)])
#so hoc sinh co diem kha gioi 24 <= diemtb < 27
A_high_score = len(A[(A >= 24) & (A < 27)])
B_high_score = len(A[(A >= 24) & (A < 27)])
C_high_score = len(A[(A >= 24) & (A < 27)])
D_high_score = len(A[(A >= 24) & (A < 27)])
#so hoc sinh co diem yeu diemtb < 15
A_lower_than_15 = len(A[A < 15])
B_lower_than_15 = len(B[B < 15])
C_lower_than_15 = len(C[C < 15])
D_lower_than_15 = len(D[D < 15])
#ve do thi
trucX = ['A>27', 'B>27', 'C>27', 'D>27', '24<=A<27', '24<=B<27', '24<=C<27', '24<=D<27',
         '15<=A<24', '15<=B<24', '15<=C<24', '15<=D<24', 'A<15', 'B<15', 'C<15', 'D<15']
#data cho truc y
trucY=[A_greater_than_27, B_greater_than_27, C_greater_than_27, D_greater_than_27,
       A_high_score, B_high_score, C_high_score, D_high_score,
       A_medium_score, B_medium_score, C_medium_score, D_medium_score,
       A_lower_than_15, B_lower_than_15, C_lower_than_15, D_lower_than_15]

total_student=data_new.count()['sbd']
print(total_student)
phan_tram=(trucY/total_student)*100

#Ve bieu do:
plt.bar(trucX,phan_tram)
plt.title('Thành tích học sinh thi các khối A00, B00, C00, D00 ở tỉnh Thái Nguyên(12)')
plt.xlabel('Thành tích học sinh')
plt.ylabel('Số lượng thí sinh')
for index, value in enumerate(phan_tram):
    plt.text(index, value, f'{value:.2f}%', ha='center', va='bottom')
plt.show()



