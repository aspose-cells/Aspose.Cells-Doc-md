---
title: Özet Tablolara Stil Uygulama
linktitle: Özet Tablolara Stil Uygulama
description: Aspose.Cells for .NET'te hem yerleşik hem de özel stilleri özet tablolara nasıl uygulayacağınızı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel özet tablo stilleri ve FormatAll kısayolu.
keywords: Aspose.Cells .NET özet tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, hem eski özet tablo otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel özet tablo stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının içinden yüklendiği biçime değil, kaydedildiği dosya biçimine bağlıdır.

{{% /alert %}}

## **Giriş**

Aspose.Cells, özet tablolar için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını hangi dosya biçiminde kaydettiğinize bağlıdır; okuduğunuz biçime değil. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir ve bu durumda eski API yerine modern stil API'si geçerli olur.

Eski `.xls` çıktısı için `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasıyla birlikte `PivotTable.AutoFormatType` özelliğini kullanın. Bu API, klasik Excel'in özet tablolar için sunduğu otomatik biçim seçicisine karşılık gelir.

Modern `.xlsx`, `.xlsm` ve `.xlsb` çıktısı için iki çeşit stil API'si mevcuttur:

- `PivotTable.PivotTableStyleType`, yerleşik adlandırılmış stillerden birini seçer (açık ve koyu temalar, Excel 2017'de eklenen stiller dahil). Bu ön ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Ön ayarların sunduğundan farklı renk, kenarlık veya yazı tipi değişiklikleri yapmak istediğinizde özel stiller gereklidir.

Bunlara ek olarak, `PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini pivotun her hücresine uygulayan, yukarıdaki stil adı API'leriyle ayarlanan her şeyi geçersiz kılan bir kısayoldur. Bu, alttaki tema dikkate alınmaksızın tek tip bir görünüm gerektiğinde yararlıdır.

## **Eski Bir XLS Ön Ayar Otomatik Biçimi Uygulama**

`PivotTable.AutoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1` ile `Report10` arası, `Classic` ve `Table1` ile `Table10` arası değerlerdir.

{{% alert color="primary" %}}

`AutoFormatType` yalnızca çalışma kitabı `.xls` olarak kaydedildiğinde dikkate alınır. Aynı çalışma kitabı `.xlsx`, `.xlsm` veya `.xlsb` olarak kaydedildiğinde, Excel bu özelliği yoksayar ve `PivotTableStyleType` ile `PivotTableStyleName` ayarlarına geri döner.

{{% /alert %}}

Aşağıdaki örnek, yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir özet tablo ekler, `PivotTableAutoFormatType.Report5`'i uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}

**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1`–`Report10`, `Table1`–`Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştı — sütun alanı başlıkları için yerleşik bir biçimlendirmeleri yoktur. Özet tablonuzun sütun alanlarına ihtiyacı varsa, bunun yerine aşağıdaki Senaryo 2'deki modern `PivotTableStyleType` ön ayarlarını kullanın; bunlar modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Senaryo 1: Eski bir XLS ön ayar otomatik biçimini uygula
// Kullanılan API: PivotTable.AutoFormatType
// Hedef dosya biçimi: .xls (eski)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();

// İlk çalışma sayfasını al
Worksheet sheet = workbook.Worksheets[0];

// Kaynak verileri başlık satırıyla doldur (Meyve, Yıl, Tutar)
// ve 2020 ve 2021 yılları arasında üzüm, yaban mersini, kivi, kiraz'ı kapsayan 9 veri satırı
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// Hedef hücre E3'te, "Pivot1" adında, A1:C10 kaynak aralığını kullanan bir pivot tablo ekle
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Alanları ata: Meyve -> Satırlar, Yıl -> Sütunlar, Tutar -> Veri
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Eski XLS ön ayar otomatik biçimi "Report5" uygula
// Not: Bu özellik yalnızca .xls olarak kaydederken anlamlıdır.
// .xlsx/.xlsm/.xlsb olarak kaydedildiğinde, Excel AutoFormatType'ı yok sayar
// ve PivotTableStyleType / PivotTableStyleName'in belirttiği her şeyi kullanır.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Çalışma kitabını eski .xls biçiminde kaydet
workbook.Save("output.xls");
```

## **Modern Adlandırılmış Ön Ayar Özet Tablo Stili Uygulama**

`PivotTable.PivotTableStyleType`, `Aspose.Cells.PivotTableStyleType` numaralandırmasından bir değer kabul eder. Numaralandırma, `PivotTableStyleLight1` ile `PivotTableStyleLight28` arası açık temaları ve `PivotTableStyleDark1` ile `PivotTableStyleDark28` arası koyu temaları kapsar. Excel 2017'de eklenen stiller (açık ve koyu temaların ikinci dalgası) aynı numaralandırma üzerinden erişilebilir.

Bu, herhangi bir modern dosya biçimi için önerilen API'dir. Eski otomatik biçimden farklı olarak, burada seçilen stil Excel tarafından aslına sadık şekilde işlenir ve diğer Office araçlarıyla yapılan gidiş-dönüşlerde de korunur.

Aşağıdaki örnek aynı Fruit/Year/Amount verilerini kullanır, özdeş bir özet tablo oluşturur, `PivotTableStyleDark1` uygular ve çalışma kitabını `.xlsx` olarak kaydeder.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Senaryo 2: PivotTableStyleType kullanarak modern bir Excel 2007+ adlandırılmış hazır stili uygulayın.
// Hedef dosya formatı: .xlsx. PivotTableStyleType numaralandırması Aspose.Cells ad alanında bulunur
// (Aspose.Cells.Pivot içinde değil) — bu yüzden ek bir using'e ihtiyacımız yok.
// GitHub referansı: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Başlık satırı: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 veri satırı: Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// E3 konumunda "Pivot1" adında bir pivot tablo ekleyin, kaynak A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot alanlarını atayın: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Modern bir Excel 2007+ adlandırılmış hazır pivot stili uygulayın.
// PivotTableStyleType, .xlsx / .xlsm / .xlsb dosyaları için doğru API'dir; AutoFormatType
// bu formatlar için Excel tarafından yok sayılır. PivotTableStyleDark1, koyu tema
// ailesine aittir (PivotTableStyleDark1..PivotTableStyleDark28) ve aynı numaralandırma ayrıca
// daha yeni Excel 2017 açık/koyu temalarını da sunar (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Modern .xlsx olarak kaydedin — PivotTableStyleType'ın anlamlı olduğu format budur.
workbook.Save("output.xlsx");
```

