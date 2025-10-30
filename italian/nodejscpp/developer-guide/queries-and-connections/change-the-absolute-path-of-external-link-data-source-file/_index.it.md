---
title: Cambia il percorso assoluto della fonte dati del collegamento esterno con Node.js tramite C++
linktitle: Modificare il percorso assoluto del file di origine dei dati del collegamento esterno
type: docs
weight: 290
url: /it/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Impara come cambiare il percorso assoluto del file sorgente di collegamento esterno usando Aspose.Cells for Node.js via C++. 
---

## Possibili scenari di utilizzo

Se desideri cambiare il percorso assoluto del file sorgente del collegamento esterno, utilizza la proprietà [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Inizialmente, questa proprietà sarà impostata al percorso da cui è stato caricato il file Excel. Ma puoi impostarla su una stringa vuota, oppure impostarla su un percorso di cartella locale o di rete remota. Ogni volta che modifichi questa proprietà, anche il percorso del file sorgente del collegamento esterno sarà aggiornato.

Modificare il percorso assoluto del file di origine dei dati del collegamento esterno

Il seguente esempio di codice carica il [file Excel di esempio](5115146.xlsx) che contiene un collegamento esterno. Prima stampa la sorgente del collegamento esterno che mostra il percorso remoto. Poi rimuove il percorso remoto e stampa di nuovo; questa volta, mostra la sorgente del collegamento esterno con il percorso locale. Infine cambia la proprietà [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) in un percorso locale e remoto e ristampa la sorgente del collegamento esterno, con le modifiche riflesse nell'output della console.

Ecco l'output della console o del debug dopo l'esecuzione del codice di esempio sopra con il [file excel di esempio](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
