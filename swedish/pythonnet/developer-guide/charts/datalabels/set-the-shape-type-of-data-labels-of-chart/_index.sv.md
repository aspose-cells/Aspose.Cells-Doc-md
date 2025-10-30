---
title: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in formen för datamärkningar i diagram med Aspose.Cells för Python via .NET. Vår guide förklarar de olika formen av typer som finns och visar hur du väljer den lämpliga formen för dina datamärkningar för att förbättra presentationen och användbarheten.
keywords: Aspose.Cells för Python via .NET, diagram, datamärkningar, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datamärken i diagrammet med egenskapen DataLabels.ShapeType. Den tar värdet av DataLabelShapeType-uppräkningen och ändrar formtypen för datamärkena därefter. Några av dess värden är

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**
Följande kod ändrar formtypen för datamärkena i diagrammet till DataLabelShapeType.WedgeEllipseCallout. Se den [exempel Excel-filen](60489778.xlsx) som används i denna kod och den [utdata Excel-filen](60489779.xlsx) som genereras av den. Skärmdumpen visar effekten av koden på den exempel Excel-filen. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
{{< app/cells/assistant language="python-net" >}}
