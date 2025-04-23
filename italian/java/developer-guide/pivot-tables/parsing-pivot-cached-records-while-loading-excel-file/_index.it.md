---
title: Analisi dei record memorizzati nella cache pivot durante il caricamento del file Excel
type: docs
weight: 100
url: /it/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Possibili Scenari di Utilizzo**

Quando si crea una tabella pivot, Microsoft Excel prende una copia dei dati di origine e li memorizza nella cache pivot. La cache pivot è memorizzata all'interno della memoria di Microsoft Excel. Non è possibile vederla, ma sono i dati a cui la tabella pivot fa riferimento quando si costruisce la tabella pivot o si modifica una selezione di sfilatori o si spostano righe/colonne. Questo consente a Microsoft Excel di rispondere molto rapidamente ai cambiamenti nella tabella pivot, ma può anche raddoppiare le dimensioni del file. Dopotutto, la cache pivot è solo una duplicazione dei dati di origine, quindi ha senso che le dimensioni del file siano potenzialmente raddoppiate.

Quando si carica il file di Excel all'interno dell'oggetto Workbook, è possibile decidere se si desidera caricare anche i record della Cache pivot o meno, utilizzando la proprietà [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Il valore predefinito di questa proprietà è **falso**. Se la Cache pivot è piuttosto grande, può aumentare le prestazioni. Ma se si desidera anche caricare i record della Cache pivot, è necessario impostare questa proprietà su **true**.

## **Analisi dei record memorizzati nella cache della tabella pivot durante il caricamento del file Excel**

Il seguente codice di esempio spiega l'uso della proprietà [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Carica il [file di Excel di esempio](61767786.xlsx) mentre analizza i record della Cache pivot. Poi aggiorna la tabella pivot e la salva come il [file di Excel di output](61767785.xlsx).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
