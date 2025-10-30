---
title: Imposta il Codice di Formattazione dei Valori della Serie del Grafico
description: Scopri come impostare il codice di formato dei valori delle serie di grafici in Aspose.Cells per Python via .NET. La nostra guida ti aiuterà a capire come formattare i dati della serie del grafico utilizzando il codice di formato appropriato, permettendoti di presentare i dati in modo accurato e professionale.
keywords: Aspose.Cells per Python via .NET, serie di grafici, codice di formato dei valori, formattazione, presentazione dei dati, accuratezza, professionalità.
linktitle: Formato numero
type: docs
weight: 100
url: /it/python-net/set-the-values-format-code-of-chart-series/
---

## **Possibili Scenari di Utilizzo**
Puoi impostare il codice di formato dei valori delle serie di grafico usando la proprietà [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code). Questa proprietà è utile non solo per le serie basate sull'intervallo all’interno del foglio di lavoro, ma anche per quelle create con un array di valori.

## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente esempio di codice aggiunge una serie in un grafico vuoto che non aveva serie prima. Aggiunge la serie usando l'array di valori. Una volta aggiunta, la formatta con il codice $#,##0 usando la proprietà [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code), e il numero 10000 diventa $10.000. La schermata mostra l’effetto del codice sul [file Excel di esempio](51740712.xlsx) e [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
{{< app/cells/assistant language="python-net" >}}
