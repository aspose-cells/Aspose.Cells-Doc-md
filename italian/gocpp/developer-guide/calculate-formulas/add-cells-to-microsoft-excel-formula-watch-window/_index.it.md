---
title: Aggiungi Celle alla finestra di monitoraggio delle formule di Microsoft Excel con Golang tramite C++
linktitle: Aggiungi celle alla finestra di watch della formula
description: Impara come usare Aspose.Cells for C++ per aggiungere celle alla finestra di watch della formula in Excel. Carica o crea un file Excel, manipola celle, imposta formule e salva il file modificato.
keywords: Aspose.Cells, Excel, finestra di watch della formula, celle, aggiunta, C++
type: docs
weight: 60
url: /it/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Possibili Scenari di Utilizzo**

La finestra di watch di Microsoft Excel è uno strumento utile per monitorare comodamente i valori delle celle e le loro formule in una finestra. Puoi aprire *Watch Window* in Microsoft Excel cliccando su *Formulas > Watch Window*. Ha il pulsante *Add Watch* che può essere usato per aggiungere celle per l'ispezione. Allo stesso modo, puoi usare il metodo [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/) per aggiungere celle alla *Watch Window* utilizzando l'API di Aspose.Cells.

## **Aggiungere celle alla finestra di visualizzazione della formula di Microsoft Excel**

Il seguente esempio di codice imposta la formula delle celle C1 ed E1 e le aggiunge entrambe alla Watch Window. Successivamente salva il file come [file Excel di output](67338481.xlsx). Se apri il file Excel di output e visualizzi la *Watch Window*, vedrai entrambe le celle come mostrato in questo screenshot.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
