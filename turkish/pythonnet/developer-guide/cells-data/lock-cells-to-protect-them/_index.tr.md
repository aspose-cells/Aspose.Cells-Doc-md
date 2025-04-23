---
title: Python.NET ile Hücreleri Kilitle ve Koruma Sağla
linktitle: Hücreleri Kilitle ve Koruma Sağla
type: docs
weight: 130
url: /tr/python-net/how-to-lock-cells-to-protect-them/
description: Aspose.Cells for Python kullanarak Excel dosyalarında belirli hücreleri nasıl kilitleneceği ve çalışma sayfalarının nasıl korunacağı hakkında bilgi edinin via .NET.
keywords: Python ile hücreleri kilitle, çalışma sayfalarını koru, Excel de hücre koruması hakkında Python eğitimi
---

## **Olası Kullanım Senaryoları**
Hücreleri korumak için kilitlemek, Microsoft Excel veya Google Sheets gibi elektronik tablo uygulamalarında sık kullanılan önemli bir uygulamadır çünkü birçok önemli nedeni vardır:

1. Kazara Değişiklikleri Önleme: Hücreleri kilitlemek, kullanıcıların önemli verileri veya formülleri kazara değiştirmesini engeller.
2. Veri Bütünlüğünü Koruma: Kritik verilerin tutarlı ve doğru kalmasını sağlar.
3. Kontrollü Erişim: İşbirliği ortamlarında düzenleme izinlerini yönetin.
4. Formülleri Koruma: Önemli hesaplamaların değiştirilmesini önle
5. İş Kurallarını Zorunlu Kılma: Veri koruma gereksinimlerine uyum sağla.
6. Kullanıcıları Yönlendirme: Karmaşık elektronik tablolarda net düzenlenebilir alanlar sağla.

## **Excel'de Hücreleri Kilitleyerek Nasıl Korumak Yapılır**
İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Kilitlenecek Hücreleri Seçin: Hücreleri seçin veya tüm sayfayı kilitlemek için geçin.
1. Hücreleri Biçim Penceresini Açın: Sağ tık > "Hücreleri Biçimlendir" veya Ctrl+1.
<br>
<img src="1.png" width=60% />
1. Hücreleri Kilitle: "Koruma" sekmesine gidin > "Kilitle" kutusunu işaretleyin > "Tamam" butonuna tıklayın.
1. Çalışma Sayfasını Koru: "İnceleme" sekmesi > "Sayfayı Koru" > Şifre/İzinleri ayarla > "Tamam" butonuna tıkla.
<br>
<img src="2.png" width=60% />

## **Python Kullanarak Hücreleri Korumak İçin Nasıl Kilitlenir**

Aspose.Cells for Python via .NET programatik hücre korumasını sağlar. Bu adımları izleyin:
1. [Örnek dosyayı](sample.xlsx) yükleyin
2. Tüm hücreleri kilidini açın (varsayılan kilitli durum, koruma olmadan uygulanmaz)
3. Belirli hücreleri kilitleyin
4. Kilitlemeyi sağlamak için çalışma sayfasını koruyun

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **Sonuç Çıktısı**
Bu uygulama, belirli hücreleri (A1 ve B2) kilitlerken diğerlerini düzenlenebilir tutar. Çalışma sayfası koruması bu ayarları uygular.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
