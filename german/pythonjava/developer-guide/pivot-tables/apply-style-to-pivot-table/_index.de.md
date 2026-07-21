---
title: Anwenden von Stilen auf Pivot-Tabellen
linktitle: Anwenden von Stilen auf Pivot-Tabellen
description: Erfahren Sie, wie Sie integrierte und benutzerdefinierte Stile auf Pivot-Tabellen in Aspose.Cells for Python via Java anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen aus Excel 2007+, benutzerdefinierten Pivot-Tabellen-Stilen und der FormatAll-Verknüpfung.
keywords: Aspose.Cells Python via Java Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt sowohl Legacy-Pivot-Autoformate (für `.xls`-Dateien vorgesehen) als auch moderne benannte oder benutzerdefinierte Pivot-Tabellen-Stile (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.

{{% /alert %}}

## **Einführung**

Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall gilt die moderne Stil-API anstelle der Legacy-API.

Für Legacy-`.xls`-Ausgaben verwenden Sie die Methode `pivotTable.setAutoFormatType(int)` zusammen mit der Enumeration `com.aspose.cells.pivot.PivotTableAutoFormatType`. Diese API entspricht der Autoformat-Auswahl, die das klassische Excel für Pivot-Tabellen angeboten hat.

Für moderne `.xlsx`-, `.xlsm`- und `.xlsb`-Ausgaben stehen zwei Varianten der Stil-API zur Verfügung:

- `pivotTable.setPivotTableStyleType(int)` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `pivotTable.setPivotTableStyleName(String)` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten ändern möchten, die über das hinausgehen, was die Voreinstellungen bieten.

Darüber hinaus ist `pivotTable.formatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und dabei überschreibt, was auch immer über eine der oben genannten Stilnamen-APIs festgelegt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**

Die Methode `setAutoFormatType` für eine Pivot-Tabelle akzeptiert einen Wert aus der Enumeration `com.aspose.cells.pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `REPORT_1` bis `REPORT_10`, `CLASSIC` und `TABLE_1` bis `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` wird nur berücksichtigt, wenn die Arbeitsmappe als `.xls` gespeichert wird. Wenn dieselbe Arbeitsmappe als `.xlsx`, `.xlsm` oder `.xlsb` gespeichert wird, ignoriert Excel diese Einstellung und greift auf die Einstellungen `setPivotTableStyleType` und `setPivotTableStyleName` zurück.

{{% /alert %}}

Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.REPORT_5` an und speichert das Ergebnis als `.xls`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Szenario 1: Anwendung eines Legacy-XLS-Voreinstellungs-Autoformats
# Verwendete API: PivotTable.AutoFormatType
# Zieldateiformat: .xls (Legacy)
# Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Eine neue Arbeitsmappe erstellen
workbook = Workbook()

# Das erste Arbeitsblatt abrufen
sheet = workbook.getWorksheets().get(0)

# Quelldaten mit Kopfzeile (Fruit, Year, Amount) befüllen
# und 9 Datenzeilen mit Trauben, Blaubeeren, Kiwi, Kirsche über 2020 und 2021
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

# Eine Pivot-Tabelle in der Zielzelle E3 hinzufügen, benannt als "Pivot1", unter Verwendung des Quellbereichs A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Felder zuweisen: Fruit -> Zeilen, Year -> Spalten, Amount -> Daten
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Das Legacy-XLS-Voreinstellungs-Autoformat "Report5" anwenden
# Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls von Bedeutung.
# Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
# und verwendet das, was PivotTableStyleType / PivotTableStyleName angibt.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Die Arbeitsmappe im Legacy-.xls-Format speichern
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungsstils**

Die Methode `setPivotTableStyleType` für eine Pivot-Tabelle akzeptiert einen Wert aus der Enumeration `com.aspose.cells.PivotTableStyleType`. Die Enumeration umfasst die hellen Designs `PIVOT_TABLE_STYLE_LIGHT_1` bis `PIVOT_TABLE_STYLE_LIGHT_28` und die dunklen Designs `PIVOT_TABLE_STYLE_DARK_1` bis `PIVOT_TABLE_STYLE_DARK_28`. Die in Excel 2017 hinzugefügten Stile (die zweite Welle der hellen und dunklen Designs) sind über dieselbe Enumeration erreichbar.

Dies ist die empfohlene API für jedes moderne Dateiformat. Im Gegensatz zum Legacy-Autoformat wird der hier ausgewählte Stil von Excel originalgetreu wiedergegeben und übersteht Round-Trips durch andere Office-Tools.

Das folgende Beispiel verwendet die gleichen Fruit/Year/Amount-Daten, erstellt eine identische Pivot-Tabelle, wendet `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` an und speichert die Arbeitsmappe als `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Szenario 2: Einen modernen benannten voreingestellten Stil aus Excel 2007+ mit PivotTableStyleType anwenden.
# Zieldateiformat: .xlsx. Die Enumeration PivotTableStyleType befindet sich im Namespace Aspose.Cells
# (nicht in Aspose.Cells.Pivot) – deshalb benötigen wir kein zusätzliches Using dafür.
# GitHub-Referenz: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Kopfzeile: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 Datenzeilen mit Fruit / Year / Amount
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

# Eine Pivot-Tabelle bei E3 mit dem Namen "Pivot1" hinzufügen, basierend auf A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Einen modernen benannten voreingestellten Pivot-Stil aus Excel 2007+ anwenden.
# PivotTableStyleType ist die korrekte API für .xlsx- / .xlsm- / .xlsb-Dateien; AutoFormatType
# wird von Excel für diese Formate ignoriert. PivotTableStyleDark1 gehört zur Familie der dunklen Designs
# (PivotTableStyleDark1..PivotTableStyleDark28), und dieselbe Enumeration stellt auch die neueren
# hellen/dunklen Designs aus Excel 2017 bereit (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Als modernes .xlsx speichern – dieses Format ist dasjenige, für das PivotTableStyleType Bedeutung hat.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellen-Stils**

Die integrierten Voreinstellungen können nicht geändert werden. Wann immer Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:

1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe über `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WHOLE_TABLE` oder `GRAND_TOTAL_ROW`) über `tableStyle.getTableStyleElements().add(TableStyleElementType)` hinzufügen und dann jedem Element über `tableStyleElement.setElementStyle(Style)` einen `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `pivotTable.setPivotTableStyleName(String)` mit dem Namen des Stils aufrufen. Verwenden Sie hier nicht `setPivotTableStyleType`, da diese Methode integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}

`setPivotTableStyleName` und `setPivotTableStyleType` sind nicht austauschbar. Verwenden Sie `setPivotTableStyleType` für integrierte Voreinstellungen und `setPivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Beides festzulegen ist harmlos, aber nur das, was zur beabsichtigten Quelle passt, wird gerendert.

