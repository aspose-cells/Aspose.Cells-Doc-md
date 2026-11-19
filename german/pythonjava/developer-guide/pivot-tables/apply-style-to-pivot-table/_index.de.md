---
title: Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Python via Java
linktitle: Anwenden von Stilen auf Pivot-Tabellen
description: Erfahren Sie, wie Sie integrierte und benutzerdefinierte Stile auf Pivot-Tabellen in Aspose.Cells for Python via Java anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Excel 2007+ Stilen, benutzerdefinierten Pivot-Tabellenstilen und der formatAll-Verknüpfung.
keywords: Aspose.Cells Python via Java Pivot-Tabellenstil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt sowohl die Anwendung von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch modernen benannten oder benutzerdefinierten Pivot-Tabellenstilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden; in diesem Fall kommt die moderne Stil-API zum Einsatz, nicht die Legacy-API.
- `pivotTable.setPivotTableStyleType(int)` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `pivotTable.setPivotTableStyleName(String)` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten über das hinaus ändern möchten, was die Voreinstellungen bieten.
Zusätzlich ist `pivotTable.formatAll(Style)` ein Kurzbefehl, der ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alles überschreibt, was über eine der oben genannten Stilnamen-APIs festgelegt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Legacy-XLS-Voreinstellungs-Autoformat anwenden**
Die Methode `setAutoFormatType` für eine Pivot-Tabelle akzeptiert einen Wert aus der Aufzählung `com.aspose.cells.pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `REPORT_1` bis `REPORT_10`, `CLASSIC` und `TABLE_1` bis `TABLE_10`.
Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.REPORT_5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** ausschließlich mit Zeilenfeldern und Werten entworfen — sie verfügen über keine integrierte Formatierung für Spaltenfeldüberschriften. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout des modernen Excel konzipiert sind.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Create a new workbook
workbook = Workbook()
# Get the first worksheet
sheet = workbook.getWorksheets().get(0)
# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# Add a pivot table at destination cell E3, using source range A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Save the workbook in legacy .xls format
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Modernen benannten Pivot-Tabellen-Voreinstellungsstil anwenden**
`pivotTable.setPivotTableStyleType(int)` wählt eine der integrierten benannten Formatvorlagen aus, die Excel 2007 für Pivot-Tabellen eingeführt hat. Die Enumeration `PivotTableStyleType` stellt drei Designfamilien bereit: die helle Familie von `PIVOT_TABLE_STYLE_LIGHT1` bis `PIVOT_TABLE_STYLE_LIGHT28`, die mittlere Familie von `PIVOT_TABLE_STYLE_MEDIUM1` bis `PIVOT_TABLE_STYLE_MEDIUM28` und die dunkle Familie von `PIVOT_TABLE_STYLE_DARK1` bis `PIVOT_TABLE_STYLE_DARK_28`. Außerdem definiert sie `None` und `Custom`. Die Mitglieder mit höheren Nummern innerhalb jeder Familie sind die Formatvorlagen, die in Excel 2017 hinzugefügt wurden.
Diese Presets sind schreibgeschützt. Sobald Sie Farben, Rahmen oder Schriften ändern müssen und damit über den Umfang eines Presets hinausgehen, müssen Sie stattdessen ein benutzerdefiniertes Pivot-Format definieren, wie in [Szenario 3](#define-and-apply-a-custom-pivot-table-style) gezeigt wird.

{{% alert color="primary" %}}
**Warum die modernen Presets und nicht die Autoformate der Report-Reihe?** Die Werte `Report1` bis `Report10` und `Table1` bis `Table10` von `PivotTableAutoFormatType` stammen aus der Zeit vor Pivot-Spaltenfeldern und enthalten daher keine Formatierung für die Kopfzeilen von Spaltenfeldern, sodass Excel diese Kopfzeilen ohne Formatierung rendert. Die Presets von `PivotTableStyleType` wurden für das zweidimensionale Layout entwickelt, das moderne Excel-Versionen verwenden, und formatieren sowohl die Kopfzeilen von Zeilenfeldern als auch die von Spaltenfeldern.
{{% /alert %}}

Dieses Szenario verwendet erneut den Datensatz Fruit/Year/Amount aus Szenario 1, fügt `Year` über `PivotFieldType.COLUMN` neben dem Zeilenfeld `Fruit` zum Spaltenbereich hinzu, wendet mit `pivotTable.setPivotTableStyleType` das Preset `PIVOT_TABLE_STYLE_DARK1` mit dunklem Design an und speichert das Ergebnis im Format `.xlsx` – also in dem Format, für das `PivotTableStyleType` sinnvoll ist.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)
# Add a pivot table at E3, sourced from A1:C10
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Benutzerdefinierten Pivot-Tabellenstil definieren und anwenden**
Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:
1. Fügen Sie der `TableStyles`-Auflistung der Arbeitsmappe über `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` einen benutzerdefinierten Stil hinzu. Diese Methode gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WHOLE_TABLE` oder `GRAND_TOTAL_ROW`) über `tableStyle.getTableStyleElements().add(TableStyleElementType)` hinzufügen, und weisen Sie dann jedem Element über `tableStyleElement.setElementStyle(Style)` einen `Style` zu.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `pivotTable.setPivotTableStyleName(String)` mit dem Namen des Stils aufrufen. Verwenden Sie hier nicht `setPivotTableStyleType`, da diese Methode integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`setPivotTableStyleName` und `setPivotTableStyleType` sind nicht austauschbar. Verwenden Sie `setPivotTableStyleType` für integrierte Voreinstellungen und `setPivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Das Festlegen beider Werte ist harmlos, aber nur der Wert, der der beabsichtigten Quelle entspricht, wird gerendert.
Die verfügbaren `TableStyleElementType`-Werte umfassen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` und `PAGE_FIELD_VALUES`.
Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen für `WHOLE_TABLE` und einer fetten roten Schriftart für `GRAND_TOTAL_ROW`, wendet ihn dann über `setPivotTableStyleName` an und speichert als `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# Add pivot table sourced from A1:C10, anchored at E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Step 1: register a new custom pivot table style and capture its index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# Step 2: add a WholeTable element and apply thin black borders on all four sides
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Step 3: add a GrandTotalRow element and apply bold red font
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Mit formatAll einen Stil auf jede Pivot-Zelle anwenden**
`pivotTable.formatAll(Style)` ist ein Kurzbefehl, der ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Alles, was zuvor über `setPivotTableStyleType` oder `setPivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}
`formatAll` überschreibt sowohl `setPivotTableStyleType` als auch `setPivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.
Das folgende Beispiel erstellt einen `Style` mit einer gelben Vollfüllung, einer fetten dunkelblauen Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn dann mit `formatAll` an und speichert als `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Scenario 4: Apply a single Style to every pivot table cell using formatAll
# API in use: PivotTable.formatAll(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# Add pivot table: source range A1:C10, destination cell E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Build a Style that will be forced onto every cell of the pivot table
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# Apply formatAll: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style)
# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `pivotTable.setAutoFormatType(int)` | Werte aus `com.aspose.cells.pivot.PivotTableAutoFormatType` (z. B. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `pivotTable.setPivotTableStyleType(int)` | Werte aus `com.aspose.cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Zu verwenden, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `tableStyleElement.setElementStyle(Style)`. |
| Beliebiges Format (einheitliche Überschreibung) | `pivotTable.formatAll(Style)` | Kurzbefehl, der jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |
Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `setPivotTableStyleType` für integrierte Designs oder `setPivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="python" >}}