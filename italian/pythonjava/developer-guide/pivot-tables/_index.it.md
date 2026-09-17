---
title: Tabelle Pivot
description: Creare e formattare tabelle pivot di file di fogli di calcolo di Excel.
linktitle: Tabelle Pivot
url: /it/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Creare Tabella Pivot, Inserire Tabella Pivot, Formattare Tabella Pivot.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Creare una tabella pivot**
È possibile utilizzare Aspose.Cells per aggiungere tabelle pivot ai fogli di calcolo a livello di codice.

### **Modello a oggetti della tabella pivot**
Aspose.Cells fornisce un insieme di classi utilizzate per creare e controllare le tabelle pivot. Gli elementi costitutivi sono:
- `PivotField` rappresenta un campo in una `PivotTable`.
- `PivotFieldCollection` rappresenta una raccolta di tutti gli oggetti `PivotField` nella `PivotTable`.
- `PivotTable` rappresenta una tabella pivot in un foglio di lavoro.
- `PivotTableCollection` rappresenta una raccolta di tutti gli oggetti `PivotTable` in un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
1. Aggiungere dati a un foglio di lavoro utilizzando il metodo `putValue` della cella. Questi dati verranno utilizzati come origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo `add` della raccolta `PivotTables`, incapsulata nell'oggetto foglio di lavoro.
3. Accedere al nuovo oggetto `PivotTable` dalla raccolta `PivotTables` passando l'indice della tabella pivot.
4. Utilizzare uno qualsiasi degli oggetti `PivotTable` (illustrati sopra) per gestire la tabella pivot.

Dopo l'esecuzione del codice di esempio, una tabella pivot viene aggiunta al foglio di lavoro.

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
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.
{{% /alert %}}

## Articoli correlati
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/it/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/it/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/it/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}