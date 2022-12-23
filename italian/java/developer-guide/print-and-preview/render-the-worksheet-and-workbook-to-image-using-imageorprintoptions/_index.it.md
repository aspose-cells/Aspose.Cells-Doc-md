---
title: Eseguire il rendering del foglio di lavoro e della cartella di lavoro in immagine utilizzando ImageOrPrintOptions
type: docs
weight: 220
url: /it/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Questo documento è progettato per fornire una comprensione dettagliata di come convertire un foglio di lavoro o una cartella di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, opzioni come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

## **Panoramica**

volte, potresti dover presentare i tuoi fogli di lavoro come una rappresentazione pittorica. Devi presentare le immagini del foglio di lavoro nelle tue applicazioni o pagine web. Potrebbe essere necessario inserire le immagini in un documento Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. Semplicemente vuoi un foglio di lavoro reso come immagine in modo da poterlo usare altrove. Aspose.Cells supporta la conversione di fogli di lavoro in file Excel in immagini. Inoltre, Aspose.Cells supporta l'impostazione di diverse opzioni come il formato dell'immagine, la risoluzione (sia verticale che orizzontale), la qualità dell'immagine e altre opzioni di immagine e stampa.

Lo API fornisce diverse classi preziose, ad esempio,[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Workbook Render**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), eccetera.

 Il[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class gestisce l'attività di rendering delle immagini per il foglio di lavoro mentre la classe[**Workbook Render**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)fa lo stesso per una cartella di lavoro. Entrambe le suddette classi hanno diverse versioni sovraccaricate di*immaginare*metodo che può convertire direttamente un foglio di lavoro o una cartella di lavoro in file immagine specificati con gli attributi o le opzioni desiderati. È possibile salvare il file immagine sul disco/stream. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIFF, JPEG, TIFF, EMF e così via.

### **Converti foglio di lavoro in immagine**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Opzioni di conversione**

È possibile salvare pagine specifiche nell'immagine. Il codice seguente converte il primo e il secondo foglio di lavoro in una cartella di lavoro in immagini JPG.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Oppure puoi scorrere la cartella di lavoro e rendere ogni foglio di lavoro in essa contenuto in un'immagine separata:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Converti cartella di lavoro in immagine:**

 Per eseguire il rendering della cartella di lavoro completa in formato immagine, è possibile utilizzare l'approccio sopra o semplicemente utilizzare il file[**Workbook Render**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) classe che accetta un'istanza di[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) così come l'oggetto di[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

 Il[**Workbook Render**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) class può salvare la cartella di lavoro solo nel formato TIFF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## articoli Correlati

- [Conversione del foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/)
- [Esporta grafico a SVG con l'attributo viewBox](/cells/it/java/export-chart-to-svg-with-viewbox-attribute/)
- [Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Conversione del foglio di lavoro in immagine e del foglio di lavoro in immagine per pagina](/cells/it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
