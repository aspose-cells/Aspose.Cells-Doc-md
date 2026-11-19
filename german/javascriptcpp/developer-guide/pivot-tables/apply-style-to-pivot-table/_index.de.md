---
title: Stile auf PivotTables in Aspose.Cells for JavaScript via C++ anwenden
linktitle: Stile auf PivotTables
description: Erfahren Sie, wie Sie integrierte und benutzerdefinierte Stile auf PivotTables in Aspose.Cells for JavaScript via C++ anwenden, einschließlich herkömmlicher XLS-Autoformatierungen, moderner benannter Stile ab Excel 2007, benutzerdefinierter PivotTable-Stile und der Kurzform FormatAll.
keywords: Aspose.Cells for JavaScript via C++, PivotTable-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/javascript-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt sowohl die Anwendung herkömmlicher PivotTable-Autoformate (für `.xls`-Dateien) als auch moderner benannter oder benutzerdefinierter PivotTable-Stile (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien). Welche API Sie verwenden sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für PivotTables bereit. Die Auswahl richtet sich nach dem Dateiformat, in dem Sie die Arbeitsmappe speichern, nicht nach dem Format, aus dem Sie sie laden. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` gespeichert werden. In diesem Fall wird die moderne Stil-API und nicht die herkömmliche angewendet.
- `pivotTable.pivotTableStyleType` wählt einen der integrierten benannten Stile (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile) aus. Diese Voreinstellungen sind schreibgeschützt.
- `pivotTable.pivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `workbook.worksheets.tableStyles.addPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Änderungen an Farben, Rahmen oder Schriften vornehmen möchten, die über die von den Voreinstellungen angebotenen Optionen hinausgehen.
Zusätzlich ist `pivotTable.formatAll(style)` eine Kurzform, die ein einzelnes `style`-Objekt auf jede Zelle der PivotTable anwendet und dabei alle Einstellungen überschreibt, die über eine der beiden oben genannten Stil-APIs festgelegt wurden. Dies ist hilfreich, wenn unabhängig vom zugrunde liegenden Design ein einheitliches Erscheinungsbild erforderlich ist.

## **Eine vorgegebene Autoformatierung für das herkömmliche XLS-Format anwenden**
`pivotTable.autoFormatType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` sowie `Table1` bis `Table10`.
Das folgende Beispiel erstellt eine neue Arbeitsmappe, füllt die Beispieldaten Fruit/Year/Amount ein, fügt eine PivotTable hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Die Autoformatierungen der Berichtsreihe (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden in klassischen Excel-Versionen für **eindimensionale PivotTables** mit ausschließlich Zeilenfeldern und Werten entwickelt; sie bieten keine integrierte Formatierung für Spaltenfeldüberschriften. Wenn Ihre PivotTable Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout moderner Excel-Versionen ausgelegt sind.
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

## **Eine moderne Voreinstellung für benannte PivotTable-Stile anwenden**
`pivotTable.pivotTableStyleType` wählt einen der integrierten benannten Stile aus, die Excel 2007 für PivotTables eingeführt hat. Die Enumeration `PivotTableStyleType` stellt drei Designfamilien bereit: die helle Familie von `PivotTableStyleLight1` bis `PivotTableStyleLight28`, die mittlere Familie von `PivotTableStyleMedium1` bis `PivotTableStyleMedium28` und die dunkle Familie von `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Sie definiert außerdem `None` und `Custom`. Die höher nummerierten Mitglieder jeder Familie sind die in Excel 2017 hinzugefügten Stile.
Diese Voreinstellungen sind schreibgeschützt. Sobald Sie Farben, Rahmen oder Schriften ändern möchten, die über das hinausgehen, was eine Voreinstellung bietet, müssen Sie stattdessen einen benutzerdefinierten PivotTable-Stil definieren, wie in [Szenario 3](#define-and-apply-a-custom-pivot-table-style) gezeigt wird.

{{% alert color="primary" %}}
**Warum die modernen Voreinstellungen und nicht die Autoformatierungen der Berichtsreihe?** Die Werte `Report1` bis `Report10` und `Table1` bis `Table10` von `PivotTableAutoFormatType` stammen aus der Zeit vor der Einführung von PivotTable-Spaltenfeldern und enthalten daher keine Formatierung für Spaltenfeldüberschriften; Excel stellt diese Überschriften ohne Formatierung dar. Die `PivotTableStyleType`-Voreinstellungen wurden für das zweidimensionale Layout moderner Excel-Versionen entwickelt und formatieren sowohl Zeilenfeld- als auch Spaltenfeldüberschriften.
{{% /alert %}}

Dieses Szenario verwendet erneut den Fruit/Year/Amount-Datensatz aus Szenario 1, fügt `Year` über `PivotFieldType.Column` zum Spaltenbereich hinzu und behält `Fruit` als Zeilenfeld bei. Anschließend wird mit `pivotTable.pivotTableStyleType` die Voreinstellung `PivotTableStyleDark1` für das dunkle Design angewendet und das Ergebnis als `.xlsx` gespeichert – dem Format, für das `PivotTableStyleType` relevant ist.

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

## **Einen benutzerdefinierten PivotTable-Stil definieren und anwenden**
Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriften ändern müssen, definieren Sie stattdessen einen benutzerdefinierten PivotTable-Stil. Der Arbeitsablauf umfasst drei Schritte:
1. Fügen Sie der `tableStyles`-Sammlung der Arbeitsmappe über `workbook.worksheets.tableStyles.addPivotTableStyle(name)` einen benutzerdefinierten Stil hinzu. Die Methode gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (z. B. `WholeTable` oder `GrandTotalRow`) über `tableStyle.tableStyleElements.add(tableStyleElementType)` hinzufügen und jedem Element anschließend über `tableStyleElement.setElementStyle(style)` einen `style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die PivotTable an, indem Sie `pivotTable.pivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `pivotTable.pivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`pivotTable.pivotTableStyleName` und `pivotTable.pivotTableStyleType` sind nicht austauschbar. Verwenden Sie `pivotTable.pivotTableStyleType` für integrierte Voreinstellungen und `pivotTable.pivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Das Festlegen beider Eigenschaften ist unkritisch; wirksam wird jedoch nur die Einstellung der Eigenschaft, die der beabsichtigten Quelle entspricht.
Zu den verfügbaren Werten von `TableStyleElementType` gehören `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.
Das folgende Beispiel definiert einen benutzerdefinierten PivotTable-Stil mit einem dünnen schwarzen Rahmen für `WholeTable` und einer fett formatierten roten Schrift für `GrandTotalRow`, wendet ihn über `pivotTable.pivotTableStyleName` an und speichert das Ergebnis als `.xlsx`.
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

## **Einen Stil mit formatAll auf jede PivotTable-Zelle anwenden**
`pivotTable.formatAll(style)` ist eine Kurzform, die ein einzelnes `style`-Objekt auf jede Zelle der PivotTable anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Alles, was zuvor über `pivotTable.pivotTableStyleType` oder `pivotTable.pivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}
`formatAll` überschreibt sowohl `pivotTable.pivotTableStyleType` als auch `pivotTable.pivotTableStyleName`. Verwenden Sie die Methode nur, wenn in der gesamten PivotTable ein einheitliches, vom Design unabhängiges Erscheinungsbild erforderlich ist.
Das folgende Beispiel erstellt einen `style` mit einer gelben Volltonfüllung, einer fett formatierten dunkelblauen Schrift und dünnen schwarzen Rahmen an allen Seiten, wendet ihn mit `formatAll` an und speichert das Ergebnis als `.xlsx`.
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

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie die Arbeitsmappe speichern. Die folgende Tabelle dient als schnelle Referenz.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (herkömmlich) | `pivotTable.autoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `pivotTable.pivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `pivotTable.pivotTableStyleName` + `workbook.worksheets.tableStyles.addPivotTableStyle(...)` | Verwenden Sie diese API, wenn die integrierten Voreinstellungen nicht ausreichen. Konfigurieren Sie den Stil über `tableStyleElement.setElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `pivotTable.formatAll(style)` | Kurzform, die alle anderen Stileinstellungen in der gesamten PivotTable überschreibt. |
Wenn Sie unsicher sind, speichern Sie als `.xlsx` und verwenden Sie `pivotTable.pivotTableStyleType` für integrierte Designs oder `pivotTable.pivotTableStyleName` für benutzerdefinierte Stile.

{{< app/cells/assistant language="javascript-cpp" >}}