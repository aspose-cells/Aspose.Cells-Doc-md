---
title: Ridimensionare la forma dell etichetta dati del grafico per adattare il testo
type: docs
weight: 190
url: /it/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

L'applicazione Excel fornisce l'opzione **Ridimensiona la forma per adattare il testo** per le etichette dati del grafico al fine di aumentare le dimensioni della forma in modo che il testo ci stia dentro. Questa opzione può essere accessibile dall'interfaccia di Excel selezionando una qualsiasi delle etichette dati sul grafico. Fai clic con il tasto destro e seleziona il menu **Formato etichette dati**. Sulla scheda **Dimensioni e proprietà**, espandi **Allineamento** per rivelare le proprietà correlate tra cui l'opzione **Ridimensiona la forma per adattare il testo**.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Ridimensiona la forma dell'etichetta dati del grafico per adattarla al testo**

Per emulare la funzione di Excel di ridimensionare le forme delle etichette dati per adattare il testo, le API di Aspose.Cells hanno esposto la proprietà di tipo Boolean [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText). Il seguente pezzo di codice mostra lo scenario d'uso semplice di tale proprietà.

Il grafico appare come segue prima di eseguire il codice.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Il grafico appare come segue dopo l'esecuzione del codice.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
