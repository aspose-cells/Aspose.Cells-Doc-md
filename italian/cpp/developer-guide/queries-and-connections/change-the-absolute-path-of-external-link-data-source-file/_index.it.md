---
title: Modifica il percorso assoluto della fonte dati del collegamento esterno con C++
linktitle: Modificare il percorso assoluto del file di origine dei dati del collegamento esterno
type: docs
weight: 290
url: /it/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Modifica il percorso assoluto del file di origine dati del collegamento esterno in Aspose.Cells con C++.
---

## Possibili scenari di utilizzo

Se vuoi cambiare il percorso assoluto del file di origine dati del collegamento esterno, utilizza il metodo [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/). Inizialmente, questa proprietà sarà impostata sul percorso da cui è stato caricato il file Excel. Ma puoi impostarla su una stringa vuota, o su un percorso di cartella locale o su un percorso di rete remoto. Ogni volta che cambierai questa proprietà, anche il percorso del file di origine dati del collegamento esterno verrà modificato.

Modificare il percorso assoluto del file di origine dei dati del collegamento esterno

Il seguente esempio di codice carica il [file Excel di esempio](5115146.xlsx) che contiene un collegamento esterno. Prima stampa la fonte dati del collegamento esterno che mostra il percorso remoto. Poi rimuove il percorso remoto e stampa di nuovo, questa volta mostra la fonte dati del collegamento esterno con il percorso locale. Successivamente, cambia il metodo [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) in un percorso locale e remoto e stampa di nuovo la fonte dati del collegamento esterno, e le modifiche si riflettono nell'output della console.

Ecco l'output della console o di debug dopo l'esecuzione del codice di esempio sopra con il [file di Excel di esempio](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
