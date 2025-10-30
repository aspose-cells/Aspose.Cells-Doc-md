---
title: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV con Golang tramite C++
linktitle: Mantieni i separatori per le righe vuote durante l esportazione di fogli di calcolo in formato CSV
type: docs
weight: 160
url: /it/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Impara come mantenere i separatori per le righe vuote quando esporti fogli di calcolo in formato CSV usando Aspose.Cells con Golang tramite C++.
---

## **Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV**

Aspose.Cells offre la possibilità di mantenere i separatori di linea durante la conversione di fogli di calcolo in formato CSV. Per questo, puoi usare la proprietà [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) della classe [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) è una proprietà booleana. Per mantenere i separatori per le linee vuote durante la conversione del file Excel in CSV, imposta la proprietà [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) a **true**.

Il seguente esempio di codice carica il [file Excel di origine](84378743.xlsx). Imposta la proprietà [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) su **true** e lo salva come [output.csv](84378744.csv). Lo screenshot mostra il confronto tra il file Excel sorgente, l'output predefinito generato durante la conversione in CSV e l'output generato impostando [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) su **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
