---
title: Ställ in formtypen för datamärken i diagrammet med Golang via C++
linktitle: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in datapunktetikettens formtyp i diagram med Aspose.Cells for C++. Vår guide förklarar de olika tillgängliga formtyperna och visar hur du väljer rätt form för att förbättra presentationen och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, diagram, datapunktetiketter, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datapunktetiketter i diagrammet med egenskapen `DataLabels.ShapeType`. Den tar värdet från `DataLabelShapeType`-enumerationen och ändrar formtypen för datapunkter därefter. Några av dess värden är:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**
Följande exempel ändrar formtypen för datalabels i diagrammet till `DataLabelShapeType.WedgeEllipseCallout`. Se gärna [exempel-Excel-filen](60489778.xlsx) som används i denna kod och den [utdata-Excel file](60489779.xlsx) som genereras av den. Skärmbilden visar hur koden påverkar exempel-Excel-filen. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
