---
title: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in formtypen för datamärken i diagram med hjälp av Aspose.Cells for .NET. Vår guide kommer att förklara de olika formtyper som är tillgängliga och visa dig hur du väljer den lämpliga formen för dina datamärken för att förbättra presentationen och användbarheten av dina diagram.
keywords: Aspose.Cells for .NET, diagram, datamärken, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/net/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datamärken i diagrammet med egenskapen DataLabels.ShapeType. Den tar värdet av DataLabelShapeType-uppräkningen och ändrar formtypen för datamärkena därefter. Några av dess värden är

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Ställ in datamärkenas formtyp i diagram**
Följande kod ändrar formtypen för datamärkena i diagrammet till DataLabelShapeType.WedgeEllipseCallout. Se den [exempel Excel-filen](60489778.xlsx) som används i denna kod och den [utdata Excel-filen](60489779.xlsx) som genereras av den. Skärmdumpen visar effekten av koden på den exempel Excel-filen. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
