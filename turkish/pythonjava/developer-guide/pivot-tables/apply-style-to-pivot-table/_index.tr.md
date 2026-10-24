---
title: Aspose.Cells for Python via Java'da Pivot Tablolarına Stil Uygulama
linktitle: Aspose.Cells for Python via Java'da Pivot Tablolarına Stil Uygulama
description: Aspose.Cells for Python via Java'da pivot tablolarına yerleşik ve özel stiller uygulamayı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stiller, özel pivot tablosu stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells Python via Java pivot tablosu stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablosu stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya formatına bağlıdır.
{{% /alert %}}

## **Giriş**
Aspose.Cells, pivot tabloları için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını okuduğunuz formata değil, kaydettiğiniz dosya formatına göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski stil API'si yerine modern stil API'si geçerli olur.
- `pivotTable.setPivotTableStyleType(int)`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `pivotTable.setPivotTableStyleName(String)`, `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.
Ayrıca, `pivotTable.formatAll(Style)` kısayolu, tek bir `Style` nesnesini pivotun her hücresine uygular ve yukarıdaki stil adı API'lerinden hangisi ayarlanmış olursa olsun geçersiz kılar. Bu, temel temadan bağımsız tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Ön Ayar Otomatik Biçimi Uygulama**
Bir pivot tablosundaki `setAutoFormatType` yöntemi, `com.aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1` ile `REPORT_10` arası, `CLASSIC` ve `TABLE_1` ile `TABLE_10` arasıdır.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablosu ekler, `PivotTableAutoFormatType.REPORT_5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu pivot tabloları** için tasarlanmıştır ve sütun alanı başlıkları için yerleşik bir stil içermez. Pivotunuz sütun alanlarına ihtiyaç duyuyorsa, modern Excel'in kullandığı iki boyutlu düzen için tasarlanmış olan [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) bölümündeki modern `PivotTableStyleType` ön ayarlarını kullanın.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Senaryo 1: Eski bir XLS ön ayar otomatik biçimi uygula
# Kullanılan API: PivotTable.AutoFormatType
# Hedef dosya biçimi: .xls (eski)
# Eksiksiz örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin
# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
# İlk çalışma sayfasını al
sheet = workbook.getWorksheets().get(0)
# Başlık satırı (Meyve, Yıl, Miktar) ve 2020 ile 2021 yıllarını kapsayan
# üzüm, yaban mersini, kivi, kiraz için 9 veri satırı ile kaynak verileri doldur
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# E3 hedef hücresinde, "Pivot1" adıyla, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)
# Alanları ata: Fruit -> Satırlar, Amount -> Veri
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Eski XLS ön ayar otomatik biçimi "Report5" uygula
# Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
# .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType değerini yok sayar
# ve PivotTableStyleType / PivotTableStyleName ile belirtilen biçimi kullanır.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Çalışma kitabını eski .xls biçiminde kaydet
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Modern Adlandırılmış Ön Ayar Pivot Tablosu Stili Uygulama**

