---
title: Inserisci tabella pivot
description: Crea e formatta tabelle pivot di file di fogli di calcolo Excel utilizzando Aspose.Cells per Node.js via Java.
linktitle: Tabelle pivot
url: /it/nodejs-java/create-pivot-table/
type: docs
weight: 160
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot, Aspose.Cells per Node.js via Java.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Crea tabella pivot**
È possibile utilizzare Aspose.Cells per aggiungere tabelle pivot ai fogli di calcolo a livello di codice.

### **Modello a oggetti della tabella pivot**
Aspose.Cells fornisce un insieme di classi utilizzate per creare e controllare le tabelle pivot. Gli elementi costitutivi sono:
- `PivotField` rappresenta un campo in una `PivotTable`.
- `PivotFieldCollection` rappresenta una raccolta di tutti gli oggetti `PivotField` nella `PivotTable`.
- `PivotTable` rappresenta una tabella pivot su un foglio di lavoro.
- `PivotTableCollection` rappresenta una raccolta di tutti gli oggetti `PivotTable` su un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
1. Aggiungere dati a un foglio di lavoro utilizzando il metodo `putValue` della cella. Questi dati verranno utilizzati come origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo `add` della raccolta `PivotTables`, incapsulato nell'oggetto foglio di lavoro.
3. Accedere al nuovo oggetto `PivotTable` dalla raccolta `PivotTables` passando l'indice della tabella pivot.
4. Utilizzare uno qualsiasi degli oggetti `PivotTable` (illustrati sopra) per gestire la tabella pivot.

Dopo l'esecuzione del codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

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
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.
{{% /alert %}}

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/it/nodejs-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}