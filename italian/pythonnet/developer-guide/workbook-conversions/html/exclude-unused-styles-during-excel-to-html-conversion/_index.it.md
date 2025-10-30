---
title: Escludere Stili Non Utilizzati durante la conversione da Excel a HTML
type: docs
weight: 30
url: /it/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Possibili Scenari di Utilizzo**

Il file Microsoft Excel può contenere molti stili non utilizzati. Quando si esporta il file Excel in formato HTML, anche questi stili non utilizzati vengono esportati. Questo può aumentare le dimensioni dell'HTML. È possibile escludere gli stili non utilizzati durante la conversione del file Excel in HTML utilizzando la proprietà [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles). Quando impostato su **true**, tutti gli stili non utilizzati vengono esclusi dall'HTML di output. La schermata seguente mostra uno stile non utilizzato di esempio all'interno dell'HTML di output.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**

Il codice di esempio seguente crea un libro di lavoro e crea anche uno stile nominato non utilizzato. Poiché il [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) è impostato su **true**, questo stile nominato non utilizzato non verrà esportato in [output HTML](61767778.zip). Ma se lo imposti su **false**, allora questo stile non utilizzato sarà presente all'interno dell'output HTML che potrai vedere nel markup HTML come mostrato nella schermata sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
