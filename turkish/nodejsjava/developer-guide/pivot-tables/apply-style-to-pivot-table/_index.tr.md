---
title: Aspose.Cells for .NET'te PivotTable'lara stil uygulama
linktitle: PivotTable Stillerini Uygulama
description: Aspose.Cells for Node.js via Java'da pivot tablolarına yerleşik ve özel stilleri nasıl uygulayacağınızı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablo stilleri ve FormatAll kısayolu.
keywords: Aspose.Cells Node.js via Java pivot tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, hem eski pivot otomatik biçimlerini (.xls dosyaları için) hem de modern adlandırılmış veya özel pivot tablo stillerini (.xlsx, .xlsm ve .xlsb dosyaları için) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata değil, kaydedildiği dosya formatına bağlıdır.

{{% /alert %}}

## **Giriş**

Aspose.Cells, pivot tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, okuduğunuz formata değil, çalışma kitabını kaydettiğiniz dosya formatına göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si değil, modern stil API'si geçerli olur.

Eski `.xls` çıktısı için, `PivotTable.autoFormatType` özelliğini `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte kullanın. Bu API, klasik Excel'in pivot tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki tür stil API'si mevcuttur:

- `PivotTable.pivotTableStyleType` yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu hazır ayarlar salt okunurdur.
- `PivotTable.pivotTableStyleName` `Worksheets.getTableStyles().addPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Hazır ayarların sunduğundan farklı renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Ek olarak, `PivotTable.formatAll(Style)` pivot tablonun her hücresine tek bir `Style` nesnesi uygulayan ve yukarıdaki stil adı API'lerinden hangisi ayarlanmış olursa olsun geçersiz kılan bir kısayoldur. Bu, temel alınan temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski XLS Hazır Otomatik Biçimi Uygulama**

`PivotTable.autoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1` ile `Report10`, `Classic` ve `Table1` ile `Table10` arasındadır.

{{% alert color="primary" %}}

`autoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde, Excel bu özelliği yok sayar ve `pivotTableStyleType` ve `pivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek, yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablo ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// İlk çalışma sayfasını al
let sheet = workbook.getWorksheets().get(0);

// Kaynak verileri başlık satırıyla (Meyve, Yıl, Miktar) doldur
// ve 2020 ile 2021 yılları arasında üzüm, yaban mersini, kivi, kirazı kapsayan 9 veri satırı ekle
sheet.getCells().get(0, 0).putValue("Meyve");
sheet.getCells().get(0, 1).putValue("Yıl");
sheet.getCells().get(0, 2).putValue("Miktar");

sheet.getCells().get(1, 0).putValue("üzüm");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);

sheet.getCells().get(2, 0).putValue("yaban mersini");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);

sheet.getCells().get(3, 0).putValue("kivi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);

sheet.getCells().get(4, 0).putValue("kiraz");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);

sheet.getCells().get(5, 0).putValue("üzüm");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);

sheet.getCells().get(6, 0).putValue("yaban mersini");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);

sheet.getCells().get(7, 0).putValue("kivi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);

sheet.getCells().get(8, 0).putValue("kiraz");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);

sheet.getCells().get(9, 0).putValue("üzüm");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);

// Hedef hücre E3'e "Pivot1" adıyla, A1:C10 kaynak aralığını kullanarak bir pivot tablo ekle
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Alanları ata: Meyve -> Satırlar, Yıl -> Sütunlar, Miktar -> Veri
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Meyve");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Miktar");

// Eski XLS hazır otomatik biçimi "Report5" uygula
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde Excel AutoFormatType'ı yok sayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği stili kullanır.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Çalışma kitabını eski .xls biçiminde kaydet
workbook.save("output.xls");
```

## **Modern Adlandırılmış Hazır Pivot Tablo Stili Uygulama**

`PivotTable.pivotTableStyleType`, `Aspose.Cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, açık temalar `PivotTableStyleLight1` ile `PivotTableStyleLight28` ve koyu temalar `PivotTableStyleDark1` ile `PivotTableStyleDark28` arasındaki değerleri kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma aracılığıyla erişilebilir.

