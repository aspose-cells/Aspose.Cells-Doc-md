---
title: Ottieni il foglio di lavoro del grafico con Golang tramite C++
linktitle: Ottieni il foglio di lavoro del grafico
description: Impara come recuperare il foglio di lavoro associato a un grafico Excel usando Aspose.Cells for C++. La nostra guida ti mostrerà come accedere al foglio di lavoro e eseguire operazioni su di esso per manipolare i dati sottostanti del grafico.
keywords: Aspose.Cells for C++, grafici Excel, fogli di lavoro, manipolazione dati, dati sottostanti, operazioni.
type: docs
weight: 1000
url: /it/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, vuoi accedere a un foglio di lavoro tramite il riferimento di un grafico. Aspose.Cells fornisce il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

Il seguente esempio mostra come usare il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/). Il codice prima stampa il nome del foglio di lavoro, poi accede al primo grafico sul foglio. Successivamente, stampa di nuovo il nome del foglio, usando il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
