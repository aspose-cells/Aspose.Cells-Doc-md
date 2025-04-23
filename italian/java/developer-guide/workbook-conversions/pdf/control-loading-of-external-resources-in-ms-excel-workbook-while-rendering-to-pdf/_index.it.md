---
title: Controlla il caricamento di Risorse Esterne nel Lavoro MS Excel mentre viene convertito in PDF
type: docs
weight: 40
url: /it/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Possibili Scenari di Utilizzo**

Il tuo file Excel può contenere risorse esterne come ad esempio immagini o oggetti collegati. Quando converti il tuo file Excel in PDF, Aspose.Cells recupera queste risorse esterne e le renderizza in PDF. Ma a volte, non vuoi caricare queste risorse esterne e, ancor di più, vuoi manipolarle. Puoi farlo usando [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) che implementa l'interfaccia [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider).

## **Controlla il caricamento di Risorse Esterne nel Lavoro MS Excel mentre viene convertito in PDF**

Il seguente esempio di codice spiega come fare uso di [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) per controllare il caricamento delle risorse esterne e manipolarle. Si prega di controllare il [file di Excel di esempio](50528353.xlsx) utilizzato all'interno del codice e il [file PDF di output](50528354.pdf) generato dal codice. La [schermata](50528357.png) mostra come la [vecchia immagine esterna](50528356.png) nel file di Excel di esempio sia stata sostituita con una [nuova immagine](50528355.png) nel file PDF di output.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
