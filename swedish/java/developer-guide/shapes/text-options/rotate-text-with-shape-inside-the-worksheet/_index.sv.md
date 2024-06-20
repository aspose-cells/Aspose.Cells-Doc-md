---
title: Rotera text med Shape i kalkylbladet
type: docs
weight: 110
url: /sv/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Möjliga användningsscenario**

Du kan lägga till text i valfri shape med hjälp av Microsoft Excel. Om du lägger till shape med hjälp av den mycket gamla Microsoft Excel 2003 kommer texten inte att rotera med shape. Men om du lägger till shape med hjälp av nyare versioner av Microsoft Excel, t.ex. 2007, 2010, 2013 eller 2016, kommer texten att rotera med shape. Du kan styra om texten ska rotera med shapen eller inte med hjälp av egenskapen [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). Standardvärdet är **true**, vilket innebär att texten kommer att rotera med shape, men om du ställer in det som **false** kommer texten inte att rotera med shape.

## **Rotera text med Shape i kalkylbladet**

Följande exempelkod laddar in [exempel Excel-filen](64716919.xlsx) som har en triangelform och där texten roterar med shapen. Om du öppnar exemplet Excel-filen i Microsoft Excel och roterar triangelformen kommer texten också att rotera med den. Koden ställer sedan in egenskapen [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) som **false** och sparar den som [utdata Excel-filen](64716917.xlsx). Om du nu öppnar utdata Excel-filen i Microsoft Excel och roterar triangelformen kommer texten inte att rotera med den. Var vänlig och titta på följande skärmbild som visar effekten av koden på exempel Excel-filen för referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
