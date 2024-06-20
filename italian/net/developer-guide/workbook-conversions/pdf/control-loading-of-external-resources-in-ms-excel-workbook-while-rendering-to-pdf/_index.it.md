---
title: Controlla il caricamento di Risorse Esterne nel Lavoro MS Excel mentre viene convertito in PDF
type: docs
weight: 40
url: /it/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Possibili Scenari di Utilizzo**

Il tuo file Excel potrebbe contenere risorse esterne come immagini o oggetti collegati. Quando converti il tuo file Excel in PDF, Aspose.Cells recupera queste risorse esterne e le rende in PDF. Ma a volte, non vuoi caricare queste risorse esterne e, inoltre, vuoi manipolarle. Puoi farlo usando [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) che implementa l'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider).

## **Controlla il caricamento di Risorse Esterne nel Lavoro MS Excel mentre viene convertito in PDF**

Il codice di esempio seguente spiega come utilizzare [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) per controllare il caricamento di risorse esterne e manipolarle. Si prega di controllare il [file Excel di esempio](50528322.xlsx) utilizzato all'interno del codice e il [PDF di output](50528325.pdf) generato dal codice. Lo [screenshot](50528326.png) mostra come la [vecchia immagine esterna](50528324.png) nel file Excel di esempio è stata sostituita con una [nuova immagine](50528323.png) nel PDF di output.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
