---
title: Exkludera oanvända stilar vid konvertering från Excel till HTML
type: docs
weight: 30
url: /sv/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Möjliga användningsscenario**

Microsoft Excel-filen kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format exporteras även dessa oanvända stilar. Detta kan öka storleken på HTML. Du kan exkludera oanvända stilar vid konvertering av Excel-fil till HTML med hjälp av egenskapen [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles). När du ställer in den **true**, exkluderas alla oanvända stilar från utdata-HTML. Följande skärmbild visar ett exempel på en oanvänd stil i utdata-HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Uteslut oanvända stilar under Excel till HTML-konvertering**

Följande exempelkod skapar en arbetsbok och skapar även en oanvänd namngiven stil. Eftersom [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) är inställd på **true**, kommer denna oanvända namngivna stil inte att exporteras till [utdata-HTML](61767781.zip). Men om du ställer in den **false**, kommer denna oanvända stil att finnas i utdata-HTML som du sedan kan se i HTML-markeringen som visas i skärmbilden ovan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
