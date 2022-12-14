---
title: Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering in PDF
type: docs
weight: 40
url: /it/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Possibili scenari di utilizzo**

 Il file Excel può contenere risorse esterne, ad esempio immagini o oggetti collegati. Quando converti il tuo file Excel in PDF, Aspose.Cells recupera queste risorse esterne e le rende in PDF. Ma a volte, non vuoi caricare queste risorse esterne e, soprattutto, vuoi manipolarle. Puoi farlo usando[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)che implementa il[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaccia.

## **Controlla il caricamento delle risorse esterne nella cartella di lavoro MS Excel durante il rendering in PDF**

 Il seguente codice di esempio spiega come utilizzare[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) per controllare il caricamento di risorse esterne e manipolarle. Si prega di controllare[esempio di file Excel](50528322.xlsx) utilizzato all'interno del codice e il[uscita PDF](50528325.pdf)generato dal codice. Il[immagine dello schermo](50528326.png) mostra come il[vecchia immagine esterna](50528324.png) nel file Excel di esempio è stato sostituito con a[nuova immagine](50528323.png) nel PDF di output.

![cose da fare:immagine_alt_testo](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
