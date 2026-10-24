---
title: Aspose.Cells for Node.js via Java'da Pivot Tablolarına Stil Uygulama
linktitle: Aspose.Cells for Node.js via Java'da Pivot Tablolarına Stil Uygulama
description: Aspose.Cells for Node.js via Java'da pivot tablolarına yerleşik ve özel stillerin nasıl uygulanacağını öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stiller, özel pivot tablosu stilleri ve FormatAll kısayolu.
keywords: Aspose.Cells Node.js via Java pivot tablosu stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablosu stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği formata bağlıdır.
{{% /alert %}}

## **Giriş**
Aspose.Cells, pivot tabloları için iki paralel stil API'si sunar. Aralarındaki karar, çalışma kitabını okuduğunuz formata değil, kaydettiğiniz formata bağlıdır. `.xls` dosyasından yüklenen bir çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda modern stil API'si eski API yerine geçerli olur.
- `PivotTable.pivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar; Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.pivotTableStyleName`, `Worksheets.getTableStyles().addPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renk, kenarlık veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.
Ayrıca, `PivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivot tablosunun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden hangisi ayarlanmış olursa olsun geçersiz kılan bir kısayoldur. Bu, temel temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Ön Ayar Otomatik Biçimini Uygulama**
`PivotTable.autoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1`–`Report10`, `Classic` ve `Table1`–`Table10` arasındadır.
Aşağıdaki örnek, yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablosu ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu pivot tablolar** için tasarlanmıştır — sütun alanı başlıkları için yerleşik bir stillendirme içermez. Pivot'unuz sütun alanları gerektiriyorsa, bunun yerine modern Excel'in kullandığı iki boyutlu düzen için tasarlanmış [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style)'deki modern `PivotTableStyleType` ön ayarlarını kullanın.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// İlk çalışma sayfasını al
let sheet = workbook.getWorksheets().get(0);
// Başlık satırı (Fruit, Year, Amount) ile kaynak verileri doldur
// ve 2020 ile 2021 yılları arasında grape, blueberry, kiwi, cherry verilerini kapsayan 9 veri satırı
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Hedef hücre E3'e, "Pivot1" adıyla, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);
// Alanları atayın: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Eski XLS ön ayarı olan "Report5" otomatik biçimini uygulayın
// Not: Bu özellik yalnızca .xls olarak kaydederken geçerlidir.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde Excel AutoFormatType'ı yok sayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği biçimi kullanır.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// Çalışma kitabını eski .xls formatında kaydedin
workbook.save("output.xls");
```

## **Modern Adlandırılmış Ön Ayar Pivot Tablosu Stilini Uygulama**

`PivotTable.setPivotTableStyleType(int)` yöntemi, Excel 2007’nin pivot tabloları için tanıttığı önceden tanımlı adlandırılmış stillerden birini seçer. `PivotTableStyleType` numaralandırması, `PIVOT_TABLE_STYLE_LIGHT1`’den `PIVOT_TABLE_STYLE_LIGHT28`’e kadar olan açık aileyi, `PIVOT_TABLE_STYLE_MEDIUM1`’den `PIVOT_TABLE_STYLE_MEDIUM28`’e kadar olan orta aileyi ve `PIVOT_TABLE_STYLE_DARK1`’den `PIVOT_TABLE_STYLE_DARK_28`’e kadar olan koyu aileyi içerir. Ayrıca `None` ve `Custom` değerlerini de tanımlar. Her ailenin daha yüksek sayıya sahip üyeleri, Excel 2017’ye eklenen stillerdir.
Bu ön ayarlar salt okunurdur. Bir ön ayarın sunduğu sınırlar dışına çıkarak renkleri, kenarlıkları veya yazı tiplerini değiştirmeniz gerektiğinde, Bunun yerine [Senaryo 3](#define-and-apply-a-custom-pivot-table-style)’te gösterildiği gibi özel bir pivot stili tanımlamanız gerekir.

{{% alert color="primary" %}}
**Neden modern ön ayarlar, rapor serisi otomatik formatlardan daha mı uygun?** `PivotTableAutoFormatType`’ın `Report1`’den `Report10`’a ve `Table1`’den `Table10`’a kadar olan değerleri, pivot sütun alanlarından önce tanımlanmıştır, bu nedenle sütun alanı başlıkları için hiçbir stillendirme içermezler ve Excel bu başlıkları stillendirilmemiş olarak işler. `PivotTableStyleType` ön ayarları ise modern Excel’in kullandığı iki boyutlu düzen için tasarlanmıştır ve hem satır alanı hem de sütun alanı başlıklarını stillendirir.
{{% /alert %}}

Bu senaryo, Senaryo 1’in Fruit/Year/Amount veri kümesini kullanır, `Fruit` satır alanının yanına `PivotFieldType.COLUMN` aracılığıyla `Year` alanını sütun alanına ekler, `pivotTable.setPivotTableStyleType` ile koyu tema ön ayarı `PIVOT_TABLE_STYLE_DARK1`’i uygular ve sonucu `.xlsx` olarak kaydeder — bu, `PivotTableStyleType`’ın anlamlı olduğu formattır.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3 named "Pivot1", sourced from A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```
## **Özel Bir Pivot Tablosu Stili Tanımlama ve Uygulama**
Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde, özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:
1. Çalışma kitabının `TableStyles` koleksiyonuna `Worksheets.getTableStyles().addPivotTableStyle(String name)` aracılığıyla özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. Stili, `TableStyle.tableStyleElements.add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WholeTable` veya `GrandTotalRow`) ekleyerek yapılandırın, ardından her öğeye `TableStyleElement.setElementStyle(Style)` ile bir `Style` atayın.
3. Özel stili pivot'a uygulamak için `PivotTable.pivotTableStyleName` özelliğini stilin adına ayarlayın. Burada `pivotTableStyleType` kullanmayın, çünkü bu özellik yerleşik ön ayarları seçer.

