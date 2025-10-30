---
title: Dölj överlagrat innehåll med CrossHideRight vid sparning till HTML med Golang via C++
linktitle: Dölja överlagt innehåll med CrossHideRight medan du sparar till HTML
type: docs
weight: 100
url: /sv/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Använd CrossHideRight med Aspose.Cells i C++ för att dölja överlagrat innehåll vid sparande till HTML.
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML kan du specificera olika kors-typer för cellsträngar. Som standard genererar Aspose.Cells HTML enligt Microsoft Excel, men när du ändrar kors-typen till [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype) döljs alla strängar till höger om cellen som är överlagrade eller overlapping med cellsträngen.

## **Dölja överlagt innehåll med CrossHideRight vid sparning till Html**

Följande exempel kod laddar [exempel-Excelfilen](64716894.xlsx) och sparar den till [utdata-HTML](64716893.zip) efter att ha ställt in [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) som [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Skärmbilden förklarar hur [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) påverkar utdata HTML från standardutgången.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
