---
title: Trova il tipo di valori X e Y dei punti nella serie di grafici
type: docs
weight: 110
url: /it/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Possibili scenari di utilizzo**

A volte, vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)e[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)proprietà utilizzabili a tale scopo. Tieni presente che dovrai chiamare[**Grafico.calcola()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) prima di poter utilizzare queste proprietà in modo efficace.

## **Trova il tipo di valori X e Y dei punti nella serie di grafici**

Il codice di esempio seguente carica il file[esempio di file Excel](64716920.xlsx)e accede al primo grafico all'interno del primo foglio di lavoro. Quindi chiama il[**Grafico.calcola()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()e trova il tipo di valori X e Y del primo punto del grafico e li stampa sulla console. Si prega di consultare l'output della console mostrato di seguito per un riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Uscita console**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
