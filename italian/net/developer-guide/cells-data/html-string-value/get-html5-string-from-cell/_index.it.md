---
title: Ottieni la stringa HTML5 da Cell
type: docs
weight: 90
url: /it/net/get-html5-string-from-cell/
---
## **Possibili scenari di utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) metodo che accetta un parametro booleano. Se passi**falso** come parametro, restituirà HTML normale ma se passi**VERO** come parametro, restituirà la stringa HTML5.

## **Ottieni la stringa HTML5 da Cell**

Il seguente codice di esempio crea un oggetto cartella di lavoro e aggiunge del testo nella cella A1 del primo foglio di lavoro. Quindi ottiene la stringa HTML normale e HTML5 dalla cella A1 utilizzando il file[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)metodo e li stampa sulla console.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
