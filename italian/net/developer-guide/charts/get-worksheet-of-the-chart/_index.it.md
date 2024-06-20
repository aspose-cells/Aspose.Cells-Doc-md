---
title: Ottieni il foglio di lavoro del grafico
description: Scopri come recuperare il foglio di lavoro associato a un grafico di Excel usando l Aspose.Cells for .NET. La nostra guida ti mostrerà come accedere al foglio di lavoro e eseguire operazioni su di esso per manipolare i dati sottostanti del grafico.
keywords: Aspose.Cells for .NET, grafici di Excel, fogli di lavoro, manipolazione dei dati, dati sottostanti, operazioni.
type: docs
weight: 1000
url: /it/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, potresti voler accedere a un foglio di lavoro da un riferimento di un grafico. Aspose.Cells fornisce la proprietà [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

L'esempio seguente mostra come utilizzare la proprietà [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet). Il codice stampa prima il nome del foglio di lavoro, quindi accede al primo grafico sul foglio di lavoro. Stampa nuovamente il nome del foglio di lavoro, utilizzando la proprietà [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
