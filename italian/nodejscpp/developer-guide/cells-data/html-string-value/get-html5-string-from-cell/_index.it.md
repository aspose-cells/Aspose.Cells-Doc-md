---
title: Ottieni stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/nodejs-cpp/get-html5-string-from-cell/
description: Impara come ottenere la stringa HTML5 dalla cella attraverso l API Aspose.Cells for Node.js via C++.
keywords: Ottieni la stringa HTML5 dalla cella Node.js tramite C++, Ottieni la stringa HTML5 dalla cella Node.js tramite C++, Gestisci la stringa HTML5 della cella Node.js tramite C++
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells restituisce la stringa HTML della cella utilizzando il metodo [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) che accetta un parametro booleano. Se passi **false** come parametro, restituirà HTML normale, se passi **true** come parametro, restituirà la stringa HTML5.

## **Ottieni una stringa HTML5 dalla cella**

Il seguente esempio di codice crea un oggetto workbook e aggiunge del testo nella cella A1 del primo foglio di lavoro. Successivamente, ottiene le stringhe HTML normale e HTML5 dalla cella A1 usando il metodo [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) e le stampa nella console.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Output della console**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
