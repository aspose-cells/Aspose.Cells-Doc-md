---
title: Ottenere il testo dell equazione della linea di tendenza del grafico con Golang tramite C++
linktitle: Retta di Tendenza
description: Impara come usare Aspose.Cells for C++ per recuperare il testo dell equazione di una trendline in un grafico creato in Microsoft Excel. La nostra guida dimostrerà come accedere ed estrarre l equazione di una trendline per ulteriori analisi o visualizzazione.
keywords: Aspose.Cells for C++, Trendline del grafico, Testo dell equazione, Microsoft Excel, Analisi dei dati, Visualizzazione.
type: docs
weight: 110
url: /it/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

È possibile recuperare il Testo dell'Equazione della Retta di Tendenza utilizzando Aspose.Cells. Aspose.Cells fornisce proprietà [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) che restituisce il testo dell'equazione della retta di tendenza. Per utilizzare questa proprietà, sarà prima necessario chiamare il metodo [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una Trendline e il suo testo dell’equazione mostrato in rosso. Recupereremo questo testo usando la proprietà [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) nel seguente esempio di codice.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Codice C++ per ottenere il testo dell'equazione della trendline del grafico

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
