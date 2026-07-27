---
title: Stile auf PivotTables in Aspose.Cells für .NET anwenden
linktitle: PivotTable-Stile anwenden
description: Erfahren Sie, wie Sie in Aspose.Cells for Python via .NET integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen ab Excel 2007, benutzerdefinierten Pivot-Tabellenstilen und der FormatAll-Kurzanwendung.
keywords: Aspose.Cells Python via .NET Pivot-Tabellenstil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt sowohl die Anwendung von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellenstilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.

{{% /alert %}}

## **Einführung**

Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall gilt die moderne Stil-API anstelle der Legacy-API.

Für Legacy-`.xls`-Ausgaben verwenden Sie die Eigenschaft `PivotTable.auto_format_type` zusammen mit der Enumeration `aspose.cells.pivot.PivotTableAutoFormatType`. Diese API entspricht der Autoformat-Auswahl, die klassisches Excel für Pivot-Tabellen angeboten hat.

Für moderne `.xlsx`-, `.xlsm`- und `.xlsb`-Ausgaben sind zwei Varianten der Stil-API verfügbar:

- `PivotTable.pivot_table_style_type` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.pivot_table_style_name` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `workbook.worksheets.table_styles.add_pivot_table_style(...)` definieren. Benutzerdefinierte Stile sind immer dann erforderlich, wenn Sie Farben, Rahmen oder Schriftarten über das hinaus ändern möchten, was die Voreinstellungen bieten.

Zusätzlich ist `PivotTable.format_all(Style)` eine Kurzanwendung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und dabei überschreibt, was auch immer über eine der oben genannten Stilnamen-APIs gesetzt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrundeliegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**

`PivotTable.auto_format_type` akzeptiert einen Wert aus der Enumeration `aspose.cells.pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `REPORT_1` bis `REPORT_10`, `CLASSIC` und `TABLE_1` bis `TABLE_10`.

{{% alert color="primary" %}}

`auto_format_type` wird nur berücksichtigt, wenn die Arbeitsmappe als `.xls` gespeichert wird. Wenn dieselbe Arbeitsmappe als `.xlsx`, `.xlsm` oder `.xlsb` gespeichert wird, ignoriert Excel diese Eigenschaft und greift auf die Einstellungen `pivot_table_style_type` und `pivot_table_style_name` zurück.

{{% /alert %}}

Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.REPORT_5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}

**Warum keine Spaltenfelder?** Die Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** mit nur Zeilenfeldern und Werten entworfen — sie haben keine integrierte Formatierung für Spaltenfeld-Überschriften. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus Szenario 2 unten, die für das zweidimensionale Layout moderner Excel-Versionen entwickelt wurden.

{{% /alert %}}

```python
import aspose.cells as ac

# Szenario 1: Ein Legacy-XLS-Preset-Autoformat anwenden
# Verwendete API: PivotTable.AutoFormatType
# Zieldateiformat: .xls (Legacy)
# Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Eine neue Arbeitsmappe erstellen
workbook = ac.Workbook()

# Das erste Arbeitsblatt abrufen
sheet = workbook.worksheets[0]

# Quelldaten mit Kopfzeile füllen (Fruit, Year, Amount)
# und 9 Datenzeilen mit grape, blueberry, kiwi, cherry über 2020 und 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")

sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)

sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)

sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)

sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)

sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)

sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)

sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)

sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)

sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)

# Eine Pivot-Tabelle in der Zielzelle E3 mit dem Namen "Pivot1" unter Verwendung des Quellbereichs A1:C10 hinzufügen
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Felder zuweisen: Fruit -> Zeilen, Year -> Spalten, Amount -> Daten
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Das Legacy-XLS-Preset-Autoformat "Report5" anwenden
# Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls relevant.
# Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
# und verwendet das, was PivotTableStyleType / PivotTableStyleName angibt.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Die Arbeitsmappe im Legacy-.xls-Format speichern
workbook.save("output.xls")
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungsstils**

`PivotTable.pivot_table_style_type` akzeptiert einen Wert aus der Enumeration `aspose.cells.PivotTableStyleType`. Die Enumeration umfasst helle Designs `PIVOT_TABLE_STYLE_LIGHT_1` bis `PIVOT_TABLE_STYLE_LIGHT_28` und dunkle Designs `PIVOT_TABLE_STYLE_DARK_1` bis `PIVOT_TABLE_STYLE_DARK_28`. Die in Excel 2017 hinzugefügten Stile (die zweite Welle der hellen und dunklen Designs) sind über dieselbe Enumeration erreichbar.

Dies ist die empfohlene API für jedes moderne Dateiformat. Im Gegensatz zum Legacy-Autoformat wird der hier ausgewählte Stil von Excel originalgetreu wiedergegeben und übersteht Roundtrips durch andere Office-Tools.

Das folgende Beispiel verwendet dieselben Fruit/Year/Amount-Daten, erstellt eine identische Pivot-Tabelle, wendet `PIVOT_TABLE_STYLE_DARK_1` an und speichert die Arbeitsmappe als `.xlsx`.

```python
import aspose.cells as ac

