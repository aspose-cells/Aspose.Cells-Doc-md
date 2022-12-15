---
title: Ottieni il testo dell'equazione della linea di tendenza del grafico
linktitle: Linea di tendenza
type: docs
weight: 90
url: /it/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 È possibile recuperare il testo dell'equazione della linea di tendenza del grafico utilizzando Aspose.Cells. Aspose.Cells fornisce[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) proprietà che restituisce il testo dell'equazione della linea di tendenza del grafico. Per usufruire di questa proprietà, dovrai prima chiamare[**Grafico.calcola()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) metodo.

{{% /alert %}}

## **Esempio**

 La seguente schermata mostra il grafico con una linea di tendenza e il suo testo dell'equazione è mostrato in colore rosso. Recupereremo questo testo utilizzando il file[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)property nel codice di esempio seguente.

![cose da fare:immagine_alt_testo](get-equation-text-of-chart-trendline_1.png)

### Codice Java per ottenere il testo dell'equazione della linea di tendenza del grafico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Output generato dal codice di esempio

Questo è l'output della console del codice di esempio precedente.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
