---
title: Imposta il codice formato valori della serie di grafici
description: Scopri come impostare il codice del formato dei valori delle serie di grafici in Aspose.Cells for Java. La nostra guida ti aiuterà a capire come formattare i dati delle serie di grafici utilizzando il codice di formato appropriato, consentendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Formato numero
type: docs
weight: 100
url: /it/java/set-the-values-format-code-of-chart-series/
---
##  **Possibili scenari di utilizzo**
È possibile impostare il codice del formato dei valori delle serie di grafici utilizzando[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) metodo. Questo metodo non è utile solo per le serie basate sull'intervallo all'interno del foglio di lavoro, ma funziona bene anche per le serie create con un array di valori.
##  **Imposta il codice formato valori della serie di grafici**
 Il seguente codice di esempio aggiunge una serie nel grafico vuoto che non ha serie prima. Aggiunge la serie utilizzando la matrice di valori. Una volta aggiunta la serie, la formatta con il codice $#,##0 utilizzando il file[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-)metodo e il numero 10000 diventa $ 10.000. Lo screenshot mostra l'effetto del codice sul file[file Excel di esempio](51740712.xlsx) E[file Excel di output](51740713.xlsx) dopo l'esecuzione.

![cose da fare:immagine_alt_testo](set-the-values-format-code-of-chart-series_1.png)
##  **Codice d'esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
