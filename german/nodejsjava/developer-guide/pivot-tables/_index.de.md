---
title: Pivot-Tabelle einfügen
description: Erstellen und formatieren Sie Pivot-Tabellen in Excel-Tabellen mit Aspose.Cells für Node.js via Java.
linktitle: Pivot-Tabellen
url: /de/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Pivot-Tabelle erstellen, Pivot-Tabelle einfügen, Pivot-Tabelle formatieren, Aspose.Cells für Node.js via Java.
ai_search_scope: cells_nodejsjava
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
2. Fügen Sie eine Pivot-Tabelle zum Arbeitsblatt hinzu, indem Sie die Methode `add` der im Arbeitsblattobjekt gekapselten `PivotTables`-Sammlung aufrufen.
3. Greifen Sie auf das neue `PivotTable`-Objekt aus der `PivotTables`-Sammlung zu, indem Sie den Index der Pivot-Tabelle übergeben.
4. Verwenden Sie eines der oben erläuterten `PivotTable`-Objekte, um die Pivot-Tabelle zu verwalten.

Nach der Ausführung des Beispielcodes wird dem Arbeitsblatt eine Pivot-Tabelle hinzugefügt.

```javascript
var dataDir = "./";

// Instantiating a Workbook object
var workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
var sheet = workbook.getWorksheets().get(0);

var cells = sheet.getCells();

// Setting the value to the cells
var cell = cells.get("A1");
cell.putValue("Sport");
cell = cells.get("B1");
cell.putValue("Quarter");
cell = cells.get("C1");
cell.putValue("Sales");

cell = cells.get("A2");
cell.putValue("Golf");
cell = cells.get("A3");
cell.putValue("Golf");
cell = cells.get("A4");
cell.putValue("Tennis");
cell = cells.get("A5");
cell.putValue("Tennis");
cell = cells.get("A6");
cell.putValue("Tennis");
cell = cells.get("A7");
cell.putValue("Tennis");
cell = cells.get("A8");
cell.putValue("Golf");

cell = cells.get("B2");
cell.putValue("Qtr3");
cell = cells.get("B3");
cell.putValue("Qtr4");
cell = cells.get("B4");
cell.putValue("Qtr3");
cell = cells.get("B5");
cell.putValue("Qtr4");
cell = cells.get("B6");
cell.putValue("Qtr3");
cell = cells.get("B7");
cell.putValue("Qtr4");
cell = cells.get("B8");
cell.putValue("Qtr3");

cell = cells.get("C2");
cell.putValue(1500);
cell = cells.get("C3");
cell.putValue(2000);
cell = cells.get("C4");
cell.putValue(600);
cell = cells.get("C5");
cell.putValue(1500);
cell = cells.get("C6");
cell.putValue(4070);
cell = cells.get("C7");
cell.putValue(5000);
cell = cells.get("C8");
cell.putValue(6430);

var pivotTables = sheet.getPivotTables();

// Adding a PivotTable to the worksheet
var index = pivotTables.add("=A1:C8", "E3", "PivotTable2");

// Accessing the instance of the newly added PivotTable
var pivotTable = pivotTables.get(index);

// Unshowing grand totals for rows.
pivotTable.setRowGrand(false);

// Draging the first field to the row area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);

// Draging the second field to the column area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, 1);

// Draging the third field to the data area.
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 2);

// Saving the Excel file
workbook.save(dataDir + "pivotTable_test_out.xls");
```

{{% alert color="primary" %}}
Wenn Sie einen Zellbereich als Datenquelle zuweisen, muss der Bereich von oben links nach unten rechts verlaufen. Beispielsweise ist "A1:C3" gültig, aber "C3:A1" nicht.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/de/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/de/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}