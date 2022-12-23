---
title: Ottieni la stringa HTML5 da Cell
type: docs
weight: 90
url: /it/java/get-html5-string-from-cell/
---
## **Possibili scenari di utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il[**getHtmlString(booleano html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)metodo. Se passi**falso**come parametro, ti restituirà Normal HTML ma se passi**VERO**come parametro, restituirà la stringa HTML5.

## **Ottieni la stringa HTML5 da Cell**

Il seguente codice di esempio crea un oggetto cartella di lavoro e aggiunge del testo nella cella A1 del primo foglio di lavoro. Quindi ottiene la stringa Normal HTML e HTML5 dalla cella A1 utilizzando il file[**getHtmlString(booleano html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)metodo e li stampa sulla console.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
