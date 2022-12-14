---
title: Uteslut oanvända stilar under konvertering av Excel till HTML
type: docs
weight: 30
url: /sv/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Uteslut oanvända stilar under konvertering av Excel till HTML**
Microsoft Excel-filer kan innehålla många oanvända stilar. När dessa filer exporteras till HTML-format, exporteras även de oanvända stilarna. Detta resulterar i ökad storlek på utdata-HTML. Aspose.Cells för Python via Java stöder exkludering av dessa stilar under konverteringen av Excel-fil till HTML. För detta tillhandahåller API:et[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)fast egendom. Ställa in värdet på[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) egendom till**Sann** kommer att utesluta alla oanvända stilar från utdata-HTML.

Följande skärmdump visar oanvända stilar i HTML-filen som kommer att tas bort genom att ställa in värdet på[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) egendom till**Sann**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Följande exempelkod visar hur man tar bort oanvända stilar under konvertering av Excel till HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
