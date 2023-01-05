---
title: Rotera text med form inuti kalkylbladet
type: docs
weight: 1300
url: /sv/net/rotate-text-with-shape-inside-the-worksheet/
---
## **Möjliga användningsscenarier**

Du kan lägga till text i vilken form som helst med Microsoft Excel. Om du lägger till form med den mycket gamla Microsoft Excel 2003, kommer texten inte att rotera med formen. Men om du lägger till form med nyare versioner av Microsoft Excel, t.ex. 2007, 2010, 2013 eller 2016, etc. kommer texten att rotera med form. Du kan styra om texten ska rotera med formen eller inte med hjälp av[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) fast egendom. Standardvärdet för den är**Sann**vilket betyder att text kommer att rotera med form men om du ställer in den som**falsk**, då kommer inte texten att rotera med formen.

## **Rotera text med form inuti kalkylbladet**

 Följande exempelkod laddar[exempel på Excel-fil](64716896.xlsx) som har en triangelform och dess text roterar med formen. Om du öppnar exemplet på Excel-filen i Microsoft Excel och roterar triangelformen kommer texten också att rotera med den. Koden ställer sedan in[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) egendom som**falsk** och sparar den som[utdata Excel-fil](64716897.xlsx). Om du nu öppnar den utgående Excel-filen i Microsoft Excel och roterar triangelformen, kommer texten inte att rotera med den. Se följande skärmdump som visar effekten av koden på exempel på Excel-fil för en referens.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
