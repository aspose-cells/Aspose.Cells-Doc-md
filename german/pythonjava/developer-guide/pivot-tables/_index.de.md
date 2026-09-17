---
title: Pivot Tabellen
description: Erstellen und Formatieren von Pivot Tabellen in Excel Tabellendateien.
linktitle: Pivot Tabellen
url: /de/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Pivot Tabelle erstellen, Pivot Tabelle einfügen, Pivot Tabelle formatieren.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Pivot-Tabelle erstellen**
Mit Aspose.Cells können Sie Pivot-Tabellen programmgesteuert zu Tabellen hinzufügen.

### **Objektmodell der Pivot-Tabelle**
Aspose.Cells stellt eine Reihe von Klassen bereit, mit denen Pivot-Tabellen erstellt und gesteuert werden. Die Bausteine sind:
- `PivotField` stellt ein Feld in einer `PivotTable` dar.
- `PivotFieldCollection` stellt eine Sammlung aller `PivotField`-Objekte in der `PivotTable` dar.
- `PivotTable` stellt eine Pivot-Tabelle auf einem Arbeitsblatt dar.
- `PivotTableCollection` stellt eine Sammlung aller `PivotTable`-Objekte auf einem Arbeitsblatt dar.

### **Erstellen einer einfachen Pivot-Tabelle mit Aspose.Cells**
1. Fügen Sie Daten mit der Methode `putValue` der Zelle zu einem Arbeitsblatt hinzu. Diese Daten werden als Datenquelle für die Pivot-Tabelle verwendet.
2. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die `add`-Methode der im Arbeitsblattobjekt gekapselten `PivotTables`-Sammlung aufrufen.
3. Greifen Sie auf das neue `PivotTable`-Objekt aus der `PivotTables`-Sammlung zu, indem Sie den Index der Pivot-Tabelle übergeben.
4. Verwenden Sie eines der oben erläuterten `PivotTable`-Objekte, um die Pivot-Tabelle zu verwalten.

Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle hinzugefügt.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Wenn Sie einen Zellbereich als Datenquelle zuweisen, muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" nicht.
{{% /alert %}}

## Verwandte Artikel
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/de/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/de/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/de/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/de/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/de/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}