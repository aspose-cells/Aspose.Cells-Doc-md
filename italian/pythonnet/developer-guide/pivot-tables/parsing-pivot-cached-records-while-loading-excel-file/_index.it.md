---
title: Analisi dei record memorizzati nella cache del pivot durante il caricamento del file Excel
type: docs
weight: 70
url: /it/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Come analizzare i record memorizzati nella cache Pivot durante il caricamento del file Excel con Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Possibili scenari di utilizzo**

Quando crei una tabella pivot, Microsoft Excel prende una copia dei dati di origine e la archivia nella cache pivot. La Pivot Cache è contenuta nella memoria di Microsoft Excel. Non puoi vederlo, ma questi sono i dati a cui fa riferimento la tabella pivot quando crei la tabella pivot o modifichi una selezione del filtro dei dati o sposti righe/colonne. Ciò consente a Microsoft Excel di essere molto reattivo alle modifiche nella tabella pivot ma può anche raddoppiare la dimensione del file. Dopotutto, la Pivot Cache è solo un duplicato dei dati di origine, quindi è logico che la dimensione del file sia potenzialmente doppia.

Quando carichi il tuo file Excel all'interno dell'oggetto Workbook, puoi decidere se caricare o meno anche i record della Pivot Cache, utilizzando il comando[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)proprietà. Il valore predefinito di questa proprietà è *false**. Se Pivot Cache è abbastanza grande, può aumentare le prestazioni. Ma se vuoi caricare anche i record di Pivot Cache, dovresti impostare questa proprietà come *true**.

##  **Analisi dei record memorizzati nella cache del pivot durante il caricamento del file Excel**

Il seguente codice di esempio spiega l'utilizzo di[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)proprietà. Carica il[file Excel di esempio](61767773.xlsx) durante l'analisi dei record memorizzati nella cache pivot. Quindi aggiorna la tabella pivot e la salva come file[file Excel di output](61767774.xlsx).

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
