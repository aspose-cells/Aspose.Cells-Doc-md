---
title: Creare un filtro per una tabella pivot
type: docs
weight: 10
url: /it/java/create-slicer-to-a-pivot-table/
---

## **Possibili Scenari di Utilizzo**
Il slicer viene utilizzato per filtrare i dati rapidamente. Può essere usato per filtrare i dati sia in una tabella che in una tabella pivot. Microsoft Excel permette di creare un slicer selezionando una tabella o una tabella pivot e cliccando su *Inserisci > Slicer*. Anche Aspose.Cells permette di creare uno slicer usando il metodo [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-)
## **Creare un selettore per una tabella pivot**
Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](67338498.xlsx) che contiene la tabella pivot. Quindi crea il slicer in base al primo campo pivot base. Infine, salva il workbook in formato [output XLSX](67338497.xlsx) e [output XLSB](67338496.xlsb). La schermata seguente mostra il slicer creato da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
