---
title: Stile auf Pivot-Tabellen in Aspose.Cells for Python via .NET anwenden
linktitle: Stile auf Pivot-Tabellen
description: Erfahren Sie, wie Sie integrierte und benutzerdefinierte Stile auf Pivot-Tabellen in Aspose.Cells for Python via .NET anwenden, einschließlich Legacy-XLS-Autoformaten, moderner benannter Stile ab Excel 2007, benutzerdefinierter Pivot-Tabellen-Stile und der FormatAll-Verknüpfung.
keywords: Aspose.Cells Python via .NET Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt sowohl die Anwendung von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellen-Stilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, und nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden; in diesem Fall kommt die moderne Stil-API zum Einsatz, nicht die Legacy-Version.
- `PivotTable.pivot_table_style_type` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.pivot_table_style_name` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `workbook.worksheets.table_styles.add_pivot_table_style(...)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten ändern möchten, die über die Voreinstellungen hinausgehen.
Darüber hinaus ist `PivotTable.format_all(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alle Einstellungen überschreibt, die über eine der beiden oben genannten Stilnamen-APIs vorgenommen wurden. Dies ist nützlich, wenn unabhängig vom zugrunde liegenden Design ein einheitliches Erscheinungsbild gewünscht ist.

## **Eine Legacy-XLS-Voreinstellung als Autoformat anwenden**
`PivotTable.auto_format_type` akzeptiert einen Wert aus der Aufzählung `aspose.cells.pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `REPORT_1` bis `REPORT_10`, `CLASSIC` und `TABLE_1` bis `TABLE_10`.
Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Beispieldaten „Fruit/Year/Amount", fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.REPORT_5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Die Autoformate der Report-Reihe (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** entworfen, die nur Zeilenfelder und Werte enthalten; sie verfügen über keine eingebaute Formatierung für Spaltenfeld-Kopfzeilen. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout moderner Excel-Versionen ausgelegt sind.
{{% /alert %}}

```python
import aspose.cells as ac
# Szenario 1: Wenden Sie ein voreingestelltes Legacy-XLS-Autoformat an
# Verwendete API: PivotTable.AutoFormatType
# Zieldateiformat: .xls (Legacy)
# Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Erstellen Sie eine neue Arbeitsmappe
workbook = ac.Workbook()
# Holen Sie sich das erste Arbeitsblatt
sheet = workbook.worksheets[0]
# Befüllen Sie die Quelldaten mit einer Kopfzeile (Frucht, Jahr, Betrag)
# und 9 Datenzeilen, die Traube, Blaubeere, Kiwi, Kirsche über 2020 und 2021 abdecken
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
# Fügen Sie eine Pivot-Tabelle in der Zielzelle E3 hinzu, benannt als "Pivot1", unter Verwendung des Quellbereichs A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]
# Felder zuweisen: Frucht -> Zeilen, Betrag -> Daten
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Wenden Sie das voreingestellte Legacy-XLS-Autoformat "Report5" an
# Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls aussagekräftig.
# Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
# und verwendet stattdessen das, was PivotTableStyleType / PivotTableStyleName angibt.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5
# Speichern Sie die Arbeitsmappe im Legacy-.xls-Format
workbook.save("output.xls")
```

## **Einen modernen benannten Voreinstellungs-Stil für Pivot-Tabellen anwenden**

## **Einen benutzerdefinierten Pivot-Tabellen-Stil definieren und anwenden**
Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriftarten anpassen müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:
1. Fügen Sie der `table_styles`-Sammlung der Arbeitsmappe über `workbook.worksheets.table_styles.add_pivot_table_style(name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WHOLE_TABLE` oder `GRAND_TOTAL_ROW`) über `table_style.table_style_elements.add(TableStyleElementType)` hinzufügen und jedem Element über `table_style_element.set_element_style(Style)` ein `Style`-Objekt zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.pivot_table_style_name` auf den Namen des Stils festlegen. Verwenden Sie hier nicht `pivot_table_style_type`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`pivot_table_style_name` und `pivot_table_style_type` sind nicht austauschbar. Verwenden Sie `pivot_table_style_type` für integrierte Voreinstellungen und `pivot_table_style_name` für benutzerdefinierte Stile, die Sie über `add_pivot_table_style` definiert haben. Das Setzen beider Werte ist unbedenklich, aber nur derjenige, der der beabsichtigten Quelle entspricht, wird gerendert.
{{% /alert %}}

Die verfügbaren Werte für `TableStyleElementType` umfassen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` und `PAGE_FIELD_VALUES`.
Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen für `WHOLE_TABLE` und einer fett formatierten roten Schriftart für `GRAND_TOTAL_ROW`, wendet ihn anschließend über `pivot_table_style_name` an und speichert als `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Quelldaten befüllen: Kopfzeile + 9 Datenzeilen (A1:C10)
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
# Schritt 1: Einen neuen benutzerdefinierten Pivot-Tabellenstil registrieren und seinen Index erfassen
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
# Schritt 3: Ein GrandTotalRow-Element hinzufügen und fette rote Schrift anwenden
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)
# Schritt 4: Den benutzerdefinierten Stil namentlich anwenden (NICHT über PivotTableStyleType, das für integrierte Voreinstellungen ist)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **Einen Stil mit FormatAll auf jede Pivot-Zelle anwenden**
`PivotTable.format_all(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Gesamtsummen. Alle zuvor über `pivot_table_style_type` oder `pivot_table_style_name` vorgenommenen Einstellungen werden überschrieben.

{{% alert color="primary" %}}
`format_all` überschreibt sowohl `pivot_table_style_type` als auch `pivot_table_style_name`. Verwenden Sie dies nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild in der gesamten Pivot-Tabelle erforderlich ist.
{{% /alert %}}

Das folgende Beispiel erstellt einen `Style` mit gelber Volltonfüllung, einer fett formatierten dunkelblauen Schriftart und dünnen schwarzen Rahmen an allen Seiten, wendet ihn anschließend mit `format_all` an und speichert als `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Szenario 4: Einen einzelnen Stil auf jede Zelle der Pivot-Tabelle anwenden mit FormatAll
# Verwendete API: PivotTable.FormatAll(Style)
# Zielformat: .xlsx
# GitHub-Referenz: siehe Aspose.Cells-for-.NET Repository — Beispiele zur Pivot-Tabellen-Formatierung
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Quelldaten einfügen: Kopfzeile (Zeile 1) + 9 Datenzeilen (Zeilen 2-10)
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
# und überschreibt zuvor gesetzte PivotTableStyleType / PivotTableStyleName-Werte
pivot_table.format_all(style)
# Arbeitsmappe im modernen .xlsx-Format speichern
workbook.save("output.xlsx")
```

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzübersicht.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.auto_format_type` | Werte aus `aspose.cells.pivot.PivotTableAutoFormatType` (z. B. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.pivot_table_style_type` | Werte aus `aspose.cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Verwenden, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `table_style_element.set_element_style(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.format_all(Style)` | Verknüpfung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |
Im Zweifelsfall speichern Sie als `.xlsx` und verwenden `pivot_table_style_type` für integrierte Designs oder `pivot_table_style_name` für benutzerdefinierte Designs.

{{< app/cells/assistant language="python-net" >}}