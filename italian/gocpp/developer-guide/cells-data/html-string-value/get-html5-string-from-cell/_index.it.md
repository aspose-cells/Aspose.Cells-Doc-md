---
title: Ottieni la stringa HTML5 dalla cella con Golang tramite C++
linktitle: Ottieni la stringa HTML5 dalla cella
type: docs
weight: 90
url: /it/go-cpp/get-html5-string-from-cell/
description: Impara come ottenere la stringa HTML5 da una cella usando l API Aspose.Cells for C++.
keywords: Ottieni la stringa HTML5 dalla cella, Ottieni la stringa HTML5 dalla cella, Gestisci la stringa HTML5 della cella
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells restituisce la stringa HTML della cella usando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) che accetta un parametro booleano. Se passi **false** come parametro, restituirà HTML normale, se passi **true**, restituirà la stringa HTML5.

## **Ottieni la stringa HTML5 dalla cella**

Il codice di esempio seguente crea un oggetto workbook e aggiunge del testo nella cella A1 della prima scheda di lavoro. Quindi ottiene l'HTML normale e l'HTML5 dalla cella A1 utilizzando il metodo [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) e li stampa sulla console.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Output della console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
