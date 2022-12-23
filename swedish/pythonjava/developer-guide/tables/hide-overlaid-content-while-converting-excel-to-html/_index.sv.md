---
title: Dölj överlagrat innehåll när du konverterar Excel till HTML
type: docs
weight: 40
url: /sv/python-java/hide-overlaid-content-while-converting-excel-to/
---
## **Dölj överlagrat innehåll när du konverterar Excel till HTML**
När du sparar din Excel-fil till HTML kan du ange olika korstyper för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel men när du ändrar[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)till[KORSA_DÖLJ_RÄTT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)sedan döljer den alla strängar på höger sida av cellen som är överlagrade eller överlappande med cellsträngen.

Följande exempelkod laddar[exempel på Excel-fil](sampleHidingOverlaidContentWithCrossHideRight.xlsx)och sparar den till[utgång HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip)efter att ha ställt in[HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType)som[KORSA_DÖLJ_RÄTT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Skärmdumpen förklarar hur[KORSA_DÖLJ_RÄTT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT)påverkar utgången HTML från standardutgången.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
