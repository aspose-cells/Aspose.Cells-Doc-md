---
title: Ottieni la stringa HTML5 da Cell
type: docs
weight: 40
url: /it/python-java/get-html5-string-from-cell/
---
## **Ottieni la stringa HTML5 da Cell**
Usando Aspose.Cells for Python via Java, puoi ottenere la stringa HTML dalla cella. Ciò può essere ottenuto utilizzando il[getHtmlString(booleano html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) metodo fornito dall'API. Se passi**falso**come parametro, ti restituirà HTML normale ma se lo passi**VERO**come parametro, restituirà la stringa HTML5.

Il seguente codice di esempio crea un oggetto cartella di lavoro e aggiunge del testo nella cella A1 del primo foglio di lavoro. Quindi ottiene la stringa HTML normale e HTML5 dalla cella A1 utilizzando il file[getHtmlString(booleano html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) e li stampa.
## **Codice di esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Di seguito è riportato l'output generato dallo snippet di codice sopra fornito.
## **Produzione**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
