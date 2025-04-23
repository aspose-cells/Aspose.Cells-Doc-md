---
title: Imposta il Codice di Formattazione dei Valori della Serie del Grafico
description: Scopri come impostare il codice del formato dei valori delle serie di grafici in Aspose.Cells for Java. La nostra guida ti aiuterà a capire come formattare i dati delle serie di grafici utilizzando il codice di formato appropriato, consentendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Aspose.Cells for Java, serie di grafici, codice del formato dei valori, formattazione, presentazione dei dati, precisione, professionalità.
linktitle: Formato numero
type: docs
weight: 100
url: /it/java/set-the-values-format-code-of-chart-series/
---

## **Possibili Scenari di Utilizzo**
Puoi impostare il codice del formato dei valori delle serie di grafici utilizzando il metodo [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-). Questo metodo è utile non solo per la serie basata sull'intervallo all'interno del foglio di lavoro ma funziona anche bene per la serie creata con un array di valori.
## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente codice di esempio aggiunge una serie nel grafico vuoto che non ha serie prima. Aggiunge la serie utilizzando l'array di valori. Una volta aggiunta la serie, la formatta con il codice $#,##0 utilizzando il metodo [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) e il numero 10000 diventa $10.000. La schermata mostra l'effetto del codice sul [file Excel di esempio](51740712.xlsx) e sul [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
{{< app/cells/assistant language="java" >}}
