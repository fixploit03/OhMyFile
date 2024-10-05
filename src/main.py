import hashlib

def calculate_all_hashes(file_path):
    # Daftar algoritma hash yang ingin dihitung
    hash_algorithms = ['md5', 'sha1', 'sha256', 'sha512']

    # Membuat objek hash untuk setiap algoritma
    hash_funcs = {algo: hashlib.new(algo) for algo in hash_algorithms}

    try:
        with open(file_path, 'rb') as file:
            # Membaca file dalam blok
            while chunk := file.read(8192):
                for func in hash_funcs.values():
                    func.update(chunk)

        # Menampilkan hasil hash dalam format heksadesimal untuk setiap algoritma
        for algo, func in hash_funcs.items():
            print(f"[+] {algo.upper()} hash dari file {file_path}: {func.hexdigest()}")

    except FileNotFoundError:
        print(f"[!] File {file_path} tidak ditemukan.")
    except PermissionError:
        print(f"[!] Tidak memiliki izin untuk membuka file {file_path}.")
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    file_path = input("[#] Masukkan path file: ")
    calculate_all_hashes(file_path)
  
