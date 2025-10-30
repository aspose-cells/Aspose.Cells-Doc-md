---
title: Rotera text med form inom kalkbladet med Golang via C++
linktitle: Rotera Text med Form
type: docs
weight: 1300
url: /sv/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lär dig hur man kontrollerar textrotation med former i Excel ark med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Du kan lägga till text inuti vilken form som helst med Microsoft Excel. Om du lägger till en form med den mycket gamla Microsoft Excel 2003, kommer texten inte att rotera med formen. Men om du lägger till en form med nyare versioner av Microsoft Excel, såsom 2007, 2010, 2013 eller 2016, kommer texten att rotera med formen. Du kan kontrollera om texten ska rotera med formen eller inte med hjälp av [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)-egenskapen. Standardvärdet för denna egenskap är **true**, vilket innebär att texten roterar med formen. Om du ställer in det till **false**, roterar inte texten med formen.

## **Rotera text med Shape i kalkylbladet**

Följande exempel laddar [exempel-Excel-filen](64716896.xlsx) som innehåller en triangel och dess text roterar med formen. Om du öppnar exempel-Excel-filen i Microsoft Excel och roterar triangelformen, kommer texten också att rotera med den. Koden ställer sedan in [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)-egenskapen till **false** och sparar den som [utdata Excel-fil](64716897.xlsx). Om du nu öppnar utdatafilen i Excel och roterar triangelformen kommer inte texten att rotera med den. Se skärmskärmbilder nedan som visar effekten av koden på exempel-Excel-filen för referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
