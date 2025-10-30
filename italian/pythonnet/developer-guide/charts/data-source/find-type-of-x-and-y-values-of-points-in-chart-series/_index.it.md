---
title: Trova il tipo di valori X e Y dei punti nella serie del grafico
description: Scopri come determinare il tipo di valori X e Y nei punti della serie del grafico usando Aspose.Cells per Python via .NET. La nostra guida spiegherà i diversi tipi di valori dei dati e ti mostrerà come accedervi e lavorarci all’interno dei tuoi grafici.
keywords: Aspose.Cells per Python via .NET, diagrammi, valori X, valori Y, tipi di dati, accesso, lavoro con, serie di grafici.
type: docs
weight: 150
url: /it/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**
A volte vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells per Python via .NET fornisce le proprietà [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) e [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) che possono essere usate a tale scopo. Ricorda, devi chiamare il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) prima di poter utilizzare efficacemente queste proprietà.

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**
Il seguente esempio di codice carica il [file Excel di esempio](64716905.xlsx) e accede al primo grafico all’interno del primo foglio di lavoro. Successivamente, chiama il metodo [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) e determina il tipo di valori X e Y del primo punto del grafico, stampandoli sulla console. Consulta l'output della console mostrato di seguito per riferimento.

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Output della console**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