{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` und `PAGE_FIELD_VALUES`.

Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WHOLE_TABLE` und einer fett formatierten roten Schriftart auf `GRAND_TOTAL_ROW`, wendet ihn dann über `setPivotTableStyleName` an und speichert als `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

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

# Add pivot table sourced from A1:C10, anchored at E3, named "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

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
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Step 3: add a GrandTotalRow element and apply bold red font
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Anwenden eines Stils auf jede Pivot-Zelle mit FormatAll**

`pivotTable.formatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Was auch immer zuvor über `setPivotTableStyleType` oder `setPivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}

`formatAll` überschreibt sowohl `setPivotTableStyleType` als auch `setPivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.

{{% /alert %}}

Das folgende Beispiel erstellt einen `Style` mit gelber Vollfüllung, fett formatierter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn dann mit `formatAll` an und speichert als `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Scenario 4: Apply a single Style to every pivot table cell using FormatAll
# API in use: PivotTable.FormatAll(Style)
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

# Add pivot table: source range A1:C10, destination cell E3, name "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Build a Style that will be forced onto every cell of the pivot table
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Apply FormatAll: forces this single style onto every cell of the pivot table,
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
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `pivotTable.setPivotTableStyleType(int)` | Werte aus `com.aspose.cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfigurieren Sie über `tableStyleElement.setElementStyle(Style)`. |
| Beliebiges Format (einheitliche Überschreibung) | `pivotTable.formatAll(Style)` | Verknüpfung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |

Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `setPivotTableStyleType` für integrierte Designs oder `setPivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="python" >}}