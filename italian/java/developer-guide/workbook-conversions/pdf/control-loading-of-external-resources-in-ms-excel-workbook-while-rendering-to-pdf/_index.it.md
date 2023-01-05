---
title: Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering su PDF
type: docs
weight: 40
url: /it/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Possibili scenari di utilizzo**

Il file Excel può contenere risorse esterne, ad esempio immagini o oggetti collegati. Quando converti il tuo file Excel in PDF, Aspose.Cells recupera queste risorse esterne e le rende in PDF. Ma a volte, non vuoi caricare queste risorse esterne e più di questo, vuoi manipolarle. Puoi farlo usando[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)che implementa il[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaccia.

## **Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering su PDF**

Il seguente codice di esempio spiega come utilizzare[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)per controllare il caricamento di risorse esterne e manipolarle. Si prega di controllare[esempio di file Excel](50528353.xlsx)utilizzato all'interno del codice e il[uscita PDF](50528354.pdf)generato dal codice. Il[immagine dello schermo](50528357.png)mostra come il[vecchia immagine esterna](50528356.png)nel file Excel di esempio è stato sostituito con a[nuova immagine](50528355.png)in uscita PDF.

![cose da fare:immagine_alt_testo](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
