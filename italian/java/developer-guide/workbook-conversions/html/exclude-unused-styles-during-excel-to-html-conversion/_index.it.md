---
title: Escludere Stili Non Utilizzati durante la conversione da Excel a HTML
type: docs
weight: 30
url: /it/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Possibili Scenari di Utilizzo**

Il file di Microsoft Excel può contenere molti stili non utilizzati. Quando esporti il file Excel in formato HTML, questi stili non utilizzati vengono esportati. Questo può aumentare le dimensioni dell'HTML. Puoi escludere gli stili non utilizzati durante la conversione del file Excel in HTML utilizzando la proprietà [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) . Quando la imposti su **true**, tutti gli stili non utilizzati vengono esclusi dall'HTML di output. La seguente schermata mostra un esempio di stile non utilizzato all'interno dell'HTML di output.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**

Il seguente codice di esempio crea un workbook e crea anche uno stile denominato non utilizzato. Poiché [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) è impostato su **true**, questo stile non utilizzato non verrà esportato su [output HTML](61767781.zip). Ma se lo imposti su **false**, allora questo stile non utilizzato sarà presente all'interno dell'HTML di output che potrai poi vedere nel markup HTML come mostrato nella schermata sopra.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
