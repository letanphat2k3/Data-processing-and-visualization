import csv

# Duong dan toi tep CSV goc
duong_dan_tep_csv = r"C:\Users\Dell\Documents\Code\Study\Python\Buoi7\diem_thi_thpt_2022.csv"

# Ten tep moi chua ket qua sau khi loc
tep_loc = "Tep_so_21_da_loc.csv"

# Mo va doc tep CSV goc
with open(duong_dan_tep_csv, "r") as tep:
    # Su dung csv.reader de doc tung dong trong tep
    doc_gia = csv.reader(tep)

    # Lay dong dau tien
    header = next(doc_gia)

    # Loc cac dong theo dieu kien gia tri o cot dau tien bat dau bang "21"
    du_lieu_loc = [dong for dong in doc_gia if dong[0].startswith("21")]

# Mo va ghi tep moi chua ket qua sau khi loc
with open(tep_loc, "w", newline='') as tep:
    # Su dung csv.writer de viet du lieu vao tep
    viet_giai = csv.writer(tep)

    # Ghi header
    viet_giai.writerow(header)

    # Ghi tat ca cac dong da loc vao tep moi
    viet_giai.writerows(du_lieu_loc)
