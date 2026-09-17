---
title: Pivot tabeller
description: Skapa och formatera pivottabeller i Excel kalkylbladsfiler.
linktitle: Pivot tabeller
url: /sv/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Skapa pivot tabell, Infoga pivot tabell, Formatera pivot tabell.
ai_search_scope: cells_pythonjava
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
När du tilldelar ett cellområde som datakälla måste området gå från övre vänstra till nedre högra hörnet. Till exempel är "A1:C3" giltigt men "C3:A1" är det inte.
{{% /alert %}}

## Relaterade artiklar
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/sv/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/sv/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/sv/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/sv/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/sv/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}