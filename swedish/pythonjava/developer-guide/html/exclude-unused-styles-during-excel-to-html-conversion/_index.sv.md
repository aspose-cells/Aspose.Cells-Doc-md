---
title: Exkludera oanvända stilar vid konvertering från Excel till HTML
type: docs
weight: 30
url: /sv/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Uteslut oanvända stilar under Excel till HTML-konvertering**
Microsoft Excel-filer kan innehålla många oanvända stilar. När dessa filer exporteras till HTML-format exporteras också de oanvända stilarna. Detta resulterar i en ökad storlek på den resulterande HTML-filen. Aspose.Cells för Python via Java stöder uteslutning av dessa stilar under konvertering av Excel-fil till HTML. För detta tillhandahåller API:et egenskapen [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles). Genom att ange värdet för [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) till **Sant** kommer alla oanvända stilar att uteslutas från den resulterande HTML-filen.

Följande skärmbild visar oanvända stilar i HTML-filen som kommer att tas bort genom att ange värdet för [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) till **Sant**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Följande kodexempel demonstrerar borttagning av oanvända stilar under konvertering från Excel till HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