`pivotTable.setPivotTableStyleType(int)`, Excel 2007'in pivottablolara tanıttığı önceden oluşturulmuş adlandırılmış stillerden birini seçer. `PivotTableStyleType` numaralandırması üç tema ailesini ortaya çıkarır: `PIVOT_TABLE_STYLE_LIGHT1` ile `PIVOT_TABLE_STYLE_LIGHT28` arasında bulunan açık tema ailesi, `PIVOT_TABLE_STYLE_MEDIUM1` ile `PIVOT_TABLE_STYLE_MEDIUM28` arasında bulunan orta tema ailesi ve `PIVOT_TABLE_STYLE_DARK1` ile `PIVOT_TABLE_STYLE_DARK_28` arasında bulunan koyu tema ailesi. Ayrıca `None` ve `Custom` değerlerini de tanımlar. Her ailenin daha yüksek numaralı üyelerine Excel 2017'de eklenen stiller aittir.
Bu ön ayarlar salt okunurdur. Bir ön ayarın sunduğu sınırların ötesine geçip renkleri, kenarlıkları veya yazı tiplerini değiştirmeniz gerektiği an, [Senaryo 3](#define-and-apply-a-custom-pivot-table-style)'te gösterildiği gibi bunun yerine özel bir pivot stili tanımlamanız gerekir.

{{% alert color="primary" %}}
**Neden modern ön ayarlar ve rapor serisi otomatik biçimlendirme değil?** `PivotTableAutoFormatType`'ın `Report1` ile `Report10` ve `Table1` ile `Table10` değerleri, pivot sütun alanlarını içermediğinden, sütun alanı başlıkları için hiçbir stillendirme sağlamazlar ve Excel bu başlıkları stilleriz şekilde işler. `PivotTableStyleType` ön ayarları ise modern Excel’in kullandığı iki boyutlu düzen için tasarlanmıştır ve hem satır alanı hem de sütun alanı başlıklarını stillendirir.
{{% /alert %}}

Bu senaryo, Senaryo 1’in meyve/yıl/miktar veri kümesini kullanır, `Fruit` satır alanı yanında `PivotFieldType.COLUMN` aracılığıyla `Year` değerini sütun alanına ekler, `PIVOT_TABLE_STYLE_DARK1` koyu tema ön ayarını `pivotTable.setPivotTableStyleType` ile uygular ve sonucu `.xlsx` olarak kaydeder — `PivotTableStyleType`’ın anlamlı olduğu formattır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)
# Add a pivot table at E3 named "Pivot1", sourced from A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```
## **Özel Bir Pivot Tablosu Stili Tanımlama ve Uygulama**
Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamanız gerekir. İş akışı üç adımdan oluşur:
1. `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `tableStyle.getTableStyleElements().add(TableStyleElementType)` ile öğeler (`WHOLE_TABLE` veya `GRAND_TOTAL_ROW` gibi) ekleyerek, ardından her öğeye `tableStyleElement.setElementStyle(Style)` ile bir `Style` atayarak stili yapılandırın.
3. Stilin adıyla `pivotTable.setPivotTableStyleName(String)` çağırarak özel stili pivota uygulayın. Burada `setPivotTableStyleType` kullanmayın, çünkü bu yöntem yerleşik ön ayarları seçer.

{{% alert color="primary" %}}
`setPivotTableStyleName` ve `setPivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `setPivotTableStyleType`, `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `setPivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynakla eşleşen görüntülenir.
Kullanılabilir `TableStyleElementType` değerleri şunlardır: `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES`.
Aşağıdaki örnek, `WHOLE_TABLE` üzerinde ince siyah kenarlık ve `GRAND_TOTAL_ROW` üzerinde kalın kırmızı yazı tipi içeren özel bir pivot stili tanımlar, ardından `setPivotTableStyleName` ile uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# A1:C10'dan kaynaklanan, E3'e sabitlenmiş ve "Pivot1" adlı pivot tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Adım 1: yeni özel bir pivot tablo stili kaydet ve dizinini yakala
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# Adım 2: bir WholeTable öğesi ekle ve dört kenara da ince siyah kenarlık uygula
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Adım 4: özel stili ada göre uygula (PivotTableStyleType ile DEĞİL, çünkü bu yerleşik ön ayarlar içindir)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **formatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**
`pivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivot tablosunun veri alanı, satır ve sütun başlıkları ve toplamlar dahil her hücresine uygulayan bir kısayoldur. `setPivotTableStyleType` veya `setPivotTableStyleName` ile daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}
`formatAll`, hem `setPivotTableStyleType` hem de `setPivotTableStyleName` öğelerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.
Aşağıdaki örnek, sarı düz dolgulu, koyu mavi kalın yazı tipine sahip ve tüm kenarlarında ince siyah kenarlık bulunan bir `Style` oluşturur, ardından `formatAll` ile uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Senaryo 4: formatAll kullanarak her pivot tablo hücresine tek bir Stil uygulama
# Kullanılan API: PivotTable.formatAll(Style)
# Hedef biçim: .xlsx
# GitHub referansı: Aspose.Cells-for-.NET deposuna bakın — pivot tablo stil örnekleri
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# Pivot tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, adı "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Pivot tablonun her hücresine zorla uygulanacak bir Stil oluştur
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# formatAll uygula: bu tek stili pivot tablonun her hücresine zorla uygular,
# daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerinin üzerine yazar
pivotTable.formatAll(style)
# Çalışma kitabını modern .xlsx biçiminde kaydet
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.
| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `pivotTable.setAutoFormatType(int)` | `com.aspose.cells.pivot.PivotTableAutoFormatType` değerleri (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern formatlarda kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `pivotTable.setPivotTableStyleType(int)` | `com.aspose.cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `tableStyleElement.setElementStyle(Style)` ile yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `pivotTable.formatAll(Style)` | Pivotun tamamında diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `setPivotTableStyleType`, özel temalar için `setPivotTableStyleName` kullanın.


{{< app/cells/assistant language="python" >}}