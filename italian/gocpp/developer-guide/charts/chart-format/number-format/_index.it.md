---
title: Imposta il codice del formato valori della serie del grafico con Golang tramite C++
linktitle: Formato numero
type: docs
weight: 100
url: /it/go-cpp/set-the-values-format-code-of-chart-series/
description: Impara come impostare il codice di formato valori delle serie del grafico in Aspose.Cells for C++. La nostra guida ti aiuterà a capire come formattare i dati della serie del grafico usando il codice di formato appropriato, permettendoti di presentare i tuoi dati in modo accurato e professionale.
keywords: Aspose.Cells for C++, serie di grafico, codice di formato valori, formattazione, presentazione dei dati, precisione, professionalità.
---

## **Possibili Scenari di Utilizzo**
 Puoi impostare il codice del formato valori della serie del grafico usando la proprietà [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/). Questa proprietà non è utile solo per le serie basate sull'intervallo all'interno del foglio di lavoro, ma funziona bene anche per le serie create con un array di valori.

## **Impostare il codice di formato dei valori della serie del grafico**
Il codice di esempio seguente aggiunge una serie nel grafico vuoto che non aveva serie prima. Aggiunge la serie usando l'array di valori. Una volta aggiunta, la formatta con il codice `$#,##0` utilizzando la proprietà [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) e il numero `10000` diventa `$10.000`. lo screenshot mostra l'effetto del codice sul [file Excel di esempio](51740712.xlsx) e [file Excel di output](51740713.xlsx) dopo l'esecuzione.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
