---
title: Imposta il Codice di Formattazione dei Valori della Serie del Grafico
description: Scopri come impostare il codice di formattazione dei valori della serie del grafico in Aspose.Cells for .NET. La nostra guida ti aiuterà a capire come formattare i dati della serie del tuo grafico utilizzando il codice di formattazione appropriato, permettendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Aspose.Cells for .NET, serie del grafico, codice di formato dei valori, formattazione, presentazione dei dati, precisione, professionalità.
linktitle: Formato numero
type: docs
weight: 100
url: /it/net/set-the-values-format-code-of-chart-series/
---

## **Possibili Scenari di Utilizzo**
E' possibile impostare il codice di formato dei valori della serie del grafico utilizzando la proprietà [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode). Questa proprietà non è utile solo per la serie basata sull'intervallo all'interno del foglio di lavoro ma funziona anche bene per la serie creata con un array di valori.
## **Impostare il codice di formato dei valori della serie del grafico**
Il seguente codice di esempio aggiunge una serie nel grafico vuoto che non ha serie prima. Aggiunge la serie utilizzando l'array di valori. Una volta aggiunta la serie, la formatta con il codice $#,##0 utilizzando la proprietà [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) e il numero 10000 diventa $10,000. La schermata mostra l'effetto del codice sul [file Excel di esempio](51740712.xlsx) e sull'[output del file Excel](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
{{< app/cells/assistant language="csharp" >}}
