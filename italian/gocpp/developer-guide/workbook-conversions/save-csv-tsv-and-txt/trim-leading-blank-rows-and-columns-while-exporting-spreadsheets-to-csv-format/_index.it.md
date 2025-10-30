---
title: Taglia le righe e le colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV con Golang tramite C++
linktitle: Rimuovi righe e colonne vuote iniziali
type: docs
weight: 100
url: /it/go-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Scopri come rimuovere righe e colonne vuote iniziali durante l esportazione di fogli di calcolo in formato CSV usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte, il tuo file Excel o CSV ha colonne o righe vuote iniziali. Ad esempio, considera questa riga:

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Qui le prime tre celle o colonne sono vuote. Quando apri un file CSV del genere in Microsoft Excel, allora Microsoft Excel scarta queste righe e colonne vuote iniziali.

Per impostazione predefinita, Aspose.Cells non scarta le colonne e le righe vuote iniziali durante il salvataggio, ma se desideri rimuoverle proprio come fa Microsoft Excel, allora Aspose.Cells fornisce la proprietà [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/). Impostala su **true** e allora tutte le righe e le colonne vuote iniziali saranno eliminate durante il salvataggio.

{{% alert color="primary" %}}

 Prima del rilascio di Aspose.Cells for C++ 20.4, il valore predefinito di [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) era **false**. Dalla versione 20.4, il valore predefinito di [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) è **true.**

{{% /alert %}}

## **Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV**

Il seguente codice di esempio carica il [file excel di origine](sampleTrimBlankColumns.xlsx) che ha due colonne vuote iniziali. Prima salva il file excel in formato CSV senza alcuna modifica, e poi imposta la proprietà [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/gettrimleadingblankrowandcolumn/) su **true** e lo salva nuovamente. La schermata mostra il [file excel di origine](sampleTrimBlankColumns.xlsx), il [file CSV di output senza taglio](outputWithoutTrimBlankColumns.csv) e il [file CSV di output con taglio](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCsvFormat.go" >}}
