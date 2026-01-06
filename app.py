from tensorboard import summary
import webview
from summarizer import summarize
from notulen_generator import generate_keputusan, generate_tindak_lanjut
from datetime import datetime

class Api:
    def generate(self, text):
        ringkasan = summarize(text)
        keputusan = generate_keputusan(ringkasan)
        tindak_lanjut = generate_tindak_lanjut(keputusan)

        tanggal = datetime.now().strftime("%d %B %Y")

        hasil = f"""NOTULEN RAPAT

Tanggal : {tanggal}

RINGKASAN RAPAT
{ringkasan}

KEPUTUSAN RAPAT
"""
        for k in keputusan:
            hasil += f"- {k}\n"

        hasil += "\nTINDAK LANJUT\n"
        for t in tindak_lanjut:
            hasil += f"- {t}\n"

        return hasil


if __name__ == "__main__":
    webview.create_window(
        "Asisten Notulen Rapat",
        "ui.html",
        js_api=Api(),
        width=900,
        height=700
    )
    webview.start()
