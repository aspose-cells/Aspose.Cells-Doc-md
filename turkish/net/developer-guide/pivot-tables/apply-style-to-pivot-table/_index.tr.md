---
title: Aspose.Cells for .NET'te Pivot Tablolarına Stil Uygulama
linktitle: Pivot Tablo Stillerini Uygula
description: Aspose.Cells for .NET'te yerleşik ve özel stilleri pivot tablolarına nasıl uygulayacağınızı öğrenin; eski XLS otomatik biçimleri, modern Excel 2007+ adlandırılmış stilleri, özel pivot tablosu stilleri ve FormatAll kısayolu dahil.
keywords: Aspose.Cells .NET pivot tablosu stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells hem eski pivot otomatik biçimlerini (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel pivot tablosu stillerini (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulamayı destekler. Çağırmanız gereken API, çalışma kitabının yüklendiği formata göre değil, kaydedildiği formata göre belirlenir.
{{% /alert %}}

## **Introduction**
Aspose.Cells, pivot tabloları için iki paralel stil API'si sunar. Aralarındaki seçim, çalışma kitabını okuduğunuz formata göre değil, kaydettiğiniz formata göre yapılır. Bir `.xls` dosyasından yüklenen çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si yerine modern stil API'si geçerlidir.
- `PivotTable.PivotTableStyleType` yerleşik adlandırılmış stillerden birini seçer (Excel 2017'de eklenen stiller dahil açık ve koyu temalar). Bu hazır ayarlar salt okunurdur.
- `PivotTable.PivotTableStyleName`, `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` aracılığıyla kendinizin tanımladığı özel bir stili seçer. Hazır ayarların sunduğundan farklı renkler, kenarlıklar veya yazı tipleri istediğinizde özel stiller gereklidir.
Ayrıca `PivotTable.FormatAll(Style)`, yukarıdaki stil adı API'lerinden herhangi biriyle ayarlananı geçersiz kılarak tek bir `Style` nesnesini pivot tablosunun her hücresine uygulayan bir kısayoldur. Bu, temel temadan bağımsız olarak tek tip bir görünüm gerektiğinde kullanışlıdır.

## **Apply a Legacy XLS Preset Autoformat**
`PivotTable.AutoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler `Report1` ile `Report10` arası, `Classic` ve `Table1` ile `Table10` arası değerlerdir.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini doldurur, bir pivot tablosu ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanı yok?** Report serisi otomatik biçimleri (`Report1` ile `Report10`, `Table1` ile `Table10` arası) klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu pivot tablolar** için tasarlanmıştır; sütun alanı başlıkları için yerleşik bir stil sunmazlar. Pivotunuz sütun alanları gerektiriyorsa, bunun yerine modern Excel'in kullandığı iki boyutlu düzen için tasarlanmış [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) bölümündeki modern `PivotTableStyleType` hazır ayarlarını kullanın.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
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
// Add a pivot table at destination cell E3, using source range A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Save the workbook in legacy .xls format
workbook.Save("output.xls");
```

## **Apply a Modern Named Preset Pivot Table Style**
`PivotTable.PivotTableStyleType`, Excel 2007’de pivot tablolar için tanıtılan önceden hazırlanmış adlandırılmış stillerden birini seçer. `PivotTableStyleType` numaralandırması, üç temel aileyi sunar: `PivotTableStyleLight1`’den `PivotTableStyleLight28`’e kadar olan açık ailesi, `PivotTableStyleMedium1`’den `PivotTableStyleMedium28`’e kadar olan orta ailesi ve `PivotTableStyleDark1`’den `PivotTableStyleDark28`’e kadar olan koyu ailesi. Ayrıca, `None` ve `Custom` değerlerini de tanımlar. Her ailenin daha yüksek numaralı üyeleri, Excel 2017’de eklenen stillerdir.
Bu ön ayarlar salt okunurdur. Bir ön ayarın sunduğu şekilde renkleri, kenarlıkları veya yazı tiplerini değiştirmeniz gerektiğinde, bunun yerine [Senaryo 3](#define-and-apply-a-custom-pivot-table-style)’te gösterildiği gibi özel bir pivot stili tanımlamanız gerekir.

{{% alert color="primary" %}}
**Neden modern ön ayarlar ve rapor serisi otomatik Biçimlendirmeleri değil?** `PivotTableAutoFormatType` numaralandırmasındaki `Report1` ile `Report10` ve `Table1` ile `Table10` değerleri, pivot sütun alanları öncesi olarak oluşturulmuştur ve dolayısıyla sütun alanı başlıklarını stilendirmek için herhangi bir tanımlama içermemektedir; Excel bu başlıkları stilsiz olarak işler. Öte yandan `PivotTableStyleType` ön ayarları, modern Excel’in kullandığı iki boyutlu düzen için tasarlanmış olup, hem satır alanı hem de sütun alanı başlıklarını stilendirebilir.
{{% /alert %}}

Bu senaryo, Senaryo 1’deki Meyve/Yıl/Miktar veri kümesini kullanmakta, `Fruit` satır alanının yanına `Year` öğesini `PivotFieldType.Column` aracılığıyla sütun alanına eklemekte, `PivotTable.PivotTableStyleType` ile koyu tema ön ayarı `PivotTableStyleDark1`’i uygulamakta ve sonucu `.xlsx` olarak kaydetmektedir — `PivotTableStyleType`'ın anlamlı olduğu format.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
// Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
// (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
// GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Header row: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 9 data rows of Fruit / Year / Amount
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
// Add a pivot table at E3, sourced from A1:C10
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.Save("output.xlsx");
```

## **Define and Apply a Custom Pivot Table Style**
Yerleşik hazır ayarlar değiştirilemez. Renkleri, kenarlıkları veya yazı tiplerini geçersiz kılmanız gerektiğinde özel bir pivot stili tanımlamalısınız. İş akışı üç adımdan oluşur:
1. `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` aracılığıyla çalışma kitabının `TableStyles` koleksiyonuna özel bir stil ekleyin. Bu, yeni oluşturulan stilin dizinini döndürür.
2. `TableStyle.TableStyleElements.Add(TableStyleElementType)` aracılığıyla öğeler (örneğin `WholeTable` veya `GrandTotalRow`) ekleyerek stili yapılandırın, ardından `TableStyleElement.SetElementStyle(Style)` ile her öğeye bir `Style` atayın.
3. Özel stili pivota `PivotTable.PivotTableStyleName` özelliğini stilin adına ayarlayarak uygulayın. Burada `PivotTableStyleType` kullanmayın; çünkü o özellik yerleşik hazır ayarları seçer.

{{% alert color="primary" %}}
`PivotTableStyleName` ve `PivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik hazır ayarlar için `PivotTableStyleType`, `AddPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `PivotTableStyleName` kullanın. İkisini birden ayarlamak zararsızdır, ancak yalnızca amaçlanan kaynağa uyan render edilir.
Kullanılabilir `TableStyleElementType` değerleri `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues` değerlerini içerir.
Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi olan özel bir pivot stili tanımlar, ardından bunu `PivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
using Aspose.Cells.Tables;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row + 9 data rows (A1:C10)
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
// Add pivot table sourced from A1:C10, anchored at E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// Step 2: add a WholeTable element and apply thin black borders on all four sides
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
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **Apply One Style to Every Pivot Cell with FormatAll**
`PivotTable.FormatAll(Style)`, tek bir `Style` nesnesini pivot tablosunun veri alanı, satır ve sütun başlıkları ile toplamlar dahil her hücresine uygulayan bir kısayoldur. `PivotTableStyleType` veya `PivotTableStyleName` aracılığıyla daha önce ayarlanan her şey geçersiz kılınır.

{{% alert color="primary" %}}
`FormatAll`, hem `PivotTableStyleType` hem de `PivotTableStyleName` değerlerini geçersiz kılar. Yalnızca tüm pivot genelinde temadan bağımsız tek tip bir görünüm gerektiğinde kullanın.
Aşağıdaki örnek sarı düz dolgu, kalın koyu mavi yazı tipi ve tüm kenarlarda ince siyah kenarlıklar içeren bir `Style` oluşturur, ardından bunu `FormatAll` ile uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 4: Apply a single Style to every pivot table cell using FormatAll
// API in use: PivotTable.FormatAll(Style)
// Target format: .xlsx
// GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
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
// Add pivot table: source range A1:C10, destination cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
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
// Apply FormatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.FormatAll(style);
// Save the workbook in the modern .xlsx format
workbook.Save("output.xlsx");
```

## **Which Style API Should I Use?**
Stil API'si seçimi, çalışma kitabını kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru olarak aşağıdaki tabloyu kullanın.
| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `PivotTable.AutoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerlerinden (ör. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimlerde kaydederken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `PivotTable.PivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerlerinden (Excel 2017 eklemeleri dahil açık/koyu temalar). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Yerleşik hazır ayarlar yeterli olmadığında kullanın. `TableStyleElement.SetElementStyle(...)` aracılığıyla yapılandırın. |
| Herhangi bir biçim (tek tip geçersiz kılma) | `PivotTable.FormatAll(Style)` | Pivot genelinde diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Kararsız kaldığınızda, `.xlsx` olarak kaydedin ve yerleşik temalar için `PivotTableStyleType`, özel temalar için `PivotTableStyleName` kullanın.

## Related Articles
- [Aspose.Cells for .NET'te Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for .NET'te Pivot Tablosu Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/)
- [Aspose.Cells for .NET'te Pivot Tablolarını Yenileme](/cells/tr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}