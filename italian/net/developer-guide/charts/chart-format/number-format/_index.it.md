---
title: Impostare il codice del formato dei valori della serie di grafici
linktitle: Formato numerico
type: docs
weight: 100
url: /it/net/set-the-values-format-code-of-chart-series/
---
## **Possibili scenari di utilizzo**
È possibile impostare il codice del formato dei valori delle serie di grafici utilizzando il file[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)proprietà. Questa proprietà non è utile solo per le serie basate sull'intervallo all'interno del foglio di lavoro, ma funziona bene anche per le serie create con un array di valori.
## **Impostare il codice del formato dei valori della serie di grafici**
Il seguente codice di esempio aggiunge una serie nel grafico vuoto che non ha serie prima. Aggiunge la serie utilizzando l'array di valori. Una volta aggiunta la serie, la formatta con il codice $#,##0 utilizzando il file[Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode)proprietà e il numero 10000 diventa $ 10.000. Lo screenshot mostra l'effetto del codice sul file[esempio di file Excel](51740712.xlsx) e[file Excel di output](51740713.xlsx) dopo l'esecuzione.

![cose da fare:immagine_alt_testo](set-the-values-format-code-of-chart-series_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
