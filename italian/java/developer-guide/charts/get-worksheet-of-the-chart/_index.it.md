---
title: Ottieni il foglio di lavoro del grafico
type: docs
weight: 80
url: /it/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, potresti voler accedere a un foglio di lavoro da un riferimento di un grafico. Aspose.Cells fornisce la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

## Esempio

L'esempio seguente mostra come utilizzare la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet). Il codice stampa prima il nome del foglio di lavoro, quindi accede al primo grafico sul foglio di lavoro. Stampa nuovamente il nome del foglio di lavoro, utilizzando la proprietà [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet).

### Codice Java per accedere al foglio di lavoro del grafico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Uscita della console generata dal codice di esempio

Di seguito è riportato l'output della console che risultato nel codice di esempio. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
