﻿---
title: Escludi stili inutilizzati durante la conversione da Excel a HTML
type: docs
weight: 30
url: /it/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Possibili scenari di utilizzo**

Microsoft Il file Excel può contenere molti stili inutilizzati. Quando si esporta il file Excel nel formato HTML, vengono esportati anche questi stili inutilizzati. Ciò può aumentare la dimensione di HTML. È possibile escludere gli stili inutilizzati durante la conversione del file Excel in HTML utilizzando il[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) proprietà. Quando lo imposti**VERO**, tutti gli stili inutilizzati sono esclusi dall'output HTML. Lo screenshot seguente mostra uno stile inutilizzato di esempio all'interno dell'output HTML.

![cose da fare:immagine_alt_testo](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Escludi stili inutilizzati durante la conversione da Excel a HTML**

Il codice di esempio seguente crea una cartella di lavoro e crea anche uno stile denominato inutilizzato. Dal momento che il[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) è impostato per**VERO** , questo stile con nome inutilizzato non verrà esportato in[uscita HTML](61767778.zip) . Ma se lo imposti su**falso**, allora questo stile inutilizzato sarà presente all'interno dell'output HTML che puoi quindi vedere nel markup HTML come mostrato nello screenshot sopra.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
