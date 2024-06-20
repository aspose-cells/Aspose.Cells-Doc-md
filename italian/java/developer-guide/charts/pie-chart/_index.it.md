---
title: Creazione di un Grafico a Torta con Linee di Guida
linktitle: Grafico a Torta
type: docs
weight: 170
url: /it/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Questo articolo spiega come creare un grafico a torta con linee guida da zero utilizzando l'API Aspose.Cells for Java. In Excel, l'opzione 'Mostra linee guida' è impostata per impostazione predefinita quindi quando si crea un grafico a torta in Excel, le linee guida vengono mostrate. Tuttavia, mentre si crea un grafico simile con le API di Aspose.Cells, è necessario impostare esplicitamente la proprietà [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines).

{{% /alert %}}

## **Creazione di un grafico a torta con linee guida**

Per dimostrare l'uso dell'API Aspose.Cells for Java per creare un grafico a torta con linee guida, creeremo prima un nuovo [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) e inseriremo alcuni dati che fungeranno da origine dei dati della serie. Una volta che i dati sono in posizione, aggiungeremo un [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) di tipo [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) alla raccolta di grafici e impostare i suoi diversi aspetti per ottenere la visualizzazione del grafico desiderata.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Risultante grafico a torta**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Articoli correlati

- [Creazione e personalizzazione di grafici](/cells/it/java/creating-and-customizing-charts/)
- [Formattazione del grafico](/cells/it/java/chart-formatting/)
