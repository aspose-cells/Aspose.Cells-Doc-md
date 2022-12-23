---
title: Conversione del foglio di lavoro in diversi formati di immagine
type: docs
weight: 30
url: /it/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in diversi formati.

{{% /alert %}}

## **Conversione del foglio di lavoro in immagine**

A volte, è utile salvare un'immagine di un foglio di lavoro. Le immagini possono essere condivise online, inserite in altri documenti (report scritti in Word Microsoft, ad esempio, o presentazioni PowerPoint).

Aspose.Cells fornisce l'esportazione di immagini tramite il file**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** classe. Questa classe rappresenta il foglio di lavoro di cui verrà eseguito il rendering in un'immagine. Il**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** la classe fornisce il**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**metodo per convertire un foglio di lavoro in un file immagine. Sono supportati i formati BMP, PNG, JPEG, TIFF e EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java supporta anche la conversione nel formato TIFF. Per convertire un foglio di lavoro in un'immagine TIFF, aggiungi la libreria JAI al tuo classpath.

{{% /alert %}} {{% alert color="primary" %}}

Al momento, il foglio di lavoro di conversione nell'immagine API non supporta i grafici a bolle 3D.

{{% /alert %}}

Il codice seguente mostra come convertire un foglio di lavoro in un file Excel Microsoft in un file PNG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Conversione del foglio di lavoro in SVG**

 SVG sta per**Grafica vettoriale scalabile**SVG è una specifica basata sugli standard XML per la grafica vettoriale bidimensionale. È uno standard aperto che è stato sviluppato dal World Wide Web Consortium (W3C) dal 1999.

 Dal rilascio della v7.1.0,**Aspose.Cells for Java** può convertire i fogli di lavoro in SVG immagini.

Per utilizzare questa funzione, devi importare lo spazio dei nomi com.aspose.cells nel tuo programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio,**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[Rendering cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, e altri.

Il**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class specifica che il foglio di lavoro verrà salvato nel formato SVG.

Il**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**la classe prende l'oggetto di**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** come parametro che imposta il formato di salvataggio sul formato SVG.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file Excel in un file immagine SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Renderizza il foglio di lavoro attivo in una cartella di lavoro**

Un modo semplice per convertire il foglio di lavoro attivo in una cartella di lavoro consiste nell'impostare l'indice del foglio attivo e quindi salvare la cartella di lavoro come SVG. Verificherà il foglio attivo su SVG. Il seguente codice di esempio dimostra questa funzione:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## articoli Correlati

- [Esporta grafico a SVG con l'attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
- [Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversione del foglio di lavoro in immagine e del foglio di lavoro in immagine per pagina](/cells/it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
