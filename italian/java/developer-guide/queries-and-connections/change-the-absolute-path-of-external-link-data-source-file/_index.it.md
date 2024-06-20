---
title: Modificare il percorso assoluto del file di origine dei dati del collegamento esterno
type: docs
weight: 1020
url: /it/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Possibili Scenari di Utilizzo**
Se desideri cambiare il percorso assoluto del file di origine dati del collegamento esterno, utilizza la proprietà Workbook.AbsolutePath. Inizialmente, questa proprietà sarà impostata sul percorso da cui è stato caricato il file excel. Ma puoi impostarlo su una stringa vuota o su un percorso di cartella locale o su un percorso di rete remota. Ogni volta che cambierai questa proprietà, il percorso del file di origine dati del collegamento esterno verrà anche modificato.
## **Cambia il percorso assoluto del file di origine dati del collegamento esterno**
Il seguente codice di esempio carica il file excel di esempio (5472589.xlsx) che contiene un collegamento esterno. Prima stampa il file di origine dati del collegamento esterno che stampa il percorso remoto. Poi rimuove il percorso remoto e stampa di nuovo, questa volta stampa il file di origine dati del collegamento esterno con il percorso locale. Poi cambia la proprietà Workbook.AbsolutePath in un percorso locale e remoto e stampa di nuovo il file di origine dati del collegamento esterno e le modifiche sono riflessi nell'output della console.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Output della console**
Ecco l'output della console o di debug dopo l'esecuzione del codice di esempio sopra con il file excel di esempio (5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
