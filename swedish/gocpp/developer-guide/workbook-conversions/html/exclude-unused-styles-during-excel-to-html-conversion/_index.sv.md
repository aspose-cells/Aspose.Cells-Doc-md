---
title: Exkludera oanvända stilar under konvertering av Excel till HTML med Golang via C++
linktitle: Exkludera oanvända stilar
type: docs
weight: 30
url: /sv/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Lär dig hur du exkluderar oanvända stilar under konvertering av Excel till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Microsoft Excel-filer kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format exporteras även dessa oanvända stilar, vilket kan öka storleken på HTML-filen. Du kan exkludera de oanvända stilarna under konverteringen av en Excel-fil till HTML med [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/)-egenskapen. När du ställer in den till **true** exkluderas alla oanvända stilar från den genererade HTML:en. Följande skärmbild visar en exempelstil som inte används inuti HTML:n.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Uteslut oanvända stilar under Excel till HTML-konvertering**

Följande exempel skapar en arbetsbok och skapar även en oanvänd namnad stil. Eftersom [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) är inställd på **true**, kommer denna oanvända namngivna stil inte att exporteras till [utdata HTML](61767778.zip). Om du ställer in den på **false**, kommer denna oanvända stil att finnas i HTML:en, vilket du kan se i HTML-markeringen som visas i skärmbilden ovan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
