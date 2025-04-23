---
title: Ottieni stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/net/get-html5-string-from-cell/
description: Impara come ottenere la stringa HTML5 dalla cella tramite l API Aspose.Cells for .NET
keywords: Ottieni la stringa HTML5 dalla cella, Ottieni la stringa HTML5 dalla cella, Gestisci la stringa HTML5 della cella
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) che accetta un parametro booleano. Se passi **false** come parametro, restituirà l'HTML normale ma se passi **true** come parametro, restituirà la stringa HTML5.

## **Ottieni una stringa HTML5 dalla cella**

Il codice di esempio seguente crea un oggetto workbook e aggiunge del testo nella cella A1 della prima scheda di lavoro. Quindi ottiene l'HTML normale e l'HTML5 dalla cella A1 utilizzando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) e li stampa sulla console.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Output della console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
