---
title: Aspose.Cells for .NET'te PivotTable'lara stil uygulama
linktitle: PivotTable Stillerini Uygulama
description: Aspose.Cells for Python via Java'da pivot tablolara yerleşik ve özel stillerin nasıl uygulanacağını öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve FormatAll kısayolu ele alınmaktadır.
keywords: Aspose.Cells Python via Java pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya formatına bağlıdır.

{{% /alert %}}

## **Giriş**

Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, okuduğunuz formata değil, çalışma kitabını kaydettiğiniz dosya formatına göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski stil API'si yerine modern stil API'si geçerli olur.

Eski `.xls` çıktısı için, `com.aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte `pivotTable.setAutoFormatType(int)` metodunu kullanın. Bu API, klasik Excel'in pivot tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktıları için iki çeşit stil API'si mevcuttur:

- `pivotTable.setPivotTableStyleType(int)` yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `pivotTable.setPivotTableStyleName(String)` `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` aracılığıyla kendi tanımladığınız özel bir stili seçer. Ön ayarların sunduğunun ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Ayrıca, `pivotTable.formatAll(Style)` kısayolu, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayarak yukarıdaki stil adı API'lerinden hangisi kullanılırsa kullanılsın geçersiz kılar. Bu, altta yatan temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Önceden Tanımlı Otomatik Biçimini Uygulama**

Pivot tablodaki `setAutoFormatType` metodu, `com.aspose.cells.pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `REPORT_1`'den `REPORT_10`'a, `CLASSIC` ve `TABLE_1`'den `TABLE_10`'a kadardır.

{{% alert color="primary" %}}

`setAutoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde, Excel bu ayarı yoksayar ve `setPivotTableStyleType` ile `setPivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablo ekler, `PivotTableAutoFormatType.REPORT_5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Senaryo 1: Eski bir XLS ön ayar otomatik biçimi uygula
# Kullanılan API: PivotTable.AutoFormatType
# Hedef dosya biçimi: .xls (eski)
# Eksiksiz örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin

# Yeni bir çalışma kitabı oluştur
workbook = Workbook()

# İlk çalışma sayfasını al
sheet = workbook.getWorksheets().get(0)

# Başlık satırı (Meyve, Yıl, Tutar) ve 2020 ile 2021 yıllarını kapsayan
# üzüm, yaban mersini, kivi, kiraz ile 9 veri satırı içeren kaynak verileri doldur
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

# Hedef hücre E3'te "Pivot1" adıyla ve A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Alanları ata: Fruit -> Satırlar, Year -> Sütunlar, Amount -> Veri
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Eski XLS ön ayar otomatik biçimi "Report5" uygula
# Not: Bu özellik yalnızca .xls olarak kaydedildiğinde anlamlıdır.
# .xlsx/.xlsm/.xlsb olarak kaydedildiğinde Excel AutoFormatType'ı yok sayar
# ve PivotTableStyleType / PivotTableStyleName'in belirttiği biçimi kullanır.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Çalışma kitabını eski .xls biçiminde kaydet
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Modern Adlandırılmış Önceden Tanımlı Pivot Tablo Stilini Uygulama**

Pivot tablodaki `setPivotTableStyleType` metodu, `com.aspose.cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, `PIVOT_TABLE_STYLE_LIGHT_1`'den `PIVOT_TABLE_STYLE_LIGHT_28`'e kadar açık temaları ve `PIVOT_TABLE_STYLE_DARK_1`'den `PIVOT_TABLE_STYLE_DARK_28`'e kadar koyu temaları kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma aracılığıyla erişilebilir.

Bu, herhangi bir modern dosya formatı için önerilen API'dir. Eski otomatik biçimin aksine, burada seçilen stil Excel tarafından sadık biçimde işlenir ve diğer Office araçlarıyla gidiş-dönüş işlemlerinde korunur.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir pivot tablo oluşturur, `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Senaryo 2: PivotTableStyleType kullanarak modern bir Excel 2007+ adlandırılmış ön ayar stilini uygulayın.
# Hedef dosya biçimi: .xlsx. PivotTableStyleType numaralandırması Aspose.Cells ad alanında bulunur
# (Aspose.Cells.Pivot içinde değil) — bu yüzden ek bir using ifadesine gerek yoktur.
# GitHub referansı: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Başlık satırı: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# Fruit / Year / Amount verilerinden oluşan 9 veri satırı
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

