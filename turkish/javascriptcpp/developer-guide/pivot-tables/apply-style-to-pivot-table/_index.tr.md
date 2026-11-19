---
title: Aspose.Cells for JavaScript via C++ ile Özet Tablolara Stilleri Uygulama
linktitle: Pivot Tablo Stillerini Uygula
description: Aspose.Cells for JavaScript via C++ ile özet tablolara yerleşik ve özel stillerin nasıl uygulanacağını öğrenin; eski XLS otomatik biçimlendirmelerini, Excel 2007 ve sonrası için modern adlandırılmış stilleri, özel özet tablo stillerini ve FormatAll kısayolunu ele alın.
keywords: Aspose.Cells for JavaScript via C++ özet tablo stili, PivotTableStyleType, AutoFormatType, FormatAll, özel stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /tr/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, hem eski özet tablo otomatik biçimlendirmelerinin (`.xls` dosyaları için tasarlanmış) hem de modern adlandırılmış veya özel özet tablo stillerinin (`.xlsx`, `.xlsm` ve `.xlsb` dosyaları için tasarlanmış) uygulanmasını destekler. Çağırmanız gereken API, çalışma kitabının kaydedildiği dosya biçimine bağlıdır; yüklenme biçimine bağlı değildir.
{{% /alert %}}

## **Giriş**
Aspose.Cells, özet tablolar için birbirine paralel iki stil API'si sunar. Bu API'ler arasındaki seçim, çalışma kitabının okunduğu biçime değil, kaydedildiği dosya biçimine göre belirlenir. `.xls` dosyasından yüklenen bir çalışma kitabı `.xlsx` olarak yeniden kaydedilebilir; bu durumda eski stil API'si yerine modern stil API'si uygulanır.
- `pivotTable.pivotTableStyleType`, Excel 2017'de eklenen stiller dâhil, açık ve koyu temalardaki yerleşik adlandırılmış stillerden birini seçer. Bu hazır stiller salt okunurdur.
- `pivotTable.pivotTableStyleName`, `workbook.worksheets.tableStyles.addPivotTableStyle(...)` aracılığıyla kendiniz tanımladığınız özel bir stili seçer. Hazır stillerin sunduğunun ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmek istediğinizde özel stiller gerekir.
Ayrıca, `pivotTable.formatAll(style)`, tek bir `style` nesnesini özet tablosunun her hücresine uygulayan ve yukarıdaki iki API aracılığıyla yapılan tüm ayarları geçersiz kılan bir kısayoldur. Bu, kullanılan temadan bağımsız olarak her yerde aynı görünüm gerektiğinde yararlıdır.

## **Eski XLS Hazır Otomatik Biçimlendirmesini Uygula**
`pivotTable.autoFormatType`, `Aspose.Cells.Pivot.PivotTableAutoFormatType` numaralandırmasından bir değer kabul eder. Kullanılabilir değerler şunlardır: `Report1`–`Report10`, `Classic` ve `Table1`–`Table10`.
Aşağıdaki örnek yeni bir çalışma kitabı yükler, Fruit/Year/Amount örnek verilerini yerleştirir, bir özet tablo ekler, `PivotTableAutoFormatType.Report5` uygular ve sonucu `.xls` olarak kaydeder.