{{% alert color="primary" %}}
`pivotTableStyleName` ve `pivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `pivotTableStyleType`, `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `pivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.
Kullanılabilir `TableStyleElementType` değerleri şunlardır: `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues`.
Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi olan özel bir pivot stili tanımlar, ardından bunu `pivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// A1:C10'dan kaynak alan, E3 hücresine sabitlenmiş ve "Pivot1" adında bir özet tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Adım 1: yeni bir özel özet tablo stili kaydet ve dizinini al
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Adım 2: bir WholeTable (TümTablo) öğesi ekle ve dört kenara ince siyah kenarlık uygula
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Adım 3: bir GrandTotalRow (Genel Toplam Satırı) öğesi ekle ve kırmızı kalın yazı tipi uygula
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Adım 4: özel stili ada göre uygula (YERLEŞİK ön ayarlar için olan PivotTableStyleType DEĞİL)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **formatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**
`PivotTable.formatAll(Style)`, tek bir `Style` nesnesini pivot tablosunun — veri alanı, satır ve sütun başlıkları ve toplamlar dahil — her hücresine uygulayan bir kısayoldur. `pivotTableStyleType` veya `pivotTableStyleName` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}
`formatAll`, hem `pivotTableStyleType` hem de `pivotTableStyleName` öğelerini geçersiz kılar. Yalnızca pivot genelinde temadan bağımsız, tek tip bir görünüm gerektiğinde kullanın.
Aşağıdaki örnek, sarı dolgulu, kalın koyu mavi yazı tipine ve her tarafta ince siyah kenarlıklara sahip bir `Style` oluşturur, ardından bunu `formatAll` ile uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satırlar 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Özet tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, ad "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Özet tablo alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Özet tablosunun her hücresine uygulanacak bir Stil oluştur
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// formatAll uygula: özet tablonun her hücresine bu tek stili uygular,
// daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName ayarlarını geçersiz kılar
pivotTable.formatAll(style);
// Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.
| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern formatlarda kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar; Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `TableStyleElement.setElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.formatAll(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `pivotTableStyleType` veya özel temalar için `pivotTableStyleName` kullanın.


{{< app/cells/assistant language="nodejs-java" >}}