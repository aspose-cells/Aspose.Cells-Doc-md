---
title: Ottieni stringa HTML5 dalla cella
type: docs
weight: 40
url: /it/python-java/get-html5-string-from-cell/
---

## **Ottieni una stringa HTML5 dalla cella**
Utilizzando Aspose.Cells per Python via Java, è possibile ottenere la stringa HTML dalla cella. Ciò può essere realizzato utilizzando il metodo [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) fornito dall'API. Se si passa **false** come parametro, verrà restituita una Normale stringa HTML, ma se si passa **true** come parametro, verrà restituita una stringa HTML5.

Il seguente codice di esempio crea un oggetto workbook e aggiunge del testo nella cella A1 del primo foglio di lavoro. Viene quindi ottenuta la Normale stringa HTML e la stringa HTML5 dalla cella A1 utilizzando il metodo [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) e stampate.
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Il seguente è l'output generato dal frammento di codice fornito sopra.
## **Output**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
