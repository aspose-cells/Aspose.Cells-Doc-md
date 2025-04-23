---
title: Ottieni il Testo dell Equazione della Retta di Tendenza del Grafico
linktitle: Linea di tendenza
type: docs
weight: 90
url: /it/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

È possibile recuperare il Testo dell'Equazione della Retta di Tendenza utilizzando Aspose.Cells. Aspose.Cells fornisce proprietà [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) che restituisce il testo dell'equazione della retta di tendenza. Per utilizzare questa proprietà, sarà prima necessario chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **Esempio**

Lo screenshot seguente mostra il grafico con una retta di tendenza e il suo testo dell'equazione è mostrato in rosso. Recupereremo questo testo utilizzando la proprietà [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) nel seguente codice di esempio.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Codice Java per ottenere il testo dell'equazione della linea di tendenza del grafico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
