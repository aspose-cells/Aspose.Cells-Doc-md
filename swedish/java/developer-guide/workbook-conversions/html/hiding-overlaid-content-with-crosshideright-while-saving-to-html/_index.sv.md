---
title: Dölja överlagt innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML kan du ange olika korssträngstyper för cellsnören. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel men när du ändrar [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) till [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) döljer det all cellsträng som är överlagd eller överlappande med cellsnöret till höger om cellen.

## **Dölja överlagt innehåll med CrossHideRight vid sparande till HTML**

Följande provkod laddar in den [exempel Excel-filen](64716916.xlsx) och sparar den till [utdata-HTML](64716915.zip) efter att ha ställt in [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) som [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Skärmbilden förklarar hur [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) påverkar utdata-HTML från standardutdata.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
