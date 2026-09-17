---
title: Aspose.Cells for Node.js via C++ ile Pivot Tablolarına Stil Uygulama
linktitle: Aspose.Cells for Node.js via C++ ile Pivot Tablolarına Stil Uygulama
description: Aspose.Cells for Node.js via C++ kullanarak pivot tablolarına yerleşik ve özel stiller uygulamayı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stiller, özel pivot tablo stilleri ve FormatAll kısayolu ele alınmaktadır.
keywords: Aspose.Cells Node.js via C++ pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağıracağınız API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya biçimine göre belirlenir.
{{% /alert %}}

## **Giriş**
Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını okuduğunuz formata değil, kaydettiğiniz dosya biçimine göre yapılır. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si değil modern stil API'si geçerli olur.
- `PivotTable.PivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar; Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renkler, kenarlıklar veya yazı tipleri uygulamak istediğinizde özel stiller gerekir.
Ayrıca `PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini pivot tablonun her hücresine uygulayan ve yukarıdaki stil adı API'lerinden hangisiyle ayarlanmış olursa olsun geçersiz kılan bir kısayoldur. Bu, temel alınan tema ne olursa olsun tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Ön Ayar Otomatik Biçimi Uygulama**
`PivotTable.AutoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1`–`Report10`, `Classic` ve `Table1`–`Table10` arasındadır.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini ekler, bir pivot tablosu oluşturur, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Rapor serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu pivot tablolar** için tasarlanmıştır; sütun alanı başlıkları için yerleşik bir stil sunmazlar. Pivotunuz sütun alanları gerektiriyorsa, modern Excel'in kullandığı iki boyutlu düzen için tasarlanmış olan [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) bölümündeki modern `PivotTableStyleType` ön ayarlarını kullanın.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Senaryo 1: Eski bir XLS ön ayar otomatik biçimi uygula
// Kullanılan API: PivotTable.AutoFormatType
// Hedef dosya formatı: .xls (eski)
// Tüm örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin
// Yeni bir çalışma kitabı oluştur
const workbook = new AsposeCells.Workbook();
// İlk çalışma sayfasını al
const sheet = workbook.getWorksheets().get(0);
// Başlık satırı (Fruit, Year, Amount) ve 2020 ile 2021 yılları için grape, blueberry, kiwi, cherry meyvelerini kapsayan 9 veri satırı ile kaynak veriyi doldur
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
// E3 hedef hücresinde, "Pivot1" adıyla, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);
// Alanları ata: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Eski XLS ön ayar otomatik biçimi "Report5" uygula
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde Excel AutoFormatType'ı yok sayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği biçimi kullanır.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Çalışma kitabını eski .xls formatında kaydet
workbook.save("output.xls");
```

## **Modern Adlandırılmış Ön Ayar Pivot Tablo Stili Uygulama**

## **Özel Bir Pivot Tablo Stili Tanımlama ve Uygulama**
Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:
1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` ile `WholeTable` veya `GrandTotalRow` gibi öğeler ekleyerek stili yapılandırın, ardından `TableStyleElement.SetElementStyle(Style)` ile her öğeye bir `Style` atayın.
3. `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `PivotTableStyleType` kullanmayın; çünkü bu özellik yerleşik ön ayarları seçer.

{{% alert color="primary" %}}
`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `PivotTableStyleType`, `AddPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.
{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri arasında `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` bulunur.
Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi içeren özel bir pivot stili tanımlar, ardından bunu `PivotTableStyleName` ile uygular ve `.xlsx` olarak kaydeder.

```javascript
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
// A1:C10'dan kaynak alan, E3'e sabitlenmiş ve "Pivot1" adlı pivot tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);
// Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Adım 4: özel stili ada göre uygula (PivotTableStyleType'a GÖRE DEĞİL, bu yerleşik ön ayarlar içindir)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**
`PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini pivot tablonun veri alanı, satır ve sütun başlıkları ile toplamlar dahil her hücresine uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` ile daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}
`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` değerlerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.
{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgu, kalın koyu mavi yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `FormatAll` ile uygular ve `.xlsx` olarak kaydeder.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
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
// Pivot tablo ekle: kaynak aralığı A1:C10, hedef hücre E3, ad "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Pivot tablosunun her hücresine uygulanacak bir Stil oluştur
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
// FormatAll uygula: bu tek stili pivot tablosunun her hücresine zorla uygular,
// daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivotTable.formatAll(style);
// Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, çalışma kitabını kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.
| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimlerde kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar; Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `TableStyleElement.SetElementStyle(...)` ile yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.FormatAll(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

{{< app/cells/assistant language="nodejs-cpp" >}}