## **Özel Bir Özet Tablo Stili Tanımlama ve Uygulama**

Yerleşik ön ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir özet stili tanımlamalısınız. İş akışı üç adımdan oluşur:

1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WholeTable` veya `GrandTotalRow`) ekleyerek stili yapılandırın, ardından her öğeye `TableStyleElement.SetElementStyle(Style)` aracılığıyla bir `Style` atayın.
3. `PivotTable.PivotTableStyleName`'i stilin adına ayarlayarak özel stili özet tabloya uygulayın. Bu özellik yerleşik ön ayarları seçtiğinden burada `PivotTableStyleType`'ı kullanmayın.

{{% alert color="primary" %}}

`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `PivotTableStyleType`'ı ve `AddPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName`'i kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uygun olan işlenir.

{{% /alert %}}

Kullanılabilir `TableStyleElementType` değerleri arasında `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` bulunur.

Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlığa ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipine sahip özel bir özet stili tanımlar, ardından bunu `PivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Kaynak verileri doldur: başlık satırı + 9 veri satırı (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

// A1:C10'dan kaynaklanan, E3'e sabitlenmiş, "Pivot1" adlı pivot tablo ekle
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Adım 1: yeni bir özel pivot tablo stili kaydet ve dizinini yakala
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Adım 2: bir WholeTable öğesi ekle ve dört kenara ince siyah kenarlıklar uygula
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);

// Adım 3: bir GrandTotalRow öğesi ekle ve kırmızı kalın yazı tipi uygula
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Adım 4: özel stili ada göre uygula (PivotTableStyleType DEĞİL, bu yerleşik ön ayarlar içindir)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **FormatAll ile Her Pivot Hücresine Tek Bir Stil Uygulama**

`PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini veri alanı, satır ve sütun başlıkları ile toplamlar dahil olmak üzere özet tablonun her hücresine uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` aracılığıyla daha önce ayarlanmış olan her şey geçersiz kılınır.

{{% alert color="primary" %}}

`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` öğelerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.

{{% /alert %}}

Aşağıdaki örnek, sarı düz dolguya, kalın koyu mavi yazı tipine ve tüm kenarlarda ince siyah kenarlıklara sahip bir `Style` oluşturur, ardından bunu `FormatAll` ile uygular ve `.xlsx` olarak kaydeder.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Senaryo 4: FormatAll kullanarak her pivot tablo hücresine tek bir Stil uygulama
// Kullanılan API: PivotTable.FormatAll(Style)
// Hedef format: .xlsx
// GitHub referansı: Aspose.Cells-for-.NET deposuna bakın — pivot tablo stil örnekleri

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Kaynak verileri doldur: başlık satırı (satır 1) + 9 veri satırı (satır 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);

// Pivot tablo ekle: kaynak aralık A1:C10, hedef hücre E3, ad "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot alanlarını ata: Fruit -> Satır alanı, Year -> Sütun alanı, Amount -> Veri alanı
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Pivot tablonun her hücresine zorla uygulanacak bir Stil oluştur
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;

// FormatAll uygula: bu tek stili pivot tablonun her hücresine zorlar,
// önceden ayarlanmış tüm PivotTableStyleType / PivotTableStyleName ayarlarını geçersiz kılar
pivotTable.FormatAll(style);

// Çalışma kitabını modern .xlsx formatında kaydet
workbook.Save("output.xlsx");
```

## **Hangi Stil API'sini Kullanmalıyım?**

Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.

| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (örn. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimlerde kaydederken yoksayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (açık/koyu temalar, Excel 2017 eklemeleri dahil). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `TableStyleElement.SetElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.FormatAll(Style)` | Tüm pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |

Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`'ı veya özel temalar için `PivotTableStyleName`'i kullanın.

{{< app/cells/assistant language="csharp" >}}