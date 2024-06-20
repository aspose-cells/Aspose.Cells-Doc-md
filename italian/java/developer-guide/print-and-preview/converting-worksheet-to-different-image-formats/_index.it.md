---
title: Conversione del foglio di lavoro in diversi formati di immagine
type: docs
weight: 30
url: /it/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in formati diversi.

{{% /alert %}}

## **Conversione del foglio di lavoro in immagine**

A volte è utile salvare un'immagine di un foglio di lavoro. Le immagini possono essere condivise online, inserite in altri documenti (rapporti scritti in Microsoft Word, ad esempio, o presentazioni PowerPoint).

Aspose.Cells fornisce l'esportazione di immagini attraverso la classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). Questa classe rappresenta il foglio di lavoro che verrà reso in un'immagine. La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) fornisce il metodo [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) per convertire un foglio di lavoro in un file immagine. Sono supportati i formati BMP, PNG, JPEG, TIFF e EMF.

{{% alert color="primary" %}}

Aspose.Cells for Java supporta anche la conversione nel formato TIFF. Per convertire un foglio di lavoro in un'immagine TIFF, aggiungere la libreria JAI al proprio classpath.

{{% /alert %}} {{% alert color="primary" %}}

Attualmente, l'API per la conversione del foglio di lavoro in immagine non supporta i grafici a bolle 3D.

{{% /alert %}}

Il codice seguente mostra come convertire un foglio di lavoro in un file PNG in un file Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Conversione del foglio di lavoro in SVG**

SVG sta per **Scalable Vector Graphics**. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Dalla versione v7.1.0, **Aspose.Cells for Java** può convertire i fogli di lavoro in immagini SVG.

Per utilizzare questa funzionalità, è necessario importare lo spazio dei nomi com.aspose.cells nel proprio programma o progetto. Ha diverse classi preziose per il rendering e la stampa, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), e altri.

La classe [**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) specifica che il foglio di lavoro verrà salvato in formato SVG.

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) prende l'oggetto di [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) come parametro che imposta il formato di salvataggio in formato SVG.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine SVG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Renderizza il foglio attivo in un libro di lavoro**

Un modo semplice per convertire il foglio attivo in un libro di lavoro è impostare l'indice del foglio attivo e quindi salvare il libro di lavoro come SVG. Renderizzerà il foglio attivo in SVG. Il codice di esempio seguente dimostra questa funzione:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Articoli correlati

- [Esportare il grafico in SVG con attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Convertire il foglio di lavoro in un'immagine e Foglio di lavoro in un'immagine per pagina](/cells/it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
