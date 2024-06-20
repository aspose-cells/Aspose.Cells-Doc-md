---
title: Ottieni il Testo dell Equazione della Retta di Tendenza del Grafico
description: Scopri come utilizzare Aspose.Cells for .NET per recuperare il testo dell equazione di una retta di tendenza in un grafico creato in Microsoft Excel. La nostra guida mostrerà come accedere ed estrarre l equazione di una retta di tendenza per un analisi o visualizzazione ulteriori.
keywords: Aspose.Cells for .NET, Retta di Tendenza del Grafico, Testo dell Equazione, Microsoft Excel, Analisi dei Dati, Visualizzazione.
linktitle: Retta di Tendenza
type: docs
weight: 110
url: /it/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

È possibile recuperare il Testo dell'Equazione della Retta di Tendenza utilizzando Aspose.Cells. Aspose.Cells fornisce proprietà [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) che restituisce il testo dell'equazione della retta di tendenza. Per utilizzare questa proprietà, sarà prima necessario chiamare il metodo [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una retta di tendenza e il suo testo dell'equazione è mostrato in rosso. Recupereremo questo testo utilizzando la proprietà [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) nel seguente codice di esempio.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

Codice C# per ottenere il testo dell'equazione della retta di tendenza

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
