def generate_keputusan(summary):
    keputusan = []

    if "menyepakati" in summary or "disepakati" in summary or "sepakat" in summary:
        keputusan.append(
            "Peserta rapat menyepakati hasil pembahasan yang telah dibahas bersama."
        )

    if "dilaksanakan" in summary or "pelaksanaan" in summary or "kegiatan" in summary:
        keputusan.append(
            "Kegiatan yang dibahas dalam rapat disepakati untuk dilaksanakan sesuai rencana."
        )

    if "tanggal" in summary or "jadwal" in summary or "tgl" in summary or "hari" in summary:
        keputusan.append(
            "Waktu dan jadwal pelaksanaan kegiatan telah ditetapkan."
        )

    if "tempat" in summary or "lokasi" in summary or "bertempat" in summary:
        keputusan.append(
            "Lokasi pelaksanaan kegiatan telah ditentukan sesuai hasil rapat."
        )

    if "pembagian tugas" in summary or "tugas" in summary or "divisi" in summary:
        keputusan.append(
            "Pembagian tugas dan tanggung jawab panitia telah disepakati."
        )

    if "panitia" in summary or "divisi" in summary or "dibentuk" in summary:
        keputusan.append(
            "Panitia atau divisi pelaksana kegiatan telah dibentuk."
        )

    if "ketua" in summary or "koordinator" in summary:
        keputusan.append(
            "Ketua atau koordinator kegiatan telah ditunjuk melalui kesepakatan rapat."
        )

    if "monitoring" in summary or "evaluasi" in summary or "pemantauan" in summary:
        keputusan.append(
            "Pelaksanaan kegiatan akan dilakukan monitoring dan evaluasi secara berkala."
        )

    if not keputusan:
        keputusan.append(
            "Belum terdapat keputusan yang ditetapkan dalam rapat ini."
        )

    return keputusan

def generate_tindak_lanjut(keputusan):
    tindak_lanjut = []

    for k in keputusan:
        k = k.lower()

        if "tugas" in k or "divisi" in k or "panitia" in k:
            tindak_lanjut.append(
                "Setiap pihak yang terlibat menjalankan peran dan tanggung jawab masing-masing."
            )

        if "jadwal" in k or "tanggal" in k or "hari" in k or "waktu" in k:
            tindak_lanjut.append(
                "Pihak terkait menyesuaikan persiapan sesuai waktu yang telah ditetapkan."
            )

        if "kegiatan" in k or "pelaksanaan" in k:
            tindak_lanjut.append(
                "Seluruh persiapan teknis dilakukan untuk mendukung kelancaran kegiatan."
            )

        if "lokasi" in k or "tempat" in k:
            tindak_lanjut.append(
                "Koordinasi dilakukan untuk memastikan kesiapan sarana dan prasarana."
            )

        if "koordinator" in k or "ketua" in k:
            tindak_lanjut.append(
                "Koordinasi internal dilakukan untuk memastikan progres kegiatan berjalan sesuai rencana."
            )

        if "monitoring" in k or "evaluasi" in k:
            tindak_lanjut.append(
                "Laporan perkembangan kegiatan disampaikan secara berkala kepada pimpinan."
            )

    if not tindak_lanjut:
        tindak_lanjut.append(
            "Menunggu arahan lanjutan dari pihak yang berwenang."
        )

    return tindak_lanjut
