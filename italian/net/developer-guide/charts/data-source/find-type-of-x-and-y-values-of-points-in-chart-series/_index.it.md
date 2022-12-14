---
title: Trova il tipo di valori X e Y dei punti nella serie di grafici
type: docs
weight: 150
url: /it/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Possibili scenari di utilizzo**
A volte, vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce le proprietà ChartPoint.XValueType e ChartPoint.YValueType che possono essere utilizzate per questo scopo. Si noti che sarà necessario chiamare il metodo Chart.Calculate() prima di poter utilizzare queste proprietà in modo efficace.
## **Trova il tipo di valori X e Y dei punti nella serie di grafici**
 Il codice di esempio seguente carica il file[esempio di file Excel](64716905.xlsx) e accede al primo grafico all'interno del primo foglio di lavoro. Quindi chiama il metodo Chart.Calculate() e trova il tipo di valori X e Y del primo punto del grafico e li stampa sulla console. Si prega di consultare l'output della console mostrato di seguito per un riferimento.
## **Codice di esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Uscita console**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
