---
title: Impostare il codice del formato dei valori della serie di grafici
type: docs
weight: 60
url: /it/java/set-the-values-format-code-of-chart-series/
---
## **Possibili scenari di utilizzo**

È possibile impostare il codice del formato dei valori delle serie di grafici utilizzando il file[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)proprietà. Questa proprietà non è utile solo per le serie che si basano sull'intervallo all'interno del foglio di lavoro, ma funziona bene anche per le serie create con un array di valori.

## **Impostare il codice del formato dei valori della serie di grafici**

Il seguente codice di esempio aggiunge una serie nel grafico vuoto che non ha serie prima. Aggiunge la serie utilizzando l'array di valori. Una volta aggiunta la serie, la formatta con il codice $#,##0 utilizzando il file[**Series.ValuesFormatCode**](https://reference.aspose.com/cells/java/com.aspose.cells/series#ValuesFormatCode)proprietà e il numero 10000 diventa $ 10.000. Lo screenshot mostra l'effetto del codice sul file[esempio di file Excel](51740736.xlsx)e[file Excel di output](51740735.xlsx)dopo l'esecuzione.

![cose da fare:immagine_alt_testo](set-the-values-format-code-of-chart-series_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-SetValuesFormatCodeOfChartSeries.java" >}}
