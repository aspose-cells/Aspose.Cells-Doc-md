---
title: Analisi dei record memorizzati nella cache pivot durante il caricamento del file Excel
type: docs
weight: 100
url: /it/java/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Possibili scenari di utilizzo**

Quando crei una tabella pivot, Microsoft Excel prende una copia dei dati di origine e la archivia nella cache pivot. La Pivot Cache è contenuta all'interno della memoria di Microsoft Excel. Non puoi vederlo, ma questi sono i dati a cui fa riferimento la tabella pivot quando crei la tabella pivot o modifichi una selezione Slicer o sposti righe/colonne. Ciò consente a Microsoft Excel di essere molto reattivo alle modifiche nella tabella pivot, ma può anche raddoppiare le dimensioni del file. Dopotutto, Pivot Cache è solo un duplicato dei tuoi dati di origine, quindi ha senso che la dimensione del tuo file sia potenzialmente doppia.

Quando carichi il tuo file Excel all'interno dell'oggetto Workbook, puoi decidere se caricare o meno anche i record della Pivot Cache, utilizzando il[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)proprietà. Il valore predefinito di questa proprietà è**falso**. Se Pivot Cache è abbastanza grande, può aumentare le prestazioni. Ma se vuoi caricare anche i record di Pivot Cache, dovresti impostare questa proprietà come**VERO**.

## **Analisi dei record memorizzati nella cache pivot durante il caricamento del file Excel**

Il seguente codice di esempio spiega l'utilizzo di[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)proprietà. Carica il[esempio di file Excel](61767786.xlsx)durante l'analisi dei record memorizzati nella cache del pivot. Quindi aggiorna la tabella pivot e la salva come file[file Excel di output](61767785.xlsx).

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
