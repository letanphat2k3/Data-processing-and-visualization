import csv
from file_tach import read_csv, write_csv

import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn đến tệp CSV gốc
duong_dan_tep_csv = r"H:\My Drive\workspace3\python_GK\diem_thi_thpt_2022.csv"

# Tên các tệp mới chứa kết quả sau khi lọc
tep_loc_10_Lang_Son = "H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_10_Lang_Son.csv"
tep_loc_11_Bac_Kan = "H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_11_Bac_Kan.csv"
tep_loc_12_Thai_Nguyen = "H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_12_Thai_Nguyen.csv"
tep_loc_13_Yen_Bai = "H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_13_Yen_Bai.csv"
tep_loc_14_Son_La = "H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_14_Son_La.csv"

def main():
    # Đọc dữ liệu từ tệp CSV
    header, du_lieu = read_csv(duong_dan_tep_csv)

    # Lọc dữ liệu theo điều kiện
    du_lieu_loc_10 = [dong for dong in du_lieu if dong[0].startswith("10")]
    du_lieu_loc_11 = [dong for dong in du_lieu if dong[0].startswith("11")]
    du_lieu_loc_12 = [dong for dong in du_lieu if dong[0].startswith("12")]
    du_lieu_loc_13 = [dong for dong in du_lieu if dong[0].startswith("13")]
    du_lieu_loc_14 = [dong for dong in du_lieu if dong[0].startswith("14")]

    # Ghi dữ liệu vào các tệp mới
    write_csv(tep_loc_10_Lang_Son, header, du_lieu_loc_10)
    write_csv(tep_loc_11_Bac_Kan, header, du_lieu_loc_11)
    write_csv(tep_loc_12_Thai_Nguyen, header, du_lieu_loc_12)
    write_csv(tep_loc_13_Yen_Bai, header, du_lieu_loc_13)
    write_csv(tep_loc_14_Son_La, header, du_lieu_loc_14)

# Đọc dữ liệu mới từ tệp CSV
    data = pd.read_csv(r'H:\My Drive\workspace3\python_GK\danh_sach_thi_sinh_10_Lang_Son.csv')
    data_new = data.fillna(0)
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
    plt.title('Số học sinh có thành tích xuất sắc tỉnh Lạng Sơn(10)')
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=140)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()