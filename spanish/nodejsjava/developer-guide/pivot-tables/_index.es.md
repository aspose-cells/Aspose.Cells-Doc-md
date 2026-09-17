---
title: Insertar tabla dinámica
description: Cree y dé formato a tablas dinámicas de archivos de hojas de cálculo de Excel con Aspose.Cells para Node.js vía Java.
linktitle: Tablas dinámicas
url: /es/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Crear tabla dinámica, Insertar tabla dinámica, Dar formato a tabla dinámica, Aspose.Cells para Node.js vía Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Crear tabla dinámica**
Es posible usar Aspose.Cells para agregar tablas dinámicas a hojas de cálculo mediante programación.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells proporciona un conjunto de clases que se usan para crear y controlar tablas dinámicas. Los componentes básicos son:
- `PivotField` representa un campo en una `PivotTable`.
- `PivotFieldCollection` representa una colección de todos los objetos `PivotField` en la `PivotTable`.
- `PivotTable` representa una tabla dinámica en una hoja de cálculo.
- `PivotTableCollection` representa una colección de todos los objetos `PivotTable` en una hoja de cálculo.

### **Creación de una tabla dinámica simple con Aspose.Cells**
1. Agregue datos a una hoja de cálculo mediante el método `putValue` de la celda. Estos datos se utilizarán como fuente de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método `add` de la colección `PivotTables`, encapsulada en el objeto hoja de cálculo.
3. Acceda al nuevo objeto `PivotTable` de la colección `PivotTables` pasando el índice de la tabla dinámica.
4. Use cualquiera de los objetos `PivotTable` (explicados anteriormente) para administrar la tabla dinámica.

Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

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
Al asignar un rango de celdas como fuente de datos, el rango debe ir de arriba a la izquierda a abajo a la derecha. Por ejemplo, "A1:C3" es válido pero "C3:A1" no lo es.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/es/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/es/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}