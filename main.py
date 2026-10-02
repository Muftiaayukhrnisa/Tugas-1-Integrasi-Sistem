from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    title="API Data Mahasiswa",
    description="API untuk Tugas 1 Integrasi Sistem",
    version="1.0.0"
)


# Model data mahasiswa
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str


# Data sementara
data_mahasiswa = [
    {
        "id": 1,
        "nama": "Muftia Ayu Khoirunnisa",
        "alamat": "Semarang",
        "ipk": 3.75,
        "semester": 5,
        "hobi": "Membaca"
    }
]


# GET - mengambil semua data mahasiswa
@app.get("/mahasiswa")
def get_mahasiswa():
    return data_mahasiswa


# GET berdasarkan ID
@app.get("/mahasiswa/{mahasiswa_id}")
def get_mahasiswa_by_id(mahasiswa_id: int):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["id"] == mahasiswa_id:
            return mahasiswa

    raise HTTPException(
        status_code=404,
        detail="Data mahasiswa tidak ditemukan"
    )


# POST - menambahkan data mahasiswa
@app.post("/mahasiswa")
def tambah_mahasiswa(mahasiswa: Mahasiswa):

    id_baru = len(data_mahasiswa) + 1

    data_baru = {
        "id": id_baru,
        "nama": mahasiswa.nama,
        "alamat": mahasiswa.alamat,
        "ipk": mahasiswa.ipk,
        "semester": mahasiswa.semester,
        "hobi": mahasiswa.hobi
    }

    data_mahasiswa.append(data_baru)

    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "data": data_baru
    }


# PUT - mengubah data mahasiswa
@app.put("/mahasiswa/{mahasiswa_id}")
def update_mahasiswa(mahasiswa_id: int, mahasiswa: Mahasiswa):

    for data in data_mahasiswa:
        if data["id"] == mahasiswa_id:

            data["nama"] = mahasiswa.nama
            data["alamat"] = mahasiswa.alamat
            data["ipk"] = mahasiswa.ipk
            data["semester"] = mahasiswa.semester
            data["hobi"] = mahasiswa.hobi

            return {
                "message": "Data mahasiswa berhasil diperbarui",
                "data": data
            }

    raise HTTPException(
        status_code=404,
        detail="Data mahasiswa tidak ditemukan"
    )


# DELETE - menghapus data mahasiswa
@app.delete("/mahasiswa/{mahasiswa_id}")
def delete_mahasiswa(mahasiswa_id: int):

    for mahasiswa in data_mahasiswa:
        if mahasiswa["id"] == mahasiswa_id:

            data_mahasiswa.remove(mahasiswa)

            return {
                "message": "Data mahasiswa berhasil dihapus"
            }

    raise HTTPException(
        status_code=404,
        detail="Data mahasiswa tidak ditemukan"
    )