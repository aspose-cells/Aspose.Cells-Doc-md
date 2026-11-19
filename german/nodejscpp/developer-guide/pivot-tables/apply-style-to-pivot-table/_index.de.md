---
title: Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Node.js via C++
linktitle: Anwenden von Stilen auf Pivot-Tabellen
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen ab Excel 2007+, benutzerdefinierten Pivot-Tabellen-Stilen und der formatAll-Abkürzung.
keywords: Aspose.Cells Node.js via C++ Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt sowohl die Anwendung von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellen-Stilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall gilt die moderne Stil-API anstelle der Legacy-API.
- `PivotTable.PivotTableStyleType` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.PivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `Workbook.Worksheets.TableStyles.addPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind immer dann erforderlich, wenn Sie Farben, Rahmen oder Schriftarten ändern möchten, die über die Voreinstellungen hinausgehen.
Darüber hinaus ist `PivotTable.formatAll(Style)` eine Abkürzung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alles überschreibt, was über eine der oben genannten Stilnamen-APIs festgelegt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**
`PivotTable.AutoFormatType` akzeptiert einen Wert aus der Aufzählung `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` und `Table1` bis `Table10`.
Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** mit nur Zeilenfeldern und Werten entwickelt — sie verfügen über keine integrierte Formatierung für Spaltenfeld-Header. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout moderner Excel-Versionen konzipiert sind.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
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
// Add a pivot table at destination cell E3, using source range A1:C10
const pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungs-Stils**
`PivotTable.pivotTableStyleType` wählt eine der integrierten benannten Formatvorlagen aus, die Excel 2007 für Pivot-Tabellen eingeführt hat. Die Enumeration `PivotTableStyleType` stellt drei Designfamilien bereit: die helle Familie von `PivotTableStyleLight1` bis `PivotTableStyleLight28`, die mittlere Familie von `PivotTableStyleMedium1` bis `PivotTableStyleMedium28` und die dunkle Familie von `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Sie definiert außerdem `None` und `Custom`. Die Mitglieder mit höheren Nummern jeder Familie sind die in Excel 2017 hinzugefügten Formatvorlagen.
Diese Voreinstellungen sind schreibgeschützt. Sobald Sie Farben, Rahmen oder Schriftarten über den von einer Voreinstellung bereitgestellten Umfang hinaus ändern müssen, müssen Sie stattdessen eine benutzerdefinierte Pivot-Formatvorlage definieren, wie in [Szenario 3](#define-and-apply-a-custom-pivot-table-style) gezeigt wird.

{{% alert color="primary" %}}
**Warum die modernen Voreinstellungen und nicht die automatischen Formatierungen der Berichtsreihe?** Die Werte `Report1` bis `Report10` und `Table1` bis `Table10` von `PivotTableAutoFormatType` stammen aus der Zeit vor den Pivot-Spaltenfeldern, enthalten daher keine Formatierung für Spaltenfeldüberschriften, und Excel rendert diese Überschriften ohne Formatierung. Die Voreinstellungen von `PivotTableStyleType` wurden für das zweidimensionale Layout entworfen, das moderne Excel-Versionen verwenden, und formatieren die Überschriften von Zeilen- und Spaltenfeldern gleichermaßen.
{{% /alert %}}

Dieses Szenario verwendet erneut den Fruit/Year/Amount-Datensatz aus Szenario 1, fügt `Year` über `PivotFieldType.Column` dem Spaltenbereich neben dem Zeilenfeld `Fruit` hinzu, wendet die Voreinstellung für das dunkle Design `PivotTableStyleDark1` mit `pivotTable.setPivotTableStyleType` an und speichert das Ergebnis als `.xlsx` — das Format, für das `PivotTableStyleType` relevant ist.

```javascript
const AsposeCells = require("aspose.cells.node");
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
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellen-Stils**
Die integrierten Voreinstellungen können nicht geändert werden. Wann immer Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:
1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe über `Workbook.Worksheets.TableStyles.addPivotTableStyle(string name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.TableStyleElements.Add(TableStyleElementType)` hinzufügen und dann jedem Element über `TableStyleElement.SetElementStyle(Style)` einen `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.PivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `PivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`PivotTableStyleName` und `PivotTableStyleType` sind nicht austauschbar. Verwenden Sie `PivotTableStyleType` für integrierte Voreinstellungen und `PivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Das Setzen beider ist harmlos, aber nur dasjenige, das der beabsichtigten Quelle entspricht, wird gerendert.
Die verfügbaren `TableStyleElementType`-Werte umfassen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.
Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WholeTable` und einer fetten roten Schriftart auf `GrandTotalRow`, wendet ihn dann über `PivotTableStyleName` an und speichert als `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row + 9 data rows (A1:C10)
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
// Add pivot table sourced from A1:C10, anchored at E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Step 2: add a WholeTable element and apply thin black borders on all four sides
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
// Step 3: add a GrandTotalRow element and apply bold red font
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Anwenden eines Stils auf jede Pivot-Zelle mit formatAll**
`PivotTable.formatAll(Style)` ist eine Abkürzung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spalten-Header sowie der Summen. Alles, was zuvor über `PivotTableStyleType` oder `PivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}
`formatAll` überschreibt sowohl `PivotTableStyleType` als auch `PivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.
Das folgende Beispiel erstellt einen `Style` mit gelber Vollfüllung, fetter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn dann mit `formatAll` an und speichert als `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
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
// Add pivot table: source range A1:C10, destination cell E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
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
// Apply formatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style);
// Save the workbook in the modern .xlsx format
workbook.save("output.xlsx");
```

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.AutoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.PivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich Excel 2017-Erweiterungen). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `TableStyleElement.SetElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.formatAll(Style)` | Abkürzung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |
Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `PivotTableStyleType` für integrierte Designs oder `PivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="nodejs-cpp" >}}