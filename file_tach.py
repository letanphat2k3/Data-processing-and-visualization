import csv

def read_csv(duong_dan):
    with open(duong_dan, "r") as tep:
        doc_gia = csv.reader(tep)
        header = next(doc_gia)
        du_lieu = [dong for dong in doc_gia]

    return header, du_lieu

def write_csv(duong_dan, header, du_lieu):
    with open(duong_dan, "w", newline='') as tep:
        viet_giai = csv.writer(tep)
        viet_giai.writerow(header)
        viet_giai.writerows(du_lieu)
