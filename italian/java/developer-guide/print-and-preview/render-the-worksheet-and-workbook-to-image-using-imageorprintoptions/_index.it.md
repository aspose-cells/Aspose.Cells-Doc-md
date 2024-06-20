---
title: Rendere il foglio di lavoro e il workbook come immagine utilizzando ImageOrPrintOptions
type: docs
weight: 220
url: /it/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire un'approfondita comprensione di come convertire un foglio di lavoro o un workbook in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, opzioni come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

## **Panoramica**

A volte potresti aver bisogno di presentare i tuoi fogli di lavoro come rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint, o utilizzarle in qualche altro scenario. Semplicemente desideri un foglio di lavoro rappresentato come un'immagine in modo da poterlo utilizzare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta impostare diverse opzioni come formato immagine, risoluzione (sia verticale che orizzontale), qualità dell'immagine e altre opzioni di immagine e stampa.

L'API fornisce diverse classi preziose, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), ecc.

La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) gestisce il compito di renderizzare le immagini per il foglio di lavoro, mentre la classe [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) fa lo stesso per un workbook. Entrambe le suddette classi hanno diverse versioni sovraccaricate del metodo *toImage* che possono convertire direttamente un foglio di lavoro o un workbook in file di immagine specificati con i tuoi attributi o opzioni desiderati. Puoi salvare il file immagine su disco/stream. Ci sono diversi formati di immagine supportati, ad esempio BMP, PNG, GIFF, JPEG, TIFF, EMF e così via.

### **Convertire foglio di lavoro in immagine**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Opzioni di conversione**

È possibile salvare pagine specifiche in immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in un libro di lavoro in immagini JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Oppure è possibile ciclare attraverso il workbook e renderizzare ogni foglio di lavoro in una immagine separata:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Convertire workbook in immagine:**

Per renderizzare l'intero workbook in formato immagine, è possibile utilizzare l'approccio sopra descritto o semplicemente utilizzare la classe [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) che accetta un'istanza di [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) e l'oggetto di [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

È possibile salvare l'intero workbook in un'unica immagine TIFF con più fotogrammi o pagine:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Articoli correlati

- [Conversione del foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/)
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Convertire il foglio di lavoro in un'immagine e Foglio di lavoro in un'immagine per pagina](/cells/it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
