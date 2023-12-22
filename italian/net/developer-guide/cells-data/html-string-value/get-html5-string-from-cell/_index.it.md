---
title: Ottieni la stringa HTML5 da Cell
type: docs
weight: 90
url: /it/net/get-html5-string-from-cell/
description: Scopri come ottenere la stringa HTML5 da Cell a Aspose.Cells for .NET API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **Possibili scenari di utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il[**OttieniHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) metodo che accetta un parametro booleano. Se passi**falso** come parametro restituirà Normal HTML ma se passi**VERO** come parametro, restituirà la stringa HTML5.

##  **Ottieni la stringa HTML5 da Cell**

Il codice di esempio seguente crea un oggetto cartella di lavoro e aggiunge del testo nella cella A1 del primo foglio di lavoro. Quindi ottiene la stringa Normal HTML e HTML5 dalla cella A1 utilizzando il file[**OttieniHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)metodo e li stampa sulla console.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **Uscita della console**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
