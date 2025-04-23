---
title: Inserire lo slicer
linktitle: Slicer
type: docs
weight: 170
url: /it/net/create-slicer/
description: Gestisci gli slicer dei file Excel con Aspose.Cells.
---

## **Possibili Scenari di Utilizzo**

Uno slicer viene utilizzato per filtrare rapidamente i dati. Può essere utilizzato per filtrare i dati sia in una tabella che in una tabella pivot. Microsoft Excel ti consente di creare uno slicer selezionando una tabella o una tabella pivot e quindi facendo clic su *Inserisci > Slicer*. Aspose.Cells ti consente anche di creare uno slicer utilizzando il metodo [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index).

## **Creare un selettore per una tabella pivot**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](67338470.xlsx) che contiene la tabella pivot. Crea quindi lo slicer in base al primo campo pivot di base. Infine, salva il libro di lavoro nel formato [XLSX di output](67338471.xlsx) e [XLSB di output](67338472.xlsb). Nella seguente schermata viene mostrato lo slicer creato da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Creare un selettore per tabella di Excel**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](sampleCreateSlicerToExcelTable.xlsx) che contiene una tabella. Crea quindi lo slicer in base alla prima colonna. Infine, salva il libro di lavoro nel formato [XLSX di output](outputCreateSlicerToExcelTable.xlsx).

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Argomenti avanzati**
- [Modifica le proprietà dello slicer](/cells/it/net/change-slicer-properties/)
- [Disegna lo slicer durante il rendering di Excel in PDF](/cells/it/net/draw-slicer-while-rendering-excel-to-pdf/)
- [Formattazione del selettore](/cells/it/net/formatting-slicer/)
- [Rimozione dello slicer](/cells/it/net/removing-slicer/)
- [Rendering dello slicer](/cells/it/net/rendering-slicer/)
- [Aggiornamento dello slicer](/cells/it/net/updating-slicer/)
{{< app/cells/assistant language="csharp" >}}
