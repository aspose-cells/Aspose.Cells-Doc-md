---
title: Excel'i OFD Formatına Dönüştürme
linktitle: Excel'i OFD Formatına Dönüştürme
description: Aspose.Cells for Python via .NET, Excel çalışma kitaplarını OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekleyen bir elektronik tablo işleme kütüphanesidir. Bu makale, Aspose.Cells kullanarak Excel içeriği oluşturmayı ve OFD olarak dışa aktarmayı, ayrıca mevcut Excel dosyalarını OFD'ye dönüştürmeyi göstermektedir.
keywords: Aspose.Cells, Python via .NET kütüphanesi, elektronik tablo, Excel'den OFD'ye, OFD dönüşümü, SaveFormat.Ofd, sabit düzenli belge, çalışma kitabı dışa aktarma
type: docs
weight: 195
url: /tr/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, `SaveFormat.Ofd` numaralandırma değerini kullanarak Excel çalışma kitaplarını doğrudan OFD (Open Fixed-layout Document) formatına dönüştürmeyi destekler. Elde edilen OFD belgesi, çalışma kitabının görünür düzenini, içeriğini, birleştirilmiş hücreleri, sütun genişliklerini, satır yüksekliklerini, yazı tiplerini, renkleri, kenarlıkları ve sayı formatlarını korur. Bu, Aspose.Cells'i arşivleme, yazdırma, düzenleyici dosyalama ve sabit düzenli çıktı gerektiren hükümet başvuru iş akışları için uygun hale getirir.

{{% /alert %}}
## **Giriş**
OFD (Open Fixed-layout Document), dijital belgeleri sabit, sayfa tabanlı bir düzende temsil etmek için kullanılan Çin ulusal standardıdır (GB/T 33190-2016). Kaynak belgenin görsel görünümünün tam olarak yazıldığı gibi korunması gereken kullanım durumları için PDF'ye benzer bir rol üstlenir. OFD, Çin Halk Cumhuriyeti'nde hükümet başvuruları, düzenleyici dosyalamalar, elektronik faturalar ve uzun süreli arşivleme için yaygın olarak benimsenmiştir.

Excel çalışma kitaplarını OFD'ye dönüştürmek, elektronik tablo içeriğinin düzenlenebilir bir elektronik tablo olarak değil, salt okunur, düzeni kilitli bir yapıt olarak dağıtılması gereken senaryolarda yaygın bir gereksinimdir. Örnekler arasında, son haline getirilmiş bir faturanın müşteriye gönderilmesi, üç aylık bir mali raporun arşivlenmesi veya bir bütçe elektronik tablosunun düzenleyici bir makama sunulması yer alır. Aspose.Cells, çalışma kitabını ara bir dönüşüm adımı gerektirmeden doğrudan OFD'ye yazan `SaveFormat.Ofd` numaralandırma değeri aracılığıyla bu gereksinimi karşılar. OFD çıktısı, hücre değerlerini, birleştirilmiş aralıkları, yazı tiplerini, renkleri, kenarlıkları, sayı formatlarını ve çalışma kitabında yapılandırılan sayfa düzeni seçeneklerini korur.

{{% alert color="primary" %}}

Aspose.Cells tarafından oluşturulan OFD çıktısı, kaynak çalışma kitabının görünür düzenini korur; buna hücre içeriği, birleştirilmiş hücreler, sütun genişlikleri ve satır yükseklikleri dahildir. Yazı tipleri, renkler, kenarlıklar, hizalama ve sayı formatları gibi hücre biçimlendirmesi de sabit düzenli çıktıda işlenir. Çalışma sayfasında yapılandırılan kağıt boyutu, yönlendirme ve yazdırma alanı gibi sayfa düzeni seçenekleri, ortaya çıkan OFD belgesinin düzenini etkiler.

