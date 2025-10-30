---
title: Ottieni il Testo dell Equazione della Retta di Tendenza del Grafico
description: Impara come usare Aspose.Cells per Python via .NET per recuperare il testo dell equazione di una linea di tendenza in un grafico creato in Microsoft Excel. La nostra guida dimostrerà come accedere ed estrarre l equazione di una linea di tendenza per un ulteriore analisi o visualizzazione.
keywords: Aspose.Cells per Python via .NET, Linea di Tendenza nel Grafico, Testo dell Equazione, Microsoft Excel, Analisi Dati, Visualizzazione.
linktitle: Retta di Tendenza
type: docs
weight: 110
url: /it/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puoi recuperare il Testo dell'Equazione della linea di tendenza del grafico usando Aspose.Cells per Python via .NET. Essa fornisce una proprietà che restituisce il Testo dell'Equazione della linea di tendenza del grafico. Per utilizzare questa proprietà, devi prima chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una retta di tendenza e il suo testo dell'equazione è mostrato in rosso. Recupereremo questo testo utilizzando la proprietà [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) nel seguente codice di esempio.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

Codice C# per ottenere il testo dell'equazione della retta di tendenza

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
