---
title: PivotTables
linktitle: PivotTables
description: Erstellen und formatieren Sie PivotTables mit Aspose.Cells for Python via Java.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Bericht mit Zusammenfassungen: Sie verdichtet einen großen Block roher, zeilenweise angeordneter Daten zu einer kompakten Matrix, ohne dass eine einzige Formel erforderlich ist. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen und welche zu Werten aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Gesamtumsatz je Produkt, Region oder Quartal anstelle langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten machen aus einer flachen Liste einen Kreuzbericht, in dem Trends auf einen Blick erkennbar sind.
- **Details anzeigen** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen zu prüfen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, reicht eine einzige Aktualisierung aus, um den gesamten Bericht neu zu berechnen.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Ausgabenaufschlüsselungen und Bestandsanalysen – also Fragen der Form „Wie schlüsseln sich diese Zahlen nach Kategorie und Zeit auf?“ Aspose.Cells for Python via Java erstellt dieselben PivotTables programmatisch, sodass die von Ihrer Anwendung generierten Arbeitsmappen vorgefertigte Berichte statt ausschließlich Rohdaten enthalten können.

### **Objektmodell der PivotTable**
Aspose.Cells stellt eine Reihe von Klassen bereit, mit denen PivotTables erstellt und gesteuert werden. Die Grundbausteine sind:
- `PivotField` stellt ein Feld in einer `PivotTable` dar.
- `PivotFieldCollection` stellt eine Auflistung aller `PivotField`-Objekte in der `PivotTable` dar.
- `PivotTable` stellt eine PivotTable auf einem Arbeitsblatt dar.
- `PivotTableCollection` stellt eine Auflistung aller `PivotTable`-Objekte auf einem Arbeitsblatt dar.

### **Erstellen einer einfachen PivotTable mit Aspose.Cells**
Das Erstellen einer PivotTable ist ein dreischrittiger Vorgang: Schreiben Sie die Quelldaten in Zellen eines Arbeitsblatts, fügen Sie die PivotTable an der Zielposition ein und ordnen Sie die Felder den Zeilen-, Spalten- und Datenbereichen zu.
1. Fügen Sie Daten mithilfe der Methode `putValue` in die Zellen eines Arbeitsblatts ein. Diese Daten dienen als Datenquelle der PivotTable.
2. Fügen Sie dem Arbeitsblatt eine PivotTable hinzu, indem Sie die Methode `add` der Auflistung `PivotTables` aufrufen: `add(sourceData, row, column)`. `sourceData` ist der Quellbereich (z. B. "A1:C8"); `row` und `column` sind die nullbasierten Koordinaten der Zielzelle für die linke obere Ecke der PivotTable (Zelle E3 bedeutet Zeile 2, Spalte 4). Die Methode gibt direkt das neue Objekt `PivotTable` zurück.
3. Ordnen Sie die Felder mithilfe der Methode `addFieldToArea` des Objekts `PivotTable` zu: Ein Feldname wird dem Zeilenbereich (`PivotFieldType.ROW`), dem Spaltenbereich (`PivotFieldType.COLUMN`) oder dem Datenbereich (`PivotFieldType.DATA`) zugewiesen.
4. Speichern Sie die Arbeitsmappe – die PivotTable wird in die gespeicherte Datei geschrieben.
Nach Ausführung des Beispielcodes wird dem Arbeitsblatt eine PivotTable hinzugefügt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Erstellen Sie eine neue Arbeitsmappe und rufen Sie das erste Arbeitsblatt ab
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Schreiben Sie die Quelldaten: Umsätze pro Sportart und Quartal
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Fügen Sie am Zielzelle E3 eine Pivot-Tabelle hinzu, die aus A1:C8 stammt
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Weisen Sie die Pivot-Felder zu: Sport zu Zeilen, Quarter zu Spalten, Sales zu Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Speichern Sie die Arbeitsmappe
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Wenn Sie einen Zellbereich als Datenquelle festlegen, muss dieser von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, "C3:A1" jedoch nicht.
{{% /alert %}}

## Verwandte Artikel
- [Filterfelder zu einer PivotTable in Aspose.Cells for Python via Java hinzufügen](/cells/de/python-java/add-page-field-in-pivot-table/)
- [Stile auf PivotTables in Aspose.Cells for Python via Java anwenden](/cells/de/python-java/apply-style-to-pivot-table/)
- [Layout des Seitenfelds in einer PivotTable ändern](/cells/de/python-java/change-page-field-layout/)
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Wertfelder von PivotTables in Aspose.Cells for Python via Java verwalten](/cells/de/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}