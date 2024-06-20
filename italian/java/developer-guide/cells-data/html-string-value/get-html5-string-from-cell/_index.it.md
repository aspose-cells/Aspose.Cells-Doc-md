---
title: Ottieni stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/java/get-html5-string-from-cell/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il metodo [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). Se passi **false** come parametro, ti restituirà HTML normale ma se passi **true** come parametro, ti restituirà la stringa HTML5.

## **Ottieni una stringa HTML5 dalla cella**

Il seguente codice di esempio crea un oggetto workbook e aggiunge del testo nella cella A1 del primo foglio di lavoro. Ottiene quindi la stringa HTML normale e HTML5 dalla cella A1 utilizzando il metodo [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString) e le stampa sulla console.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Output della console**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
