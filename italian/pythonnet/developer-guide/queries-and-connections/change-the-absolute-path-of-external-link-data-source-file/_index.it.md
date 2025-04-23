---
title: Modificare il percorso assoluto del file di origine dei dati del collegamento esterno
type: docs
weight: 290
url: /it/python-net/change-the-absolute-path-of-external-link-data-source-file/
---

## Possibili scenari di utilizzo

Se si desidera modificare il percorso assoluto del file di origine dei dati del collegamento esterno, utilizzare la proprietà [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path). Inizialmente, questa proprietà sarà impostata sul percorso da cui è stato caricato il file di Excel. Ma è possibile impostarlo su una stringa vuota o su un percorso di cartella locale o remoto. Ogni volta che si modificherà questa proprietà, verrà modificato anche il percorso del file di origine dei dati del collegamento esterno.

Modificare il percorso assoluto del file di origine dei dati del collegamento esterno

Il seguente codice di esempio carica il [file di Excel di esempio](5115146.xlsx) che contiene un collegamento esterno. Prima stampa il file di origine dei dati del collegamento esterno che stampa il percorso remoto. Quindi rimuove il percorso remoto e stampa di nuovo, questa volta stampa il file di origine dei dati del collegamento esterno con il percorso locale. Poi modifica la proprietà [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) in un percorso locale e remoto e stampa di nuovo il file di origine dei dati del collegamento esterno e le modifiche sono riflesse nell'output della console.

Ecco l'output della console o di debug dopo l'esecuzione del codice di esempio sopra con il [file di Excel di esempio](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

