---
title: Trova il tipo di valori X e Y dei punti nella serie del grafico
type: docs
weight: 110
url: /it/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**

A volte si desidera conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce le proprietà [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) e [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) che possono essere utilizzate a tale scopo. Si noti che sarà necessario chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) prima di poter utilizzare efficacemente queste proprietà.

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**

Il seguente codice di esempio carica il [file Excel di esempio](64716920.xlsx) e accede al primo grafico nel primo foglio di lavoro. Chiama poi il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) e trova il tipo di valori X e Y del primo punto del grafico e li stampa sulla console. Si prega di vedere l'output della console mostrato di seguito per riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Output della console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
