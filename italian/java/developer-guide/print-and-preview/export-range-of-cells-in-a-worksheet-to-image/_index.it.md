---
title: Esporta intervallo di Cells in un foglio di lavoro in immagine
type: docs
weight: 130
url: /it/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

È possibile creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells. Tuttavia, a volte è necessario esportare solo un intervallo di celle in un foglio di lavoro in un'immagine. Questo articolo spiega come raggiungere questo obiettivo.

{{% /alert %}}

 Per acquisire un'immagine di un intervallo, impostare l'area di stampa sull'intervallo desiderato, quindi impostare tutti i margini su 0. Impostare anche[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) a**VERO**.

Il codice seguente acquisisce un'immagine dell'intervallo E8:H10. Di seguito è riportato uno screenshot della cartella di lavoro di origine utilizzata nel codice. Puoi provare il codice con qualsiasi cartella di lavoro.

**File di input**

![cose da fare:immagine_alt_testo](export-range-of-cells-in-a-worksheet-to-image_1.png)

L'esecuzione del codice crea solo un'immagine dell'intervallo E8:H10.

**Immagine di uscita**

![cose da fare:immagine_alt_testo](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 Potresti trovare anche l'articolo[Conversione del foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/) utile.
