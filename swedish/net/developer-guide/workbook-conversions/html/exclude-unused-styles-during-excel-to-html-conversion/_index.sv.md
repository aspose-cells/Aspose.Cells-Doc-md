---
title: Uteslut oanvända stilar under konvertering av Excel till HTML
type: docs
weight: 30
url: /sv/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Möjliga användningsscenarier**

Microsoft Excel-filen kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format, exporteras även dessa oanvända stilar. Detta kan öka storleken på HTML. Du kan utesluta oanvända stilar under konverteringen av Excel-fil till HTML med hjälp av[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) fast egendom. När du ställer in den**Sann**alla oanvända stilar exkluderas från utdata-HTML. Följande skärmdump visar ett exempel på en oanvänd stil i utdata-HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Uteslut oanvända stilar under konvertering av Excel till HTML**

Följande exempelkod skapar en arbetsbok och skapar även en oanvänd namngiven stil. Sedan[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) är satt till**Sann** , kommer denna oanvända namngivna stil inte att exporteras till[mata ut HTML](61767778.zip) . Men om du ställer in det på**falsk**, då kommer denna oanvända stil att finnas i utdata-HTML som du sedan kan se i HTML-uppmärkning som visas i skärmdumpen ovan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
