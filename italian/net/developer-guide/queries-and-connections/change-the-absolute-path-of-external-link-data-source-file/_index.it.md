---
title: Modificare il percorso assoluto del file di origine dati del collegamento esterno
type: docs
weight: 290
url: /it/net/change-the-absolute-path-of-external-link-data-source-file/
---
## Possibili scenari di utilizzo

 Se si desidera modificare il percorso assoluto del file di origine dati del collegamento esterno, utilizzare l'estensione[**Cartella di lavoro.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)proprietà. Inizialmente, questa proprietà verrà impostata sul percorso da cui è stato caricato il file excel. Ma puoi impostarlo su una stringa vuota oppure puoi impostarlo su un percorso di cartella locale o su un percorso di rete remoto. Ogni volta che si modifica questa proprietà, verrà modificato anche il percorso del file di origine dati del collegamento esterno.

## Modificare il percorso assoluto del file di origine dati del collegamento esterno

 Il codice di esempio seguente carica il file[file excel di esempio](5115146.xlsx) che contiene un collegamento esterno. Prima stampa l'origine dati del collegamento esterno che stampa il percorso remoto. Quindi rimuove il percorso remoto e stampa di nuovo, questa volta stampa l'origine dati del collegamento esterno con il percorso locale. Poi cambia il[**Cartella di lavoro.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)property su un percorso locale e remoto e stampa nuovamente l'origine dati del collegamento esterno e le modifiche si riflettono nell'output della console.

Ecco l'output della console o di debug dopo l'esecuzione del codice di esempio precedente con il file[file excel di esempio](5115146.xlsx).

{{< highlight "java" >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
