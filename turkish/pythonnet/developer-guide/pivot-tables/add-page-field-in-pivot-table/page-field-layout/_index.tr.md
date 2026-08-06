---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Python via .NET kullanarak bir pivot tabloda sayfa alanı bölgesinin düzenini nasıl kontrol edeceğinizi öğrenin. Buna pivot tablonun üst kısmındaki sayfa alanlarının görüntüleme sırası, sarma sayısı ve alan sırasının ayarlanması dahildir.
keywords: Aspose.Cells, Python via .NET kitaplığı, elektronik tablo, pivot tablo, sayfa alanı, sayfa alanı sırası, sayfa alanı sarma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Sayfa alanı bölgesinin — pivot tablonun üst kısmındaki filtre kontrolleri şeridinin — düzenini, görüntüleme sırası, sarma sayısı ve alan yeniden sıralaması dahil olmak üzere nasıl kontrol edileceğini gösterir.
{{% /alert %}}
## **Giriş**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde yer alan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, açılır filtre kontrollerinden oluşan bir şerit (her sayfa alanı için bir tane) olarak işlenir ve son kullanıcıların pivot tabloyu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells for Python via .NET bu bölgeyi `pivot_table.page_fields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl yerleştirileceğini kontrol eden üç özellik sunar:
- `pivot_table.page_field_order` (bir `PrintOrderType` değeri), ek sayfa alanlarının mevcut alanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `pivot_table.page_field_wrap_count`, kaydırmadan önce satır veya sütun başına kaç sayfa alanı yerleştirileceğini ayarlar.
- `pivot_table.page_fields.move(curr_index, dest_index)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, ortak bir veri kümesi üzerinde bu işlemlerin her birini gösteren üç kod örneğini adım adım açıklar; böylece ortaya çıkan düzenleri yan yana karşılaştırabilirsiniz.
## **Kaynak Veri**
Aşağıdaki üç örnek de bu sekiz satırlık satış verisini `PivotData` adlı bir çalışma sayfasına yükler. Veri, iki sayfa alanı adayı (`Year`, `Region`), bir satır alanı adayı (`Fruit`) ve bir ölçü (`Amount`) içerir; bu da sayfa alanı şeridinin incelenmesini anlamlı kılar.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Her kod örneğinde, aynı sırada olmak üzere, sekiz satırın tamamı doldurulur; böylece kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.
## **Örnek 1: Yukarı Sonra Aşağı**
İlk senaryoda, iki sayfa alanını (`Year`, `Region`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırırız. `Fruit` öğesini satır eksenine atarız, `Year` öğesini sayfa ekseninde birinci, `Region` öğesini ise ikinci sıraya yerleştiririz (`add_field_to_area` çağrılarının sırası başlangıç dizinini belirler), `Amount` (Sum) öğesini veri alanı olarak ekleriz ve ardından `page_field_order` öğesini `PrintOrderType.OverThenDown` olarak, `page_field_wrap_count` öğesini ise `2` olarak ayarlarız. `OverThenDown` ve sarma sayısı 2 ile, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; dolayısıyla şerit iki genişliğinde tek bir satır kaplar.
```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Başlıklar (satır 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Satır 1: Apple, 2022, North, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Satır 2: Apple, 2023, North, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Satır 3: Banana, 2022, South, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Satır 4: Banana, 2023, South, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Satır 5: Cherry, 2022, East, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Satır 6: Cherry, 2023, East, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Satır 7: Grape, 2022, West, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Satır 8: Grape, 2023, West, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# PivotTableReport sayfasını ekle
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# PivotData!A1:D9 kaynaklı ve PivotTableReport üzerinde A1 hücresine yerleştirilmiş pivot tablo oluştur
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Alanları ekle
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Fruit
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Year
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Region
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Amount
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Sayfa alanı düzenini yapılandır: sayfa alanlarını önce yatay yerleştir, her 2 alandan sonra satır kaydır
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Yenile ve hesapla
pivot_table.calculate_data()

# Kaydet
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```
## **Örnek 2: Aşağı Sonra Yukarı**
Bu örnekte `Fruit` öğesini satır eksenine, `Year` ve `Region` öğelerini sayfa eksenine (`Year` birinci sırada olacak şekilde) ve `Amount` (Sum) öğesini veri alanı olarak yerleştiririz — tıpkı Örnek 1'deki gibi. Ardından `page_field_order` öğesini `PrintOrderType.DownThenOver`, `page_field_wrap_count` öğesini ise `2` olarak ayarlarız. `DownThenOver` ve sarma sayısı 2 ile, iki sayfa alanı dikey olarak üst üste yığılır — `Year` üstte, `Region` doğrudan altında — ve pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, bir genişliğinde iki satır kaplar.
```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```
## **Örnek 3: Bir Sayfa Alanını Taşıma**
Üçüncü senaryoda bu veri kümesini ve alan atamasını koruruz, nötr bir düzen (`OverThenDown` ve sarma sayısı `2`) ayarlarız ve ardından `page_fields.move` işlemini gösteririz. `move(0, 1)` çağrısı, dizin 0'daki (`Year`) sayfa alanını 1 konumuna taşır ve 1 konumunda bulunan (`Region`) sayfa alanı 0 konumuna kayar. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Sarma ve sıra modu değişmediğinden, şerit hâlâ yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.
```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```
## **İlgili Makaleler**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-net/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan ana sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/python-net/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan şekilde, alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/python-net/manage-value-fields/) — bu makalede kullanılan `Sum` toplama işlemi dahil olmak üzere veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `refresh_data` ve `calculate_data` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.
{{< app/cells/assistant language="python-net" >}}