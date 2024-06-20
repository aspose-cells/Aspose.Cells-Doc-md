---
title: Creare un filtro per una tabella pivot
type: docs
weight: 10
url: /it/python-java/create-slicer-to-a-pivot-table/
---

## **Possibili Scenari di Utilizzo**
I filtri sono utilizzati per filtrare rapidamente i dati. Possono essere utilizzati per filtrare i dati sia in una tabella che in una tabella pivot. Microsoft Excel consente di creare un filtro selezionando una tabella o una tabella pivot e quindi facendo clic su *Inserisci > Filtro*. Aspose.Cells for Python via Java fornisce il metodo Worksheet.getSlicers().add() per creare un filtro.
## **Creare un selettore per una tabella pivot**
Il seguente frammento di codice carica il [file Excel di esempio](106364966.xlsx) che contiene la tabella pivot. Quindi crea il filtro in base al primo campo pivot di base. Infine, salva il workbook in formato [XLSX di output](106364967.xlsx). La seguente schermata mostra il filtro creato da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
