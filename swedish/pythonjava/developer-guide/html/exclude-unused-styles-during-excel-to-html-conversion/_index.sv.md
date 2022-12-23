---
title: Uteslut oanvända formatmallar under konvertering av Excel till HTML
type: docs
weight: 30
url: /sv/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Uteslut oanvända formatmallar under konvertering av Excel till HTML**
Microsoft Excel-filer kan innehålla många oanvända stilar. När dessa filer exporteras till formatet HTML, exporteras även de oanvända formaten. Detta resulterar i en ökad storlek på utdata HTML. Aspose.Cells for Python via Java stöder exkludering av dessa stilar under konverteringen av Excel-fil till HTML. För detta tillhandahåller API[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)fast egendom. Ställa in värdet på[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) egendom till**Sann** kommer att utesluta alla oanvända stilar från utgången HTML.

Följande skärmdump visar oanvända stilar i filen HTML som kommer att tas bort genom att ställa in värdet på[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) egendom till**Sann**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Följande exempelkod visar hur man tar bort oanvända stilar under konvertering av Excel till HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
