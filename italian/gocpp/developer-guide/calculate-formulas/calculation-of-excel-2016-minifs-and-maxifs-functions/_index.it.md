---
title: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016 con Golang tramite C++
description: Questo articolo introduce come usare la libreria Aspose.Cells per calcolare le funzioni MINIFS e MAXIFS in Microsoft Excel 2016 usando C++.
keywords: Aspose.Cells, Excel, 2016, funzione MINIFS, funzione MAXIFS, calcolo
type: docs
weight: 300
url: /it/go-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel 2016 supporta le funzioni MINIFS e MAXIFS. Queste funzioni non sono supportate in Excel 2013 o versioni precedenti. Aspose.Cells supporta anche il calcolo di queste funzioni. Lo screenshot seguente illustra l'uso di queste funzioni. Si prega di leggere i commenti in rosso all'interno dello screenshot per capire come funzionano queste funzioni.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016**
Il seguente esempio di codice carica il [file Excel di esempio](5115149.xlsx) e chiama il metodo [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) per eseguire il calcolo delle formule tramite Aspose.Cells e poi salva i risultati in un [file PDF di output](5115154.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculationOfExcel2016MinifsAndMaxifsFunctions.go" >}}