# E3 konumuna "Pivot1" adında, A1:C10 aralığından beslenen bir pivot tablo ekleyin
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Pivot alanlarını atayın: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Modern bir Excel 2007+ adlandırılmış ön ayar pivot stili uygulayın.
# PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
# bu biçimler için Excel tarafından yok sayılır. PivotTableStyleDark1, koyu tema
# ailesine aittir (PivotTableStyleDark1..PivotTableStyleDark28); aynı numaralandırma ayrıca
# daha yeni Excel 2017 açık/koyu temalarını da sunar (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Modern .xlsx olarak kaydedin — bu, PivotTableStyleType'ın anlamlı olduğu biçimdir.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Özel Pivot Tablo Stili Tanımlama ve Uygulama**

Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde, özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `tableStyle.getTableStyleElements().add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WHOLE_TABLE` veya `GRAND_TOTAL_ROW`) ekleyerek, ardından her öğeye `tableStyleElement.setElementStyle(Style)` ile bir `Style` atayarak stili yapılandırın.
3. Stilin adıyla `pivotTable.setPivotTableStyleName(String)` çağırarak özel stili pivota uygulayın. Burada `setPivotTableStyleType` kullanmayın; çünkü bu metot yerleşik ön ayarları seçer.

{{% alert color="primary" %}}

`setPivotTableStyleName` ve `setPivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `setPivotTableStyleType`, `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için ise `setPivotTableStyleName` kullanın. Her ikisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uyan işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri şunları içerir: `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` ve `PAGE_FIELD_VALUES`.

Aşağıdaki örnek, `WHOLE_TABLE` üzerinde ince siyah kenarlığa ve `GRAND_TOTAL_ROW` üzerinde kalın kırmızı yazı tipine sahip özel bir pivot stili tanımlar, ardından bunu `setPivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

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

# A1:C10'dan kaynaklanan ve E3'e yerleştirilen "Pivot1" adlı pivot tablo ekle
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Adım 3: bir GrandTotalRow öğesi ekle ve kırmızı kalın yazı tipi uygula
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Adım 4: özel stili ada göre uygula (yerleşik önayarlar için olan PivotTableStyleType ile DEĞİL)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **FormatAll ile Her Pivot Hücresine Tek Stil Uygulama**

`pivotTable.formatAll(Style)`, veri alanı, satır ve sütun başlıkları ve toplamlar dahil olmak üzere pivot tablonun her hücresine tek bir `Style` nesnesi uygulayan bir kısayoldur. `setPivotTableStyleType` veya `setPivotTableStyleName` ile daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`formatAll`, hem `setPivotTableStyleType` hem de `setPivotTableStyleName` öğelerini geçersiz kılar. Yalnızca tüm pivotta temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolguya, kalın koyu mavi yazı tipine ve tüm kenarlarda ince siyah kenarlıklara sahip bir `Style` oluşturur, ardından bunu `formatAll` ile uygular ve `.xlsx` olarak kaydeder.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Senaryo 4: FormatAll API kullanarak her pivot tablo hücresine tek bir Stil uygulama
# Kullanılan API: PivotTable.FormatAll(Style)
# Hedef format: .xlsx
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

# Pivot tablosu ekle: kaynak aralık A1:C10, hedef hücre E3, ad "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Pivot tablosunun her hücresine zorla uygulanacak bir Stil oluştur
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# FormatAll uygula: bu tek stili pivot tablosunun her hücresine zorlar,
# daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivotTable.formatAll(style)

# Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir başvuru için aşağıdaki tabloyu kullanın.

| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `pivotTable.setAutoFormatType(int)` | `com.aspose.cells.pivot.PivotTableAutoFormatType` değerleri (ör. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Modern formatlarda kaydederken yoksayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `pivotTable.setPivotTableStyleType(int)` | `com.aspose.cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `tableStyleElement.setElementStyle(Style)` aracılığıyla yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `pivotTable.formatAll(Style)` | Tüm pivot boyunca diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `setPivotTableStyleType`, özel temalar için ise `setPivotTableStyleName` kullanın.

{{< app/cells/assistant language="python" >}}