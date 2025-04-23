---
title: Exkludera oanvända stilar vid konvertering från Excel till HTML
type: docs
weight: 30
url: /sv/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Möjliga användningsscenario**

En Microsoft Excel-fil kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format exporteras även dessa oanvända stilar. Detta kan öka storleken på HTML-filen. Du kan utesluta oanvända stilar under konvertering av Excel-filen till HTML genom att använda [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) egenskapen. När du ställer in den till **true**, exkluderas alla oanvända stilar från utdata-HTML. Den följande skärmbilden visar ett prov på oanvänd stil i utdata-HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Uteslut oanvända stilar under Excel till HTML-konvertering**

Det följande kodexemplet skapar en arbetsbok och skapar även en oanvänd namngiven stil. Eftersom [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) är inställd på **true**, kommer denna oanvända namngivna stil inte att exporteras till [utdata-HTML](61767778.zip). Men om du sätter den till **false**, kommer denna oanvända stil att finnas i den genererade HTML-filen som du då kan se i HTML-markeringen, som visas på skärmbilden ovan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
