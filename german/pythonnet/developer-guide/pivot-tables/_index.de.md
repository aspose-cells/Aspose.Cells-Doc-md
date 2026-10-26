---
title: PivotTable einfügen
linktitle: PivotTable einfügen
description: Erstellen und formatieren Sie PivotTables mit Aspose.Cells for Python via .NET.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Zusammenfassungsbericht: Sie verdichtet einen großen Datenblock aus einzelnen Datenzeilen zu einer kompakten Matrix, ohne dass eine einzige Formel erforderlich ist. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen werden und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Gesamtumsatz pro Produkt, Region oder Quartal statt langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten verwandeln eine flache Liste in einen Kreuzbericht, in dem Trends auf einen Blick erkennbar sind.
- **Detaillieren** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen zu prüfen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, berechnet eine Aktualisierung den gesamten Bericht neu.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Ausgabenanalysen und Bestandsanalysen – also Anwendungen, die Fragen wie „Wie lassen sich diese Zahlen nach Kategorie und Zeit aufschlüsseln?“ beantworten. Aspose.Cells for Python via .NET erstellt dieselben PivotTables programmgesteuert, sodass die von Ihrer Anwendung generierten Arbeitsmappen einsatzbereite Berichte statt nur Rohdaten enthalten können.

### **Objektmodell der PivotTable**
Aspose.Cells for Python via .NET stellt einen speziellen Satz an Klassen im [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/)-Namespace bereit, die zum Erstellen und Steuern von PivotTables verwendet werden. Diese Klassen dienen zum Erstellen und Festlegen von [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)-Objekten, die die Bausteine einer PivotTable bilden. Die Objekte sind:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) stellt ein Feld in einer [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) dar.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) stellt eine Sammlung aller [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)-Objekte in der [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) dar.
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) stellt eine PivotTable in einem Arbeitsblatt dar.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) stellt eine Sammlung aller [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)-Objekte in einem Arbeitsblatt dar.

### **Erstellen einer einfachen PivotTable mit Aspose.Cells**
Das Erstellen einer PivotTable umfasst drei Schritte: Schreiben Sie die Quelldaten in Zellen des Arbeitsblatts, fügen Sie die PivotTable an der Zielposition hinzu und ordnen Sie die PivotTable-Felder den Zeilen-, Spalten- und Datenbereichen zu.
1. Fügen Sie einem Arbeitsblatt mithilfe der Methode [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) des Objekts [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) Daten hinzu. Diese Daten dienen als Datenquelle der PivotTable.
2. Fügen Sie dem Arbeitsblatt eine PivotTable hinzu, indem Sie die Methode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) der Sammlung [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) aufrufen: `add(source_data, row, column)`. `source_data` ist der Quellbereich (zum Beispiel "A1:C8"); `row` und `column` sind die nullbasierten Koordinaten der Zielzelle an der linken oberen Ecke der PivotTable (Zelle E3 bedeutet Zeile 2, Spalte 4). Die Methode gibt direkt das neue Objekt [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) zurück.
3. Ordnen Sie die PivotTable-Felder mit der Methode `add_field_to_area` des Objekts [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) zu: Ein Feldname wird dem Zeilenbereich (`PivotFieldType.ROW`), dem Spaltenbereich (`PivotFieldType.COLUMN`) oder dem Datenbereich (`PivotFieldType.DATA`) zugewiesen.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine PivotTable hinzugefügt.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Erstelle eine neue Arbeitsmappe und rufe das erste Arbeitsblatt ab
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Schreibe die Quelldaten: Umsätze pro Sportart und Quartal
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Füge am Zielzelle E3 eine Pivot-Tabelle hinzu, deren Quelle A1:C8 ist
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Weise Pivotfelder zu: Sport zu Zeilen, Quarter zu Spalten, Sales zu Daten
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Speichere die Arbeitsmappe
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Wenn ein Zellenbereich als Datenquelle zugewiesen wird, muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, "C3:A1" jedoch nicht.
{{% /alert %}}

## Verwandte Artikel
- [Filterfelder zu einer PivotTable in Aspose.Cells for Python via .NET hinzufügen](/cells/de/python-net/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for Python via .NET anwenden](/cells/de/python-net/apply-style-to-pivot-table/)
- [Layout des Seitenfelds in einer PivotTable ändern](/cells/de/python-net/change-page-field-layout/)
- [PivotTables nach Beschriftung oder Wert filtern](/cells/de/python-net/filter-by-label-or-value-of-pivot-table/)
- [Wertfelder von PivotTables in Aspose.Cells for Python via .NET verwalten](/cells/de/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}