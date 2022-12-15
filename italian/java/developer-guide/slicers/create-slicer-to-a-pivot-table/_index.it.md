---
title: Crea Slicer in una tabella pivot
type: docs
weight: 10
url: /it/java/create-slicer-to-a-pivot-table/
---
## **Possibili scenari di utilizzo**
L'affettatrice viene utilizzata per filtrare rapidamente i dati. Può essere utilizzato per filtrare i dati sia in una tabella che in una tabella pivot. Microsoft Excel consente di creare un'affettatrice selezionando una tabella o una tabella pivot e quindi facendo clic su*Inserisci > Affettatrice*. Aspose.Cells permette anche di creare affettatrici utilizzando il[Foglio di lavoro.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)) metodo.
## **Crea Slicer in una tabella pivot**
Vedere il seguente codice di esempio. Carica il[esempio di file Excel](67338498.xlsx)che contiene la tabella pivot. Quindi crea l'affettatrice in base al primo campo pivot di base. Infine, salva la cartella di lavoro in[uscita XLSX](67338497.xlsx)e[uscita XLSB](67338496.xlsb)formato. Lo screenshot seguente mostra l'affettatrice creata da Aspose.Cells nel file Excel di output.

![cose da fare:immagine_alt_testo](create-slicer-to-a-pivot-table_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