# Szenario 2: Einen modernen benannten Excel 2007+ Vorlagenstil mit PivotTableStyleType anwenden.
# Zieldateiformat: .xlsx. Die PivotTableStyleType-Enum befindet sich im Aspose.Cells-Namespace
# (nicht in Aspose.Cells.Pivot) — deshalb benötigen wir kein zusätzliches using dafür.
# GitHub-Referenz: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Kopfzeile: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 Datenzeilen mit Fruit / Year / Amount
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Eine Pivot-Tabelle bei E3 mit dem Namen "Pivot1" hinzufügen, bezogen aus A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Einen modernen benannten Excel 2007+ Pivot-Vorlagenstil anwenden.
# PivotTableStyleType ist die korrekte API für .xlsx / .xlsm / .xlsb Dateien; AutoFormatType
# wird von Excel für diese Formate ignoriert. PivotTableStyleDark1 gehört zur Dunkel-Themen
# Familie (PivotTableStyleDark1..PivotTableStyleDark28), und dieselbe Enum stellt auch die
# neueren Excel 2017 Hell/Dunkel-Themen bereit (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Als modernes .xlsx speichern — dies ist das Format, für das PivotTableStyleType relevant ist.
workbook.save("output.xlsx")
```

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellenstils**

Die integrierten Voreinstellungen können nicht geändert werden. Wann immer Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:

1. Fügen Sie der `table_styles`-Sammlung der Arbeitsmappe über `workbook.worksheets.table_styles.add_pivot_table_style(name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WHOLE_TABLE` oder `GRAND_TOTAL_ROW`) über `table_style.table_style_elements.add(TableStyleElementType)` hinzufügen und dann jedem Element über `table_style_element.set_element_style(Style)` einen `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.pivot_table_style_name` auf den Namen des Stils setzen. Verwenden Sie hier nicht `pivot_table_style_type`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}

`pivot_table_style_name` und `pivot_table_style_type` sind nicht austauschbar. Verwenden Sie `pivot_table_style_type` für integrierte Voreinstellungen und `pivot_table_style_name` für benutzerdefinierte Stile, die Sie über `add_pivot_table_style` definiert haben. Beides zu setzen ist harmlos, aber nur dasjenige, das zur beabsichtigten Quelle passt, wird wiedergegeben.

{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` und `PAGE_FIELD_VALUES`.

Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WHOLE_TABLE` und einer fetten roten Schriftart auf `GRAND_TOTAL_ROW`, wendet ihn dann über `pivot_table_style_name` an und speichert als `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Quellendaten befüllen: Kopfzeile + 9 Datenzeilen (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

# Pivot-Tabelle aus A1:C10 hinzufügen, verankert bei E3, benannt "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Schritt 1: Einen neuen benutzerdefinierten Pivot-Tabellenstil registrieren und dessen Index erfassen
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]

# Schritt 2: Ein WholeTable-Element hinzufügen und dünne schwarze Rahmen auf allen vier Seiten anwenden
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)

# Schritt 3: Ein GrandTotalRow-Element hinzufügen und eine fette rote Schrift anwenden
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)

# Schritt 4: Den benutzerdefinierten Stil nach Namen anwenden (NICHT nach PivotTableStyleType, der für integrierte Voreinstellungen ist)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Anwenden eines Stils auf jede Pivot-Zelle mit FormatAll**

`PivotTable.format_all(Style)` ist eine Kurzanwendung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Was auch immer zuvor über `pivot_table_style_type` oder `pivot_table_style_name` gesetzt wurde, wird überschrieben.

{{% alert color="primary" %}}

`format_all` überschreibt sowohl `pivot_table_style_type` als auch `pivot_table_style_name`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.

{{% /alert %}}

Das folgende Beispiel erstellt einen `Style` mit gelber Vollfüllung, fetter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn dann mit `format_all` an und speichert als `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Szenario 4: Einen einzelnen Stil auf jede Pivot-Tabellen-Zelle mit FormatAll anwenden
# Verwendete API: PivotTable.FormatAll(Style)
# Zielformat: .xlsx
# GitHub-Referenz: siehe Aspose.Cells-for-.NET-Repository — Beispiele zur Pivot-Tabellen-Gestaltung

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Quelldaten befüllen: Kopfzeile (Zeile 1) + 9 Datenzeilen (Zeilen 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)

# Pivot-Tabelle hinzufügen: Quellbereich A1:C10, Zielzelle E3, Name "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Einen Stil erstellen, der auf jede Zelle der Pivot-Tabelle angewendet wird
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black

# FormatAll anwenden: erzwingt diesen einzelnen Stil auf jede Zelle der Pivot-Tabelle,
# wodurch ein zuvor gesetzter PivotTableStyleType / PivotTableStyleName überschrieben wird
pivot_table.format_all(style)

# Die Arbeitsmappe im modernen .xlsx-Format speichern
workbook.save("output.xlsx")
```

## **Welche Stil-API sollte ich verwenden?**

Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.

| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.auto_format_type` | Werte aus `aspose.cells.pivot.PivotTableAutoFormatType` (z. B. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.pivot_table_style_type` | Werte aus `aspose.cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `table_style_element.set_element_style(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.format_all(Style)` | Kurzanwendung, die jede andere Stileinstellung über die gesamte Pivot-Tabelle hinweg überschreibt. |

Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `pivot_table_style_type` für integrierte Designs oder `pivot_table_style_name` für benutzerdefinierte Designs.

{{< app/cells/assistant language="python" >}}