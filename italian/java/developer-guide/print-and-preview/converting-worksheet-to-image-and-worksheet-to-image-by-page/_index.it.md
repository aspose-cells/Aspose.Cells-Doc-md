---
title: Convertire foglio elettronico in immagine e foglio elettronico in immagine per pagina
type: docs
weight: 210
url: /it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio elettronico in un file immagine e un foglio elettronico con pagine multiple in un file immagine per pagina.

A volte potresti aver bisogno di presentare i fogli di lavoro come immagini, ad esempio per utilizzarli in applicazioni o pagine web. Potresti aver bisogno di inserire le immagini in un documento di Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. Semplicemente, desideri rendere il foglio di lavoro come un'immagine. Le API di Aspose.Cells supportano la conversione dei fogli di lavoro nei file Microsoft Excel in immagini. Inoltre, Aspose.Cells supporta la conversione di un libro di lavoro in più file immagine, uno per pagina.

{{% /alert %}}

## **Utilizzare Aspose.Cells per convertire un foglio elettronico in un file immagine**

Questo articolo mostra come utilizzare l'API Aspose.Cells for Java per convertire un foglio di lavoro in un'immagine. L'API fornisce diverse classi preziose, come [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), e così via. La classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) rappresenta un foglio di lavoro per rendere le immagini per il foglio di lavoro ed ha un metodo sovraccaricato [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-) che può convertire direttamente un foglio di lavoro in file immagine con qualsiasi attributo o opzione impostata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Risultato**

Dopo aver eseguito il codice precedente, il foglio di lavoro chiamato Foglio1 viene convertito in un file immagine FoglioImmagine.jpg.

**Il file JPG di output**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Utilizzare Aspose.Cells per convertire il foglio di lavoro in un file immagine per pagina**

Questo esempio mostra come utilizzare Aspose.Cells per convertire un foglio di lavoro da un modello di cartella di lavoro che ha diverse pagine in un file immagine per pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Risultato**

Dopo aver eseguito il codice precedente, il foglio di lavoro chiamato Foglio1 viene convertito in due file immagine (uno per pagina) Foglio 1 Pagina 1.Tiff e Foglio 1 Pagina 2.Tiff.

**File immagine generato (Foglio 1 Pagina 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**File immagine generato (Foglio 1 Pagina 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Questo articolo mostra come convertire un foglio di lavoro in un file immagine e convertire fogli di lavoro con più pagine in file immagine multipli (uno per pagina) utilizzando Aspose.Cells. Aspose.Cells offre maggiore flessibilità rispetto ad altri componenti e fornisce un'eccezionale velocità, efficienza e affidabilità. I risultati dimostrano che Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto.

{{% /alert %}}

## Articoli correlati

- [Conversione del foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/)
- [Esportare un foglio di lavoro o un grafico in un'immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
