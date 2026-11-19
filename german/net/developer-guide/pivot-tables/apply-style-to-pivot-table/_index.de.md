---
title: Stile auf Pivot-Tabellen in Aspose.Cells for .NET anwenden
description: Erfahren Sie, wie Sie in Aspose.Cells for .NET integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen ab Excel 2007, benutzerdefinierten Pivot-Tabellen-Stilen und der FormatAll-Verknüpfung.
linktitle: Pivot-Tabellen-Stile anwenden
keywords: Aspose.Cells .NET Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt sowohl die Anwendung von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellen-Stilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden; in diesem Fall gilt die moderne Stil-API statt der Legacy-API.
- `PivotTable.PivotTableStyleType` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.PivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind immer dann erforderlich, wenn Sie Farben, Rahmen oder Schriftarten über das hinaus ändern möchten, was die Voreinstellungen bieten.
Darüber hinaus ist `PivotTable.FormatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alle über die beiden oben genannten Stilnamens-APIs gesetzten Einstellungen überschreibt. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Ein Legacy-XLS-Voreinstellungs-Autoformat anwenden**
`PivotTable.AutoFormatType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` und `Table1` bis `Table10`.
Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** ausschließlich mit Zeilenfeldern und Werten entwickelt — sie verfügen über keine integrierte Formatierung für Spaltenfeldüberschriften. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout moderner Excel-Versionen konzipiert sind.
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

## **Einen modernen benannten Pivot-Tabellen-Voreinstellungsstil anwenden**
`PivotTable.PivotTableStyleType` wählt eine der integrierten benannten Formatvorlagen aus, die Excel 2007 für PivotTables eingeführt hat. Die Enumeration `PivotTableStyleType` stellt drei Designfamilien bereit: die helle Familie von `PivotTableStyleLight1` bis `PivotTableStyleLight28`, die mittlere Familie von `PivotTableStyleMedium1` bis `PivotTableStyleMedium28` und die dunkle Familie von `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Sie definiert außerdem `None` und `Custom`. Die Mitglieder mit höheren Nummern innerhalb jeder Familie sind die in Excel 2017 hinzugefügten Formatvorlagen.
Diese Voreinstellungen sind schreibgeschützt. Sobald Sie Farben, Rahmen oder Schriftarten ändern müssen, die über die von einer Voreinstellung bereitgestellten hinausgehen, müssen Sie stattdessen eine benutzerdefinierte Pivot-Formatvorlage definieren, wie in [Szenario 3](#define-and-apply-a-custom-pivot-table-style) gezeigt wird.

{{% alert color="primary" %}}
**Warum die modernen Voreinstellungen und nicht die Autoformatierungen der Berichtsreihe?** Die Werte `Report1` bis `Report10` sowie `Table1` bis `Table10` von `PivotTableAutoFormatType` stammen aus der Zeit vor den Pivot-Spaltenfeldern. Daher enthalten sie keine Formatierung für die Kopfzeilen von Spaltenfeldern, und Excel rendert diese Kopfzeilen ohne Formatierung. Die Voreinstellungen von `PivotTableStyleType` wurden für das zweidimensionale Layout entwickelt, das moderne Excel-Versionen verwenden, und formatieren die Kopfzeilen von Zeilen- und Spaltenfeldern gleichermaßen.
{{% /alert %}}

Dieses Szenario verwendet erneut den Fruit/Year/Amount-Datensatz aus Szenario 1, fügt `Year` mithilfe von `PivotFieldType.Column` zum Spaltenbereich neben dem Zeilenfeld `Fruit` hinzu, wendet die Voreinstellung `PivotTableStyleDark1` des dunklen Designs über `PivotTable.PivotTableStyleType` an und speichert das Ergebnis als `.xlsx` – das Format, für das `PivotTableStyleType` sinnvoll ist.

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

## **Einen benutzerdefinierten Pivot-Tabellen-Stil definieren und anwenden**
Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Workflow umfasst drei Schritte:
1. Fügen Sie der `TableStyles`-Auflistung der Arbeitsmappe über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.TableStyleElements.Add(TableStyleElementType)` hinzufügen und jedem Element anschließend über `TableStyleElement.SetElementStyle(Style)` einen `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.PivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `PivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`PivotTableStyleName` und `PivotTableStyleType` sind nicht austauschbar. Verwenden Sie `PivotTableStyleType` für integrierte Voreinstellungen und `PivotTableStyleName` für benutzerdefinierte Stile, die Sie über `AddPivotTableStyle` definiert haben. Beides zu setzen ist harmlos, aber nur dasjenige, das der beabsichtigten Quelle entspricht, wird gerendert.
Die verfügbaren `TableStyleElementType`-Werte umfassen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.
Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WholeTable` und einer fetten roten Schriftart auf `GrandTotalRow`, wendet ihn anschließend über `PivotTableStyleName` an und speichert als `.xlsx`.
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

## **Einen Stil mit FormatAll auf jede Pivot-Zelle anwenden**
`PivotTable.FormatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Gesamtsummen. Alle zuvor über `PivotTableStyleType` oder `PivotTableStyleName` gesetzten Einstellungen werden überschrieben.

{{% alert color="primary" %}}
`FormatAll` überschreibt sowohl `PivotTableStyleType` als auch `PivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.
Das folgende Beispiel erstellt einen `Style` mit einer gelben Vollfüllung, einer fetten dunkelblauen Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn anschließend mit `FormatAll` an und speichert als `.xlsx`.
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

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.AutoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.PivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Zu verwenden, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `TableStyleElement.SetElementStyle(...)`. |
| Jedes Format (einheitliche Überschreibung) | `PivotTable.FormatAll(Style)` | Verknüpfung, die jede andere Stileinstellung über die gesamte Pivot-Tabelle hinweg überschreibt. |
Im Zweifelsfall speichern Sie als `.xlsx` und verwenden `PivotTableStyleType` für integrierte Designs oder `PivotTableStyleName` für benutzerdefinierte Designs.

## Verwandte Artikel
- [Zeilen- und Spaltenfelder zu Pivot-Tabellen in Aspose.Cells for .NET hinzufügen](/cells/de/net/pivot-table-add-row-and-column-fields/)
- [Wertfelder von Pivot-Tabellen in Aspose.Cells for .NET verwalten](/cells/de/net/manage-value-fields/)
- [Pivot-Tabellen in Aspose.Cells for .NET aktualisieren](/cells/de/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}