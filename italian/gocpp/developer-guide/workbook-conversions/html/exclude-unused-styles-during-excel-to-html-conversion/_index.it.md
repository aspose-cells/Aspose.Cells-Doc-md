---
title: Escludi stili inutilizzati durante la conversione da Excel a HTML con Golang via C++
linktitle: Escludi Stili Non Utilizzati
type: docs
weight: 30
url: /it/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Scopri come escludere stili non utilizzati durante la conversione da Excel a HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

I file Microsoft Excel possono contenere tanti stili inutilizzati. Quando esporti il file Excel in formato HTML, anche questi stili inutilizzati vengono esportati, il che può aumentare la dimensione dell'HTML. Puoi escludere gli stili inutilizzati durante la conversione di un file Excel in HTML usando la proprietà [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/). Quando la imposti su **true**, tutti gli stili inutilizzati vengono esclusi dall'HTML di output. Il seguente screenshot mostra un esempio di stile inutilizzato all'interno dell'HTML di output.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**

Il seguente esempio di codice crea un workbook e crea anche uno stile nominato inutilizzato. Poiché [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) è impostato su **true**, questo stile inutilizzato non verrà esportato nell'[HTML di output](61767778.zip). Tuttavia, se lo imposti su **false**, allora questo stile inutilizzato sarà presente nell'HTML di output, visibile nel markup HTML come mostrato nello screenshot sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