{{% alert color="primary" %}}
**Neden sütun alanları yok?** Rapor serisi otomatik biçimlendirmeleri (`Report1` ile `Report10`, `Table1` ile `Table10`), klasik Excel'de yalnızca satır alanları ve değerler içeren **tek boyutlu özet tablolar** için tasarlanmıştır; sütun alanı başlıkları için yerleşik biçimlendirme içermezler. Özet tablonuzun sütun alanlarına ihtiyacı varsa bunun yerine [Senaryo 2](#apply-a-modern-named-preset-pivot-table-style) bağlantısındaki modern `PivotTableStyleType` ön ayarlarını kullanın; bu ön ayarlar, modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 1: Apply a legacy XLS preset autoformat
            // API in use: PivotTable.AutoFormatType
            // Target file format: .xls (legacy)
            // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
            // Create a new workbook
            const workbook = new Workbook();
            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Populate the source data with header row (Fruit, Year, Amount)
            // and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
            cells.get(0, 0).value = "Fruit";
            cells.get(0, 1).value = "Year";
            cells.get(0, 2).value = "Amount";
            cells.get(1, 0).value = "grape";
            cells.get(1, 1).value = 2020;
            cells.get(1, 2).value = 50;
            cells.get(2, 0).value = "blueberry";
            cells.get(2, 1).value = 2020;
            cells.get(2, 2).value = 30;
            cells.get(3, 0).value = "kiwi";
            cells.get(3, 1).value = 2020;
            cells.get(3, 2).value = 25;
            cells.get(4, 0).value = "cherry";
            cells.get(4, 1).value = 2020;
            cells.get(4, 2).value = 40;
            cells.get(5, 0).value = "grape";
            cells.get(5, 1).value = 2021;
            cells.get(5, 2).value = 60;
            cells.get(6, 0).value = "blueberry";
            cells.get(6, 1).value = 2021;
            cells.get(6, 2).value = 35;
            cells.get(7, 0).value = "kiwi";
            cells.get(7, 1).value = 2021;
            cells.get(7, 2).value = 28;
            cells.get(8, 0).value = "cherry";
            cells.get(8, 1).value = 2021;
            cells.get(8, 2).value = 45;
            cells.get(9, 0).value = "grape";
            cells.get(9, 1).value = 2020;
            cells.get(9, 2).value = 45;
            // Add a pivot table at destination cell E3, using source range A1:C10
            const pivotTable = sheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign fields: Fruit -> Rows, Amount -> Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply the legacy XLS preset autoformat "Report5"
            // Note: This property is only meaningful when saving as .xls.
            // When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
            // and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;
            // Save the workbook in legacy .xls format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xls";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Excel 2007+ Adlandırılmış Hazır Özet Tablo Stilini Uygula**
