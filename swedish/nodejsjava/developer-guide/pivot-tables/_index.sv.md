---
title: Infoga pivottabell
description: Skapa och formatera pivottabeller i Excel-kalkylblad med Aspose.Cells för Node.js via Java.
linktitle: Pivottabeller
url: /sv/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: pivottabell, infoga pivottabell, formatera pivottabell, Aspose.Cells för Node.js via Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Skapa pivottabell**
Det är möjligt att använda Aspose.Cells för att lägga till pivottabeller i kalkylblad programmatiskt.

### **Pivottabellens objektmodell**
Aspose.Cells tillhandahåller en uppsättning klasser som används för att skapa och styra pivottabeller. Byggstenarna är:
- `PivotField` representerar ett fält i en `PivotTable`.
- `PivotFieldCollection` representerar en samling av alla `PivotField`-objekt i `PivotTable`.
- `PivotTable` representerar en pivottabell i ett kalkylblad.
- `PivotTableCollection` representerar en samling av alla `PivotTable`-objekt i ett kalkylblad.

### **Skapa en enkel pivottabell med Aspose.Cells**
1. Lägg till data i ett kalkylblad med hjälp av cellens `putValue`-metod. Denna data kommer att användas som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa `add`-metoden i `PivotTables`-samlingen, som är inkapslad i kalkylbladsobjektet.
3. Få åtkomst till det nya `PivotTable`-objektet från `PivotTables`-samlingen genom att skicka pivottabellens index.
4. Använd valfritt av de `PivotTable`-objekt (som förklaras ovan) för att hantera pivottabellen.

Efter att ha kört exempelkoden läggs en pivottabell till i kalkylbladet.

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
När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra hörnet. Till exempel är "A1:C3" giltigt men "C3:A1" är det inte.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/sv/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/sv/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/sv/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}