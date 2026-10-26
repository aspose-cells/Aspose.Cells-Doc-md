---
title: Aspose.Cells for Python via .NET ile Pivot Tablolarına Stil Uygulama
linktitle: Aspose.Cells for Python via .NET ile Pivot Tablolarına Stil Uygulama
description: Aspose.Cells for Python via .NET'te yerleşik ve özel stilleri pivot tablolarına nasıl uygulayacağınızı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve _format_all kısayolu dahil.
keywords: Aspose.Cells Python via .NET pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği formata bağlıdır.
{{% /alert %}}

## **Giriş**
Aspose.Cells, pivot tabloları için iki paralel stil API'si sunar. Aralarındaki seçim, okuduğunuz formata değil, çalışma kitabını kaydettiğiniz formata göre belirlenir. `.xls` dosyasından yüklenen bir çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si değil, modern stil API'si geçerli olur.
- `PivotTable.pivot_table_style_type`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar dahil, Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.pivot_table_style_name`, `workbook.worksheets.table_styles.add_pivot_table_style(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renkler, kenarlıklar veya yazı tipleri istediğinizde özel stiller gereklidir.
Buna ek olarak, `PivotTable.format_all(Style)`, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden herhangi biri ile ayarlananları geçersiz kılan bir kısayoldur. Bu, alttaki temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski Bir XLS Ön Ayarı Otomatik Biçimi Uygulama**
`PivotTable.auto_format_type`, `aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1`'den `REPORT_10`'a, `CLASSIC` ve `TABLE_1`'den `TABLE_10`'a kadardır.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablo ekler, `PivotTableAutoFormatType.REPORT5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Rapor serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu pivot tablolar** için tasarlanmıştır — sütun alanı başlıkları için yerleşik stillendirme sunmazlar. Pivotunuz sütun alanlarına ihtiyaç duyuyorsa, bunun yerine modern Excel'in iki boyutlu düzeni için tasarlanmış olan [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) içindeki modern `PivotTableStyleType` ön ayarlarını kullanın.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotTableAutoFormatType
# Senaryo 1: Eski bir XLS ön ayar otomatik biçimi uygula
# Kullanılan API: PivotTable.AutoFormatType
# Hedef dosya formatı: .xls (eski)
# Tam örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin
# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
# İlk çalışma sayfasını al
sheet = workbook.worksheets[0]
# Başlık satırı (Fruit, Year, Amount) ile kaynak verileri doldur
# ve 2020 ve 2021 yıllarını kapsayan grape, blueberry, kiwi, cherry için 9 veri satırı
sheet.cells.get(0, 0).put_value("Fruit")
sheet.cells.get(0, 1).put_value("Year")
sheet.cells.get(0, 2).put_value("Amount")
sheet.cells.get(1, 0).put_value("grape")
sheet.cells.get(1, 1).put_value(2020)
sheet.cells.get(1, 2).put_value(50)
sheet.cells.get(2, 0).put_value("blueberry")
sheet.cells.get(2, 1).put_value(2020)
sheet.cells.get(2, 2).put_value(30)
sheet.cells.get(3, 0).put_value("kiwi")
sheet.cells.get(3, 1).put_value(2020)
sheet.cells.get(3, 2).put_value(25)
sheet.cells.get(4, 0).put_value("cherry")
sheet.cells.get(4, 1).put_value(2020)
sheet.cells.get(4, 2).put_value(40)
sheet.cells.get(5, 0).put_value("grape")
sheet.cells.get(5, 1).put_value(2021)
sheet.cells.get(5, 2).put_value(60)
sheet.cells.get(6, 0).put_value("blueberry")
sheet.cells.get(6, 1).put_value(2021)
sheet.cells.get(6, 2).put_value(35)
sheet.cells.get(7, 0).put_value("kiwi")
sheet.cells.get(7, 1).put_value(2021)
sheet.cells.get(7, 2).put_value(28)
sheet.cells.get(8, 0).put_value("cherry")
sheet.cells.get(8, 1).put_value(2021)
sheet.cells.get(8, 2).put_value(45)
sheet.cells.get(9, 0).put_value("grape")
sheet.cells.get(9, 1).put_value(2020)
sheet.cells.get(9, 2).put_value(45)
# E3 hedef hücresinde, adında, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
pivot_table = sheet.pivot_tables.add("A1:C10", 2, 4)
# Alanları ata: Fruit -> Satırlar, Amount -> Veri
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Eski XLS ön ayar otomatik biçimi "Report5" uygula
# Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
# .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType'ı yok sayar
# ve PivotTableStyleType / PivotTableStyleName'de belirtileni kullanır.
pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
# Çalışma kitabını eski .xls formatında kaydet
workbook.save("output.xls")
```

## **Modern Adlandırılmış Bir Ön Ayar Pivot Tablo Stilini Uygulama**
`pivot_table.pivot_table_style_type`, Excel 2007’in pivot tabloları için tanıttığı yerleşik adlandırılmış stillerden birini seçer. `PivotTableStyleType` numaralandırması üç tema ailesini ortaya çıkarır: `PIVOT_TABLE_STYLE_LIGHT1`’den `PIVOT_TABLE_STYLE_LIGHT28`’e kadar olan açık ailesi, `PIVOT_TABLE_STYLE_MEDIUM1`’den `PIVOT_TABLE_STYLE_MEDIUM28`’e kadar olan orta ailesi ve `PIVOT_TABLE_STYLE_DARK1`’den `PIVOT_TABLE_STYLE_DARK28`’e kadar olan koyu ailesi. Ayrıca `None` ve `Custom` değerlerini de tanımlar. Her ailenin daha yüksek numaralı üyeleri Excel 2017’ye eklenen stillerdir.
Bu ön ayarlar salt-okunurdur. Bir ön ayarın sunduğu imkanlar ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmeniz gerektiğinde, bunun yerine [Senaryo 3](#define-and-apply-a-custom-pivot-table-style)’te gösterildiği gibi özel bir pivot stili tanımlamanız gerekir.

{{% alert color="primary" %}}
**Neden modern ön ayarlar ve rapor serisi otomatik biçimlendirmeleri değil?** `PivotTableAutoFormatType`’ın `Report1`’den `Report10`’a ve `Table1`’den `Table10`’a kadar olan değerleri, pivot sütun alanlarından önce gelmiştir, dolayısıyla sütun alanı başlıkları için herhangi bir stillendirme içermez ve Excel bu başlıkları stillendirilmemiş olarak işler. `PivotTableStyleType` ön ayarları ise modern Excel’in kullandığı iki boyutlu düzen için tasarlanmıştır ve hem satır alanı hem de sütun alanı başlıklarını stillendirir.
{{% /alert %}}

Bu senaryo, Senaryo 1’in meyve/yıl/miktar veri kümesini kullanır, `Fruit` satır alanı yanında `PivotFieldType.COLUMN` aracılığıyla `Year` değerini sütun alanına ekler, koyu tema ön ayarını olan `PIVOT_TABLE_STYLE_DARK1`’i `pivot_table.pivot_table_style_type` ile uygular ve sonucu `.xlsx` olarak kaydeder — bu format, `PivotTableStyleType`’ın anlamlı olduğu formattır.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotTableStyleType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. PivotTableStyleType lives in aspose.cells.pivot,
# so it is imported explicitly alongside PivotFieldType.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Header row: Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(180)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(120)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(170)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(210)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(190)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(130)
# Add a pivot table at E3, sourced from A1:C10
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PIVOT_TABLE_STYLE_DARK1 belongs to the dark-theme
# family (PIVOT_TABLE_STYLE_DARK1..PIVOT_TABLE_STYLE_DARK28), and the same enum also exposes
# the newer Excel 2017 themes (PIVOT_TABLE_STYLE_LIGHT1..LIGHT28 / DARK1..DARK28).
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
```

## **Özel Bir Pivot Tablo Stilini Tanımlama ve Uygulama**
Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde, özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:
1. `workbook.worksheets.table_styles.add_pivot_table_style(name)` aracılığıyla çalışma kitabının `table_styles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `table_style.table_style_elements.add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WHOLE_TABLE` veya `GRAND_TOTAL_ROW`) ekleyerek stili yapılandırın, ardından `table_style_element.set_element_style(Style)` ile her öğeye bir `Style` atayın.
3. `PivotTable.pivot_table_style_name` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `pivot_table_style_type` kullanmayın, çünkü bu özellik yerleşik ön ayarları seçer.

{{% alert color="primary" %}}
`pivot_table_style_name` ve `pivot_table_style_type` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `pivot_table_style_type`, `add_pivot_table_style` aracılığıyla tanımladığınız özel stiller için `pivot_table_style_name` kullanın. Her ikisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.
Kullanılabilir `TableStyleElementType` değerleri arasında `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES` bulunur.
Aşağıdaki örnek, `WHOLE_TABLE` üzerinde ince siyah kenarlık ve `GRAND_TOTAL_ROW` üzerinde koyu kırmızı kalın yazı tipi içeren özel bir pivot stili tanımlar, ardından bunu `pivot_table_style_name` aracılığıyla uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.tables import TableStyleElementType
from aspose.pydrawing import Color
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(500)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(600)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(700)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(800)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(900)
# A1:C10'dan kaynaklanan, E3'e yerleştirilen ve adında bir pivot tablo ekle
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
whole_table_element_index = table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).color = Color.black
whole_table_element.set_element_style(whole_table_style)
# Adım 3: bir GrandTotalRow öğesi ekle ve kırmızı kalın yazı tipi uygula
grand_total_element_index = table_style.table_style_elements.add(TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = Color.red
grand_total_element.set_element_style(grand_total_style)
# Adım 4: özel stili ada göre uygula (PivotTableStyleType ile DEĞİL, bu yerleşik ön ayarlar içindir)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **format_all ile Her Pivot Hücresine Tek Bir Stil Uygulama**
`PivotTable.format_all(Style)`, tek bir `Style` nesnesini pivot tablonun veri alanı, satır ve sütun başlıkları ve toplamlar dahil her hücresine uygulayan bir kısayoldur. Daha önce `pivot_table_style_type` veya `pivot_table_style_name` aracılığıyla ayarlanan her şey geçersiz kılınır.

{{% alert color="primary" %}}
`format_all`, hem `pivot_table_style_type` hem de `pivot_table_style_name` öğelerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.
Aşağıdaki örnek, sarı düz dolgu, koyu mavi kalın yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `format_all` ile uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```python
from aspose.pydrawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Senaryo 4: format_all kullanarak her pivot tablo hücresine tek bir Stil uygulama
# Kullanılan API: PivotTable.format_all(Style)
# Hedef format: .xlsx
# GitHub referansı: Aspose.Cells-for-.NET deposuna bakın — pivot tablo stil örnekleri
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(5000)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(3000)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(4000)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(2000)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(6000)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(3500)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(4500)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(2500)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(5500)
# Pivot tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, ad
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Pivot tablonun her hücresine zorla uygulanacak bir Stil oluştur
style = workbook.create_style()
style.foreground_color = Color.yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.dark_blue
style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.TOP_BORDER).color = Color.black
style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.BOTTOM_BORDER).color = Color.black
style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.LEFT_BORDER).color = Color.black
style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.RIGHT_BORDER).color = Color.black
# format_all uygula: bu tek stili pivot tablonun her hücresine zorlar,
# daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivot_table.format_all(style)
# Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx")
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir referans için aşağıdaki tabloyu kullanın.
| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.auto_format_type` | `aspose.cells.pivot.PivotTableAutoFormatType` değerleri (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern formatlara kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.pivot_table_style_type` | `aspose.cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `table_style_element.set_element_style(...)` aracılığıyla yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `PivotTable.format_all(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `pivot_table_style_type` veya özel temalar için `pivot_table_style_name` kullanın.

{{< app/cells/assistant language="python-net" >}}