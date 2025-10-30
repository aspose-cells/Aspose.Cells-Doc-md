---
title: Ottieni il foglio di lavoro del grafico
description: Impara come recuperare il foglio di lavoro associato a un grafico Excel usando Aspose.Cells per Python via .NET. La nostra guida ti mostrerà come accedere al foglio di lavoro e eseguire operazioni su di esso per manipolare i dati sottostanti del grafico.
keywords: Aspose.Cells per Python via .NET, grafici Excel, fogli di lavoro, manipolazione dati, dati sottostanti, operazioni.
type: docs
weight: 1000
url: /it/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, vuoi accedere a un foglio di lavoro da un riferimento di un grafico. Aspose.Cells per Python via .NET fornisce la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

L'esempio seguente mostra come utilizzare la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet). Il codice stampa prima il nome del foglio di lavoro, quindi accede al primo grafico sul foglio di lavoro. Stampa nuovamente il nome del foglio di lavoro, utilizzando la proprietà [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