`pivotTable.pivotTableStyleType`, Excel 2007 ile özet tablolar için sunulan yerleşik adlandırılmış stillerden birini seçer. `PivotTableStyleType` numaralandırması üç tema ailesi içerir: `PivotTableStyleLight1` ile `PivotTableStyleLight28` arasındaki açık tema ailesi, `PivotTableStyleMedium1` ile `PivotTableStyleMedium28` arasındaki orta tema ailesi ve `PivotTableStyleDark1` ile `PivotTableStyleDark28` arasındaki koyu tema ailesi. Ayrıca `None` ve `Custom` değerlerini tanımlar. Her ailenin daha yüksek numaralı üyeleri, Excel 2017'de eklenen stillerdir.
Bu hazır stiller salt okunurdur. Bir stilin sunduğunun ötesinde renkleri, kenarlıkları veya yazı tiplerini değiştirmeniz gerektiğinde bunun yerine özel bir özet tablo stili tanımlamanız gerekir; [Senaryo 3](#define-and-apply-a-custom-pivot-table-style) bağlantısı bunu göstermektedir.

{{% alert color="primary" %}}
**Neden rapor serisi otomatik biçimlendirmeleri yerine modern hazır stiller?** `PivotTableAutoFormatType` içindeki `Report1`–`Report10` ve `Table1`–`Table10` değerleri, özet tablo sütun alanlarından önce geliştirilmiştir; bu nedenle sütun alanı başlıkları için stil tanımlamaz ve Excel bu başlıkları biçimlendirmeden görüntüler. `PivotTableStyleType` ön ayarları ise modern Excel'in kullandığı iki boyutlu düzen için tasarlanmıştır ve hem satır alanı hem de sütun alanı başlıklarına stil uygular.
{{% /alert %}}

Bu senaryo, birinci senaryodaki Fruit/Year/Amount veri kümesini yeniden kullanır, `Fruit` satır alanının yanına `Year` alanını `PivotFieldType.Column` aracılığıyla sütun alanına ekler, `pivotTable.pivotTableStyleType` kullanarak koyu tema ön ayarı `PivotTableStyleDark1` değerini uygular ve sonucu `.xlsx` olarak kaydeder. Bu, `PivotTableStyleType` özelliğinin anlamlı olduğu biçimdir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
            // Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
            // (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
            // GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Header row: Fruit / Year / Amount
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // 9 data rows of Fruit / Year / Amount
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 150;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 200;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 180;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 120;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 170;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 210;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 190;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 130;
            // Add a pivot table at E3, sourced from A1:C10
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Apply a modern Excel 2007+ named preset pivot style.
            // PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
            // is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
            // family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
            // newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
            pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;
            // Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

## **Özel Bir Özet Tablo Stili Tanımlayın ve Uygulayın**
Yerleşik stiller değiştirilemez. Farklı renkler, kenarlıklar veya yazı tipleri uygulamak istediğinizde özel bir özet tablo stili tanımlamanız gerekir. İş akışı üç adımdan oluşur:
1. Çalışma kitabının `tableStyles` koleksiyonuna `workbook.worksheets.tableStyles.addPivotTableStyle(name)` aracılığıyla özel bir stil ekleyin. Bu işlem, oluşturulan yeni stilin indeksini döndürür.
2. `tableStyle.tableStyleElements.add(tableStyleElementType)` aracılığıyla `WholeTable` veya `GrandTotalRow` gibi öğeler ekleyerek stili yapılandırın; ardından `tableStyleElement.setElementStyle(style)` aracılığıyla her öğeye bir `style` atayın.
3. `pivotTable.pivotTableStyleName` özelliğini stilin adına ayarlayarak özel stili özet tablosuna uygulayın. Burada `pivotTable.pivotTableStyleType` özelliğini kullanmayın; çünkü bu özellik yerleşik ön ayarları seçer.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` ve `pivotTable.pivotTableStyleType` birbirinin yerine kullanılamaz. Yerleşik ön ayarlar için `pivotTable.pivotTableStyleType`, `addPivotTableStyle` aracılığıyla tanımladığınız özel stiller için `pivotTable.pivotTableStyleName` kullanın. İkisini birlikte ayarlamak zararsızdır; ancak yalnızca amaçlanan kaynağa uygun olan stil uygulanır.
Mevcut `TableStyleElementType` değerleri şunlardır: `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` ve `PageFieldValues`.
Aşağıdaki örnek, `WholeTable` üzerinde ince siyah kenarlık ve `GrandTotalRow` üzerinde kalın kırmızı yazı tipi bulunan özel bir özet tablo stili tanımlar; ardından stili `pivotTable.pivotTableStyleName` aracılığıyla uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Populate source data: header row + 9 data rows (A1:C10)
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 100;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 200;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 300;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 400;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 500;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 600;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 700;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 800;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 900;
            // Add pivot table sourced from A1:C10, anchored at E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Step 1: register a new custom pivot table style and capture its index
            const styleIndex = workbook.worksheets.tableStyles.addPivotTableStyle("CustomPivotStyle");
            const tableStyle = workbook.worksheets.tableStyles.get(styleIndex);
            // Step 2: add a WholeTable element and apply thin black borders on all four sides
            const wholeTableElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.WholeTable);
            const wholeTableElement = tableStyle.tableStyleElements.get(wholeTableElementIndex);
            const wholeTableStyle = workbook.createStyle();
            const topBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.TopBorder);
            topBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            topBorder.color = "black";
            const bottomBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.BottomBorder);
            bottomBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            bottomBorder.color = "black";
            const leftBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.LeftBorder);
            leftBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            leftBorder.color = "black";
            const rightBorder = wholeTableStyle.borders.get(AsposeCells.BorderType.RightBorder);
            rightBorder.lineStyle = AsposeCells.CellBorderType.Thin;
            rightBorder.color = "black";
            wholeTableElement.setElementStyle(wholeTableStyle);
            // Step 3: add a GrandTotalRow element and apply bold red font
            const grandTotalElementIndex = tableStyle.tableStyleElements.add(AsposeCells.TableStyleElementType.GrandTotalRow);
            const grandTotalElement = tableStyle.tableStyleElements.get(grandTotalElementIndex);
            const grandTotalStyle = workbook.createStyle();
            grandTotalStyle.font.isBold = true;
            grandTotalStyle.font.color = "red";
            grandTotalElement.setElementStyle(grandTotalStyle);
            // Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
            pivotTable.pivotTableStyleName = "CustomPivotStyle";
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **formatAll ile Her Özet Tablo Hücresine Tek Stil Uygulama**
`pivotTable.formatAll(style)`, tek bir `style` nesnesini özet tablosunun her hücresine uygulayan bir kısayoldur; veri alanı, satır ve sütun başlıkları ile toplamlar da buna dahildir. `pivotTable.pivotTableStyleType` veya `pivotTable.pivotTableStyleName` aracılığıyla daha önce yapılan tüm ayarlar geçersiz kılınır.

{{% alert color="primary" %}}
`formatAll`, hem `pivotTable.pivotTableStyleType` hem de `pivotTable.pivotTableStyleName` ayarlarını geçersiz kılar. Yalnızca tüm özet tablo boyunca tek tip ve temadan bağımsız bir görünüm gerektiğinde kullanın.
Aşağıdaki örnek, sarı düz dolguya, kalın koyu mavi yazı tipine ve dört tarafında ince siyah kenarlığa sahip bir `style` oluşturur; ardından `formatAll` kullanarak uygular ve `.xlsx` olarak kaydeder.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Scenario 4: Apply a single Style to every pivot table cell using FormatAll
            // API in use: PivotTable.FormatAll(Style)
            // Target format: .xlsx
            // GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            // Populate source data: header row (row 1) + 9 data rows (rows 2-10)
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            cells.get("A2").value = "Grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 5000;
            cells.get("A3").value = "Blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 3000;
            cells.get("A4").value = "Kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 4000;
            cells.get("A5").value = "Cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 2000;
            cells.get("A6").value = "Grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 6000;
            cells.get("A7").value = "Blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 3500;
            cells.get("A8").value = "Kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 4500;
            cells.get("A9").value = "Cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 2500;
            cells.get("A10").value = "Grape";
            cells.get("B10").value = 2021;
            cells.get("C10").value = 5500;
            // Add pivot table: source range A1:C10, destination cell E3
            const pivotTable = worksheet.pivotTables.add("=A1:C10", 2, 4);
            // Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Build a Style that will be forced onto every cell of the pivot table
            const style = workbook.createStyle();
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.font.isBold = true;
            style.font.color = AsposeCells.Color.DarkBlue;
            style.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.TopBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.LeftBorder).color = AsposeCells.Color.Black;
            style.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
            style.borders.get(AsposeCells.BorderType.RightBorder).color = AsposeCells.Color.Black;
            // Apply FormatAll: forces this single style onto every cell of the pivot table,
            // overriding any PivotTableStyleType / PivotTableStyleName previously set
            pivotTable.formatAll(style);
            // Save the workbook in the modern .xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Hangi Stil API'sini Kullanmalıyım?**
Stil API'si seçimi, kaydettiğiniz dosya biçimine bağlıdır. Hızlı bir başvuru için aşağıdaki tabloyu kullanın.
| Hedef dosya biçimi | Kullanılacak API | Notlar |
|---|---|---|
| `.xls` (eski) | `pivotTable.autoFormatType` | `Aspose.Cells.Pivot.PivotTableAutoFormatType` değerleri (örn. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Modern biçimlerde kaydedilirken yok sayılır. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, yerleşik stil) | `pivotTable.pivotTableStyleType` | `Aspose.Cells.PivotTableStyleType` değerleri (Excel 2017'de eklenenler dâhil açık/koyu temalar). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, özel stil) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Yerleşik ön ayarlar yeterli olmadığında kullanın. `tableStyleElement.setElementStyle(...)` aracılığıyla yapılandırın. |
| Her biçim (tek tip stil) | `pivotTable.formatAll(style)` | Özet tablosunun tamamındaki diğer tüm stil ayarlarını geçersiz kılan kısayol. |
Tereddüt ederseniz `.xlsx` olarak kaydedin; yerleşik temalar için `pivotTable.pivotTableStyleType`, özel temalar için `pivotTable.pivotTableStyleName` kullanın.

{{< app/cells/assistant language="javascript-cpp" >}}