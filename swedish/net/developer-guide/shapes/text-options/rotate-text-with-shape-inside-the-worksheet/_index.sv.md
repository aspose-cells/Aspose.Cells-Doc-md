---
title: Rotera text med Shape i kalkylbladet
type: docs
weight: 1300
url: /sv/net/rotate-text-with-shape-inside-the-worksheet/
---

## **Möjliga användningsscenario**

Du kan lägga till text inuti vilken form som helst med Microsoft Excel. Om du lägger till en form med den mycket gamla versionen av Microsoft Excel 2003 kommer inte texten att rotera med formen. Men om du lägger till en form med nyare versioner av Microsoft Excel t.ex. 2007, 2010, 2013 eller 2016, osv. kommer texten att rotera med formen. Du kan kontrollera om texten ska rotera med formen eller inte med hjälp av egenskapen [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape). Standardvärdet är **true** vilket innebär att texten kommer att rotera med formen, men om du ställer in det som **false** kommer inte texten att rotera med formen.

## **Rotera text med Shape i kalkylbladet**

Följande kodexempel laddar den [provExcel-fil](64716896.xlsx) som har en triangelform och dess text roterar med formen. Om du öppnar provExcel-filen i Microsoft Excel och roterar triangeln kommer texten också att rotera med den. Koden ställer sedan in egenskapen [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) som **false** och sparar den som [utdataExcel-fil](64716897.xlsx). Om du nu öppnar utdataExcel-filen i Microsoft Excel och roterar triangeln kommer texten inte att rotera med den. Se nedanstående skärmbild som visar effekten av koden på provExcel-filen som referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
