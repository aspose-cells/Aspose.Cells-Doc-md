---
title: Trova il tipo di valori X e Y dei punti nella serie del grafico
description: Scopri come determinare il tipo di valori X e Y nei punti delle serie del grafico utilizzando Aspose.Cells for .NET. La nostra guida spiegherà i diversi tipi di valori e ti mostrerà come accedere e lavorare con essi nei tuoi grafici.
keywords: Aspose.Cells for .NET, creazione di grafici, valori X, valori Y, tipi di dati, accesso, lavoro con serie di grafici.
type: docs
weight: 150
url: /it/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**
A volte, si desidera conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce le proprietà ChartPoint.XValueType e ChartPoint.YValueType che possono essere utilizzate a questo scopo. Si noti che sarà necessario chiamare il metodo Chart.Calculate() prima di poter utilizzare queste proprietà in modo efficace.
## **Trova il tipo di valori X e Y dei punti nella serie del grafico**
Il seguente codice di esempio carica il [file Excel di esempio](64716905.xlsx) e accede al primo grafico all'interno del primo foglio di lavoro. Quindi chiama il metodo Chart.Calculate() e trova il tipo di valori X e Y del primo punto del grafico e li stampa sulla console. Si prega di consultare l'output della console mostrato di seguito per un riferimento.

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Output della console**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
