---
title: Inserire lo slicer
linktitle: Slicer
type: docs
weight: 170
url: /it/nodejs-cpp/create-slicer/
description: Gestisci gli slicer dei file Excel con Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Uno slicer viene utilizzato per filtrare rapidamente i dati. Può essere utilizzato per filtrare i dati sia in una tabella che in una tabella pivot. Microsoft Excel ti permette di creare uno slicer selezionando una tabella o una tabella pivot e cliccando su *Inserisci > Slicer*. Aspose.Cells for Node.js via C++ permette anche di creare uno slicer usando il metodo [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-).

## **Creare un selettore per una tabella pivot**

Vedi il seguente esempio di codice. Carica il [file Excel di esempio](67338470.xlsx) che contiene la tabella pivot. Successivamente crea lo slicer basato sul primo campo pivot di base. Infine, salva il workbook in formato [output XLSX](67338471.xlsx) e [output XLSB](67338472.xlsb). Lo screenshot seguente mostra lo slicer creato da Aspose.Cells for Node.js via C++ nel file Excel di output.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Creare un selettore per tabella di Excel**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](sampleCreateSlicerToExcelTable.xlsx) che contiene una tabella. Crea quindi lo slicer in base alla prima colonna. Infine, salva il libro di lavoro nel formato [XLSX di output](outputCreateSlicerToExcelTable.xlsx).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
