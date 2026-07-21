---
title: Özet Tablolara Stil Uygulama
linktitle: Özet Tablolara Stil Uygulama
description: Aspose.Cells for Node.js via C++'te hem yerleşik hem de özel stilleri özet tablolara nasıl uygulayacağınızı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel özet tablo stilleri ve FormatAll kısayolu.
keywords: Aspose.Cells Node.js via C++ özet tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells, hem eski özet tablo otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel özet tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının kaydedildiği dosya biçimine bağlıdır, yüklendiği biçime değil.

{{% /alert %}}

## **Giriş**

Aspose.Cells, özet tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, okuduğunuz biçime değil, çalışma kitabını kaydettiğiniz dosya biçimine göre belirlenir. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski stil API'si yerine modern stil API'si geçerlidir.

Eski `.xls` çıktısı için, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte `PivotTable.AutoFormatType` özelliğini kullanın. Bu API, klasik Excel'in özet tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki çeşit stil API'si mevcuttur:

- `PivotTable.PivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar; Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Önceden tanımlanmış stillerin sunduğundan farklı renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gereklidir.

Ayrıca, `PivotTable.FormatAll(Style)` kısayolu, tek bir `Style` nesnesini pivotun her hücresine uygulayarak yukarıdaki stil adı API'lerinden herhangi biriyle ayarlananı geçersiz kılar. Bu, altta yatan temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Eski Bir XLS Ön Ayar Otomatik Biçimi Uygulama**

`PivotTable.AutoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1` ile `Report10` arası, `Classic` ve `Table1` ile `Table10` arasıdır.

{{% alert color="primary" %}}

`AutoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde, Excel bu özelliği yok sayar ve `PivotTableStyleType` ile `PivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek, yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir özet tablo ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");

// Senaryo 1: Eski bir XLS hazır otomatik biçimi uygulayın
// Kullanılan API: PivotTable.AutoFormatType
// Hedef dosya biçimi: .xls (eski)
// Eksiksiz örnekler ve veri dosyaları için lütfen https://github.com/aspose-cells/Aspose.Cells-for-.NET adresine gidin

// Yeni bir çalışma kitabı oluşturun
const workbook = new AsposeCells.Workbook();

// İlk çalışma sayfasını alın
const sheet = workbook.getWorksheets().get(0);

// Başlık satırı (Fruit, Year, Amount) ile kaynak verileri doldurun
// ve 2020 ile 2021 yılları arasında grape, blueberry, kiwi, cherry değerlerini kapsayan 9 veri satırı
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

// E3 hedef hücresinde, "Pivot1" adıyla ve A1:C10 kaynak aralığı kullanılarak bir pivot tablo ekleyin
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// Alanları atayın: Fruit -> Satırlar, Year -> Sütunlar, Amount -> Veri
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Eski XLS hazır otomatik biçimi "Report5" uygulayın
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType değerini yok sayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği biçimi kullanır.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Çalışma kitabını eski .xls biçiminde kaydedin
workbook.save("output.xls");
```

## **Modern Adlandırılmış Ön Ayar Özet Tablo Stili Uygulama**

`PivotTable.PivotTableStyleType`, `Aspose.Cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, `PivotTableStyleLight1` ile `PivotTableStyleLight28` arası açık temaları ve `PivotTableStyleDark1` ile `PivotTableStyleDark28` arası koyu temaları kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma aracılığıyla erişilebilir.

Bu, herhangi bir modern dosya biçimi için önerilen API'dir. Eski otomatik biçimin aksine, burada seçilen stil Excel tarafından aslına uygun şekilde işlenir ve diğer Office araçlarıyla gidiş-dönüşlerde korunur.

Aşağıdaki örnek, aynı Fruit/Year/Amount verilerini kullanır, özdeş bir özet tablo oluşturur, `PivotTableStyleDark1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

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

// E3 hücresine "Pivot1" adında, A1:C10 kaynaklı bir özet tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Özet tablo alanlarını ata: Meyve -> Satır alanı, Yıl -> Sütun alanı, Miktar -> Veri alanı
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Modern bir Excel 2007+ adlandırılmış önceden ayarlanmış özet tablo stili uygula.
// PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
// Excel tarafından bu formatlar için yok sayılır. PivotTableStyleDark1, koyu tema ailesine
// aittir (PivotTableStyleDark1..PivotTableStyleDark28) ve aynı enum, daha yeni
// Excel 2017 açık/koyu temalarını da (PivotTableStyleLight1..Light28 / Dark1..Dark28) sunar.
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// Modern .xlsx olarak kaydet — PivotTableStyleType'ın anlamlı olduğu format budur.
workbook.save("output.xlsx");
```

## **Özel Bir Özet Tablo Stili Tanımlama ve Uygulama**

Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir özet stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` aracılığıyla öğeler (`WholeTable` veya `GrandTotalRow` gibi) ekleyerek, ardından `TableStyleElement.SetElementStyle(Style)` aracılığıyla her öğeye bir `Style` atayarak stili yapılandırın.
3. `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili pivota uygulayın. Burada `PivotTableStyleType` kullanmayın, çünkü bu özellik yerleşik ön ayarları seçer.

{{% alert color="primary" %}}

`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `PivotTableStyleType`, `AddPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName` kullanın. Her ikisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynakla eşleşen işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` değerlerini içerir.

Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi ile özel bir özet stili tanımlar, ardından `PivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

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

// A1:C10'dan kaynaklanan, E3'e sabitlenmiş, "Pivot1" adlı pivot tablo ekle
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Adım 1: yeni özel pivot tablo stilini kaydet ve dizinini yakala
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Adım 2: bir WholeTable öğesi ekle ve dört kenara da ince siyah kenarlık uygula
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

// Adım 4: özel stili ada göre uygula (PivotTableStyleType DEĞİL, bu yerleşik ön ayarlar içindir)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini özet tablonun veri alanı, satır ve sütun başlıkları ile toplamlar dahil her hücresine uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` öğelerini geçersiz kılar. Yalnızca tüm pivot genelinde tek tip ve temadan bağımsız bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolgulu, kalın koyu mavi yazı tipine ve her tarafta ince siyah kenarlıklara sahip bir `Style` oluşturur, ardından `FormatAll` ile uygular ve `.xlsx` olarak kaydeder.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020); // Üzüm 2020 yılı satış tutarı: 5000 worksheets.getCells().get("C2").putValue(5000);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020); worksheets.getCells().get("C3").putValue(3000);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020); worksheets.getCells().get("C4").putValue(4000);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020); worksheets.getCells().get("C5").putValue(2000);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021); worksheets.getCells().get("C6").putValue(6000);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021); worksheets.getCells().get("C7").putValue(3500);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021); worksheets.getCells().get("C8").putValue(4500);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021); worksheets.getCells().get("C9").putValue(2500);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021); worksheets.getCells().get("C10").putValue(5500);

// Pivot tablosu ekle: kaynak aralığı A1:C10, hedef hücre E3, adı "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Pivot tablosunun her hücresine zorla uygulanacak bir Stil oluştur
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

// FormatAll uygula: bu tek stili pivot tablosunun her hücresine zorlar,
// daha önce ayarlanmış olan PivotTableStyleType / PivotTableStyleName değerlerini geçersiz kılar
pivotTable.formatAll(style);

// Çalışma kitabını modern .xlsx biçiminde kaydet
workbook.save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimler olarak kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar; Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `TableStyleElement.SetElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.FormatAll(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Şüpheye düştüğünüzde, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

{{< app/cells/assistant language="javascript" >}}
