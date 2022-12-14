---
title: Döljer överlagrat innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Möjliga användningsscenarier**

När du sparar din Excel-fil i HTML kan du ange olika korstyper för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel men när du ändrar[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)till[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)sedan döljer den alla strängar på höger sida av cellen som är överlagrade eller överlappande med cellsträngen.

## **Döljer överlagrat innehåll med CrossHideRight medan du sparar till HTML**

Följande exempelkod laddar[exempel på Excel-fil](64716916.xlsx)och sparar den till[mata ut HTML](64716915.zip)efter att ha ställt in[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)som[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Skärmdumpen förklarar hur[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)påverkar HTML-utdata från standardutdata.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
