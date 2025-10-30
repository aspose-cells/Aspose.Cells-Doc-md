---
title: Modifica il percorso assoluto della sorgente dati del collegamento esterno con JavaScript tramite C++
linktitle: Modificare il percorso assoluto del file di origine dei dati del collegamento esterno
type: docs
weight: 290
url: /it/javascript-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Impara come cambiare il percorso assoluto della sorgente dei dati del collegamento esterno usando Aspose.Cells for JavaScript tramite C++. 
---

## Possibili scenari di utilizzo

Se desideri cambiare il percorso assoluto del file sorgente del collegamento esterno, utilizza la proprietà [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--). Inizialmente, questa proprietà sarà impostata al percorso da cui è stato caricato il file Excel. Ma puoi impostarla su una stringa vuota, oppure impostarla su un percorso di cartella locale o di rete remota. Ogni volta che modifichi questa proprietà, anche il percorso del file sorgente del collegamento esterno sarà aggiornato.

Modificare il percorso assoluto del file di origine dei dati del collegamento esterno

Il seguente esempio di codice carica il [file Excel di esempio](5115146.xlsx) che contiene un collegamento esterno. Prima stampa la sorgente del collegamento esterno che mostra il percorso remoto. Poi rimuove il percorso remoto e stampa di nuovo; questa volta, mostra la sorgente del collegamento esterno con il percorso locale. Infine cambia la proprietà [**Workbook.absolutePath**](https://reference.aspose.com/cells/javascript-cpp/workbook/#absolutePath--) in un percorso locale e remoto e ristampa la sorgente del collegamento esterno, con le modifiche riflesse nell'output della console.



{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
