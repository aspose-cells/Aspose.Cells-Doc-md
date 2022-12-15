---
title: Conversione del foglio di lavoro in immagine e del foglio di lavoro in immagine per pagina
type: docs
weight: 210
url: /it/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e un foglio di lavoro con più pagine in un file immagine per pagina.

A volte, potrebbe essere necessario presentare i fogli di lavoro come immagini, ad esempio per utilizzarli in applicazioni o pagine Web. Potrebbe essere necessario inserire le immagini in un documento Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. Semplicemente, vuoi rendere il foglio di lavoro come un'immagine. Aspose.Cells Le API supportano la conversione in immagini dei fogli di lavoro nei file di Microsoft Excel. Inoltre, Aspose.Cells supporta la conversione di una cartella di lavoro in più file immagine, uno per pagina.

{{% /alert %}}

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in file di immagine**

Questo articolo mostra come utilizzare l'API Aspose.Cells for Java per convertire un foglio di lavoro in un'immagine. L'API fornisce diverse classi utili, ad esempio[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**Workbook Render**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , e così via. Il[**FoglioRendering**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class rappresenta un foglio di lavoro per il rendering delle immagini per il foglio di lavoro e ha un overload[**immaginare**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) che può convertire un foglio di lavoro in file immagine direttamente con qualsiasi attributo o opzione impostata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Risultato**

Dopo aver eseguito il codice precedente, il foglio di lavoro denominato Sheet1 viene convertito in un file immagine SheetImage.jpg.

**L'output JPG**

![cose da fare:immagine_alt_testo](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Utilizzo di Aspose.Cells per convertire il foglio di lavoro in file immagine per pagina**

Questo esempio mostra come usare Aspose.Cells per convertire un foglio di lavoro da una cartella di lavoro modello con diverse pagine in un file di immagine per pagina.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Risultato**

Dopo aver eseguito il codice precedente, il foglio di lavoro denominato Foglio1 viene convertito in due file immagine (1 per pagina) Foglio 1 Pagina 1.Tiff e Foglio 1 Pagina 2.Tiff.

**File immagine generato (Foglio 1 Pagina 1.Tiff)**

![cose da fare:immagine_alt_testo](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**File immagine generato (Foglio 1 Pagina 2.Tiff)**

![cose da fare:immagine_alt_testo](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Questo articolo mostra come convertire un foglio di lavoro in un file immagine e convertire fogli di lavoro con più pagine in più file immagine (uno per pagina) utilizzando Aspose.Cells. Aspose.Cells offre maggiore flessibilità rispetto ad altri componenti e fornisce velocità, efficienza e affidabilità eccezionali. I risultati mostrano che Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto.

{{% /alert %}}

## articoli Correlati

- [Conversione del foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/)
- [Esporta foglio di lavoro o grafico in immagine con larghezza e altezza desiderate](/cells/it/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
