---
title: Esporta un intervallo di celle in un foglio di lavoro in un immagine
type: docs
weight: 130
url: /it/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

È possibile creare un'immagine di un foglio di lavoro utilizzando Aspose.Cells. Tuttavia, talvolta è necessario esportare solo un intervallo di celle in un foglio di lavoro in un'immagine. Questo articolo spiega come raggiungere questo obiettivo.

{{% /alert %}}

Per acquisire un'immagine di un intervallo, imposta l'area di stampa sull'intervallo desiderato e quindi imposta tutti i margini a 0. Imposta anche [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) su **true**.

Il seguente codice acquisisce un'immagine dell'intervallo E8:H10. Di seguito è riportata un'immagine dello stesso foglio di lavoro utilizzato nel codice. Puoi provare il codice con qualsiasi foglio di lavoro.

**File di input**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Eseguendo il codice viene creata un'immagine solo dell'intervallo E8:H10.

**Immagine di output**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Potresti trovare utile anche l'articolo [Conversione foglio di lavoro in diversi formati di immagine](/cells/it/java/converting-worksheet-to-different-image-formats/).
