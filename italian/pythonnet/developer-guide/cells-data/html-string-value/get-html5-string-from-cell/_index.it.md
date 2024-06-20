---
title: Ottieni stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/python-net/get-html5-string-from-cell/
description: Scopri come ottenere una stringa HTML5 dalla cella tramite l API Aspose.Cells per Python via .NET.
keywords: Excel Libreria di Python, Ottieni stringa HTML5 dalla cella in Python, Ottenere stringa HTML5 dalla cella utilizzando Python, Gestisci stringa HTML5 della cella in Python.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET restituisce la stringa HTML della cella utilizzando il metodo [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) che accetta un parametro booleano. Se passi **false** come parametro, restituirà l'HTML normale, ma se passi **true** come parametro, restituirà la stringa HTML5.

## **Ottieni una stringa HTML5 dalla cella**

Il codice di esempio seguente crea un oggetto workbook e aggiunge del testo nella cella A1 della prima scheda di lavoro. Quindi ottiene l'HTML normale e l'HTML5 dalla cella A1 utilizzando il metodo [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) e li stampa sulla console.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Output della console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