{{% /alert %}}
## **Excel Çalışma Kitabı Oluşturma ve OFD Olarak Kaydetme**
Aspose.Cells, bir çalışma kitabını programlı olarak oluşturmanıza, verilerle doldurmanıza ve ardından `SaveFormat.Ofd` numaralandırmasını kullanarak doğrudan OFD formatında kaydetmenize olanak tanır. Aşağıdaki örnek sıfırdan bir fatura oluşturur. Bir şirket logosu, başlık bilgileri, fatura alıcı bölümü, satır öğeleri ve hesaplanmış toplamlar ekler, ardından çalışma kitabını bir OFD belgesi olarak dışa aktarır.
### **Logo İçeren Bir Fatura Oluşturma**
Örnek, sol üst alana bir logo görüntüsü ekleyerek, şirket adı ve iletişim bilgilerini doldurarak, birleştirilmiş hücreler arasına bir "FATURA" başlığı ekleyerek, fatura numarasını ve tarihini kaydederek, fatura alıcı müşterisini listeleyerek, açıklama, miktar, birim fiyat ve toplam sütunlarıyla bir satır öğeleri tablosu oluşturarak ve hücre formüllerini kullanarak ara toplam, vergi ve genel toplamı hesaplayarak bir fatura çalışma sayfası oluşturur. Kalın başlıklar, fiyatlar için para birimi formatı, kenarlıklar ve sütun genişlikleri gibi biçimlendirmeler `Style` ve `Font` nesneleri kullanılarak uygulanır. Son olarak, çalışma kitabı `SaveFormat.Ofd` kullanılarak `.ofd` uzantısıyla kaydedilir.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Yeni bir Workbook oluştur
workbook = ac.Workbook()

# İlk çalışma sayfasını al
worksheet = workbook.worksheets[0]

# Sütun genişliklerini ayarla
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Şirket logosunu ekle
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Şirket adı ve iletişim bilgileri
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# FATURA başlığı - hücreleri birleştir
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Fatura numarası ve tarih
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Fatura alıcı bölümü
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# Satır öğeleri başlığı
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Kenarlıklı para birimi stili
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Açıklama/miktar hücreleri için düz kenarlık stili
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Satır öğeleri satırları
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Ara toplam, vergi, genel toplam
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Toplam değerler için kalın + para birimi stili
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Toplam etiketleri için kalın stil
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Workbook'u OFD dosyası olarak kaydet
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Mevcut Bir Excel Dosyasını OFD'ye Dönüştürme**
Aspose.Cells ayrıca disk üzerindeki mevcut bir Excel çalışma kitabını yükleyebilir ve doğrudan OFD formatında dışa aktarabilir. Bu, toplu dönüşüm hatları, arşivleme iş akışları ve kaynak çalışma kitabının başka bir araç tarafından üretildiği ve yalnızca sabit düzenli bir yapıt olarak yeniden yayınlanması gereken senaryolar için kullanışlıdır. Aşağıdaki örnek, mevcut bir `.xlsx` çalışma kitabını yükler, hücrelerinden veri okur, isteğe bağlı sayfa düzeni ayarlamaları uygular ve sonucu bir OFD belgesi olarak kaydeder.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Mevcut bir Excel çalışma kitabını diskten aç
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Dosyanın yüklendiğini onaylamak için seçili hücrelerdeki değerleri oku ve görüntüle
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Mevcut sayfaları listelemek için Worksheets koleksiyonu üzerinde yineleme yap
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) İsteğe bağlı olarak dönüşümü yansıtmak için bir zaman damgası hücresini güncelle
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Veri bloğunun üstüne bir özet başlık satırı ekle
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Çalışma sayfasında PageSetup özelliklerini yapılandır
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) OFD çıktısı için yazdırma alanını isteğe bağlı olarak ayarla
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Çalışma kitabını OFD dosyası olarak kaydet
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **İlgili Makaleler**
- [Excel Dosyalarını Birden Çok Dosyaya Bölme](/cells/tr/python-net/splitting-excel-files-into-multiple-files/)
- [Bir Hücreye Görüntü Ekleme](/cells/tr/python-net/inserting-an-image-into-a-cell/)
- [DBF Dosyalarını Okuma ve Yazma](/cells/tr/python-net/dbf/)
- [Aspose.Cells for Python via .NET'te Sparkline'ı Görüntüye ve HTML'ye Dönüştürme](/cells/tr/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}