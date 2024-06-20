---
title: Dölj överlagt innehåll vid konvertering av Excel till HTML
type: docs
weight: 40
url: /sv/python-java/hide-overlaid-content-while-converting-excel-to/
---

## **Dölj överlagt innehåll vid konvertering av Excel till HTML**
När du sparar din Excel-fil till HTML kan du ange olika korsnings typer för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel men när du ändrar [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) till [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) så döljer den alla strängar till höger om cellen som är överlagda eller överlappar med cellsträngen.

Följande exempelkod laddar [prov Excel-filen](sampleHidingOverlaidContentWithCrossHideRight.xlsx) och sparar den till [utförlig HTML](HTML-outputHidingOverlaidContentWithCrossHideRight.zip) efter att ha ställt in [HtmlSaveOptions.HtmlCrossStringType](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#HtmlCrossStringType) som [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT). Skärmbilden förklarar hur [CROSS_HIDE_RIGHT](https://reference.aspose.com/cells/python/asposecells.api/htmlcrosstype#CROSS_HIDE_RIGHT) påverkar utdata-HTML från standardutdata.

![todo:image_alt_text](Hiding-Overlaid-Content-With-CrossHideRight.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