Bu, herhangi bir modern dosya formatı için önerilen API'dir. Eski otomatik biçimin aksine, burada seçilen stil Excel tarafından sadık bir şekilde işlenir ve diğer Office araçlarıyla gidiş-dönüş işlemlerinde korunur.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir pivot tablo oluşturur, `PivotTableStyleDark1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Başlık satırı: Meyve / Yıl / Miktar
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 veri satırı: Meyve / Yıl / Miktar
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

// E3 hücresine "Pivot1" adında bir özet tablo ekle, A1:C10 kaynağından
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Özet tablo alanlarını ata: Meyve -> Satır alanı, Yıl -> Sütun alanı, Miktar -> Veri alanı
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Modern bir Excel 2007+ adlandırılmış hazır özet tablo stili uygula.
// PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
// Excel tarafından bu formatlar için yoksayılır. PivotTableStyleDark1, koyu tema ailesine aittir
// (PivotTableStyleDark1..PivotTableStyleDark28) ve aynı enum ayrıca
// daha yeni Excel 2017 açık/koyu temalarını (PivotTableStyleLight1..Light28 / Dark1..Dark28) gösterir.
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Modern .xlsx olarak kaydet — PivotTableStyleType'ın anlamlı olduğu format budur.
workbook.save("output.xlsx");
```

## **Özel Bir Pivot Tablo Stili Tanımlama ve Uygulama**

Yerleşik hazır ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde, özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `Worksheets.getTableStyles().addPivotTableStyle(String name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.tableStyleElements.add(TableStyleElementType)` aracılığıyla öğeler (`WholeTable` veya `GrandTotalRow` gibi) ekleyerek, ardından `TableStyleElement.setElementStyle(Style)` aracılığıyla her öğeye bir `Style` atayarak stili yapılandırın.
3. `PivotTable.pivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `pivotTableStyleType` kullanmayın, çünkü bu özellik yerleşik hazır ayarları seçer.

{{% alert color="primary" %}}

`pivotTableStyleName` ve `pivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik hazır ayarlar için `pivotTableStyleType` kullanın ve `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `pivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uyan stil işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri arasında `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` bulunur.

Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlığa ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipine sahip özel bir pivot stili tanımlar, ardından bunu `pivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

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

// A1:C10'dan beslenen, E3'e sabitlenmiş ve "Pivot1" adında bir özet tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Adım 1: yeni bir özel özet tablo stili kaydet ve dizinini yakala
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Adım 2: bir WholeTable öğesi ekle ve dört kenara da ince siyah kenarlık uygula
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Adım 3: bir GrandTotalRow öğesi ekle ve kalın kırmızı yazı tipi uygula
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Adım 4: özel stili ada göre uygula (yerleşik ön ayarlar için olan PivotTableStyleType'a göre DEĞİL)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.formatAll(Style)`, pivot tablonun her hücresine (veri alanı, satır ve sütun başlıkları ve toplamlar dahil) tek bir `Style` nesnesi uygulayan bir kısayoldur. `pivotTableStyleType` veya `pivotTableStyleName` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`formatAll` hem `pivotTableStyleType` hem de `pivotTableStyleName` öğelerini geçersiz kılar. Bunu yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgulu, kalın koyu mavi yazı tipine sahip ve tüm kenarlarında ince siyah kenarlıklar bulunan bir `Style` oluşturur, ardından bunu `formatAll` ile uygular ve `.xlsx` olarak kaydeder.

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

// Pivot tablonun her hücresine uygulanacak bir Stil oluştur
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

// FormatAll uygula: bu tek stili pivot tablonun her hücresine zorla uygular,
// daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivotTable.formatAll(style);

// Çalışma kitabını modern .xlsx formatında kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya formatına bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya formatı | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern formatlar olarak kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Yerleşik hazır ayarlar yeterli olmadığında kullanın. `TableStyleElement.setElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir format (tek tip geçersiz kılma) | `PivotTable.formatAll(Style)` | Tüm pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `pivotTableStyleType` veya özel temalar için `pivotTableStyleName` kullanın.

{{< app/cells/assistant language="javascript" >}}