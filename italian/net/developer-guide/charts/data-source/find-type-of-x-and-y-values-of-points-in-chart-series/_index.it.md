---
title: Trova il tipo di valori X e Y dei punti nella serie di grafici
description: Scopri come determinare il tipo di valori X e Y nei punti delle serie di grafici utilizzando Aspose.Cells for .NET. La nostra guida spiegherà i diversi tipi di valori di dati e ti mostrerà come accedervi e lavorare con essi nei tuoi grafici.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /it/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Possibili scenari di utilizzo**
A volte, vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce le proprietà ChartPoint.XValueType e ChartPoint.YValueType che possono essere utilizzate per questo scopo. Tieni presente che dovrai chiamare il metodo Chart.Calculate() prima di poter utilizzare queste proprietà in modo efficace.
##  **Trova il tipo di valori X e Y dei punti nella serie di grafici**
 Il codice di esempio seguente carica il file[file Excel di esempio](64716905.xlsx) e accede al primo grafico all'interno del primo foglio di lavoro. Quindi chiama il metodo Chart.Calculate() e trova il tipo di valori X e Y del primo punto del grafico e li stampa sulla console. Per riferimento, vedere l'output della console mostrato di seguito.
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Uscita della console**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
