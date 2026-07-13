---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells for Python via Java, OFD (Open Fixed-layout Document) formatına Excel çalışma kitaplarını dönüştürmeyi destekleyen, elektronik tablo dosyalarıyla çalışmaya yönelik bir kütüphanedir. Bu makale, Aspose.Cells for Python via Java kullanarak Excel içeriği oluşturmayı ve bunu OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, Python via Java kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java, `SaveFormat.Ofd` sabit değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekler. Elde edilen OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücrelerini, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renklerini, kenarlıklarını ve sayı biçimlerini korur. Bu, Aspose.Cells for Python via Java'yı arşivleme, yazdırma, düzenleyici dosyalama ve sabit düzenli çıktı gerektiren hükümet başvuru iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı şekliyle korunması gereken kullanım durumlarında PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde hükümet başvuruları, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir yapı olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında sonlandırılmış bir faturanın müşteriye gönderilmesi, üç aylık bir finansal raporun arşivlenmesi veya bir bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells for Python via Java, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` sabit değeri aracılığıyla bu gereksinimi karşılar. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı biçimlerini ve çalışma kitabında yapılandırılmış sayfa yapısı seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells for Python via Java tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini korur; buna hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahildir. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı biçimleri gibi hücre biçimlendirmeleri de sabit düzenli çıktıda işlenir. Çalışma sayfasında yapılandırılmış sayfa yapısı seçenekleri (kağıt boyutu, yönlendirme ve yazdırma alanı gibi) ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells for Python via Java, bir çalışma kitabını programlı olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` sabit değerini kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura alıcı bölümü, kalem satırları ve hesaplanmış toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.
### **Logo İçeren Bir Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek bir fatura çalışma sayfası oluşturur; şirket adını ve iletişim bilgilerini doldurur, birleştirilmiş hücreler arasına bir "INVOICE" (FATURA) başlığı ekler, fatura numarasını ve tarihini kaydeder, fatura alıcısı müşterisini listeler, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir kalem satırları tablosu oluşturur ve hücre formülleri kullanarak ara toplam, vergi ve genel toplamı hesaplar. Kalın başlıklar, fiyatlar için para birimi biçimi, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Yeni bir Çalışma Kitabı oluştur
workbook = Workbook()

# İlk çalışma sayfasını al
worksheet = workbook.getWorksheets().get(0)

# Sütun genişliklerini ayarla
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Şirket logosunu ekle
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Şirket adı ve iletişim bilgileri
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# FATURA başlığı - hücreleri birleştir
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Fatura numarası ve tarih
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Fatura kesilen kişi bölümü
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Kalem başlıkları
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Kenarlıklı para birimi stili
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Açıklama/miktar hücreleri için düz kenarlık stili
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Kalem satırları
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# Ara toplam, vergi, genel toplam
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Toplam değerler için kalın + para birimi stili
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Toplam etiketleri için kalın stil
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells for Python via Java ayrıca disk üzerindeki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatına dışa aktarabilir. Bu, toplu dönüştürme işlem hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araçla üretildiği ve yalnızca sabit düzenli bir yapı olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa yapısı ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Diskteki mevcut bir Excel çalışma kitabını aç
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Dosyanın yüklendiğini onaylamak için seçili hücrelerden değerleri oku ve görüntüle
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yineleme yap
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) İsteğe bağlı olarak dönüşümü yansıtmak için bir zaman damgası hücresini güncelle
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Veri bloğunun en üstüne bir özet başlık satırı ekle
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) İsteğe bağlı olarak OFD çıktısı için yazdırma alanını ayarla
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/python-java/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/python-java/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/python-java/dbf/)
- [Aspose.Cells for Python via Java'da Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}