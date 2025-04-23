---
title: Python.NET kullanarak Sayfa Çalışma Sayfasını Ölçeklendirme Nasıl Yapılır
linktitle: Sayfa Çalışma Sayfasını Nasıl Ölçeklendirilir
type: docs
weight: 130
url: /tr/python-net/how-to-scale-a-worksheet/
description: Bu makale, Aspose.Cells for Python.NET kullanarak çalışma sayfasını nasıl ölçeklendireceğinizi açıklar.
keywords: Python da çalışma sayfasını ölçeklendirme, Python.NET ile çalışma sayfasını ölçeklendirme, Python da sayfa sığdırma, Python da çalışma sayfası ölçeklendirme yüzdesi, Aspose.Cells Python çalışma sayfası ölçeklendirme.
---

## **Olası Kullanım Senaryoları**
Çalışma sayfasını ölçeklendirmek, çalıştığınız bağlama bağlı olarak çeşitli yarar sağlayabilir. İşte birkaç yaygın neden:
1. **Sayfaya Sığdır**: Yazdırırken tüm içeriğin tek bir sayfaya veya belirli sayfa sayısına sığmasını sağlamak.
1. **Sunum**: Paylaşmak için düzenli ve profesyonel görünümlü çalışma sayfaları oluşturmak.
1. **Okunabilirlik**: Metin ve öğe boyutlarını daha iyi görsel erişilebilirlik için ayarlamak.
1. **Alan Yönetimi**: Çalışma sayfası düzenini optimize etmek ve gereksiz beyaz alanı minimize etmek.
1. **Veri Görselleştirme**: Grafik ve çizelgeleri uygun şekilde boyutlandırmak.
1. **Tutarlılık**: Birden fazla çalışma sayfası veya belge arasında tutarlı görünüm sağlamak.

## **Excel'de Çalışma Sayfasını Nasıl Ölçeklendirilir**
Excel'de çalışma sayfasını ölçeklendirmek, içeriğin yazdırıldığında belirlenen sayfalara sığmasını sağlar. İşte adımlar:

1. Excel'de çalışma sayfanızı açın
1. **Sayfa Düzeni** > **Sığdırma Ölçeği** grubuna gidin
1. Sayfa sayısı gereksinimlerine göre **Genişlik** ve **Yükseklik** ayarlayın
1. Gerekirse özel ölçeklendirme yüzdesi belirleyin
<br>
<img src="1.png" width=60% />

## **Python.NET kullanarak Çalışma Sayfasını Ölçeklendirme Nasıl Yapılır**
Aspose.Cells for Python.NET kapsamlı çalışma sayfası ölçeklendirme yetenekleri sağlar. İşte programlı olarak çalışma sayfalarını ölçeklendirmek için yaklaşımlar:

### **Sayfa Sığdırma Örneği**
Yazdırma ayarlarını belirtilen sayfalara uygun hale getirmek için ayarlayın:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Yüzdeye Göre Ölçeklendirme Örneği**
Çalışma sayfası içeriğine özel ölçeklendirme yüzdesi uygulayın:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Ana API Referansları:**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfı
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) sınıfı
- [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) yapılandırması
