---
title: Analisi dei record memorizzati nella cache pivot durante il caricamento del file Excel
type: docs
weight: 70
url: /it/nodejs-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Possibili Scenari di Utilizzo**

Quando si crea una tabella pivot, Microsoft Excel prende una copia dei dati di origine e li memorizza nella cache pivot. La cache pivot è memorizzata all'interno della memoria di Microsoft Excel. Non è possibile vederla, ma sono i dati a cui la tabella pivot fa riferimento quando si costruisce la tabella pivot o si modifica una selezione di sfilatori o si spostano righe/colonne. Questo consente a Microsoft Excel di rispondere molto rapidamente ai cambiamenti nella tabella pivot, ma può anche raddoppiare le dimensioni del file. Dopotutto, la cache pivot è solo una duplicazione dei dati di origine, quindi ha senso che le dimensioni del file siano potenzialmente raddoppiate.

Quando carichi il tuo file Excel all'interno dell'oggetto Workbook, puoi decidere se desideri anche caricare i record della Cache dei Pivot o meno, utilizzando la proprietà [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-). Il valore predefinito di questa proprietà è **falso**. Se la Cache dei Pivot è piuttosto grande, può aumentare le prestazioni. Ma se desideri anche caricare i record della Cache dei Pivot, dovresti impostare questa proprietà su **vero**.

## **Analisi dei record memorizzati nella cache della tabella pivot durante il caricamento del file Excel**

Il codice di esempio seguente spiega l'uso della proprietà [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-). Carica il [file Excel di esempio](61767773.xlsx) mentre analizza i record memorizzati nella cache dei pivot. Quindi aggiorna la tabella pivot e la salva come [file Excel di output](61767774.xlsx).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
