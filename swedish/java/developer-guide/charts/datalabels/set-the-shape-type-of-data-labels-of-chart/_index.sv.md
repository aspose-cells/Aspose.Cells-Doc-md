---
title: Ställ in datamärkenas formtyp i diagrammet
type: docs
weight: 70
url: /sv/java/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**

Du kan ändra formtypen på diagrammets datamarkörer med [**DataLabels.ShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShapeType) egenskapen. Den tar värdet av [**DataLabelShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/DataLabelShapeType) uppräkningen och ändrar formtypen på diagrammets datamarkörer därefter. Några av dess värden är

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**

Följande exempelkod ändrar formtypen på diagrammets datamarkörer till [**DataLabelShapeType.WEDGE_ELLIPSE_CALLOUT**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabelshapetype#WEDGE_ELLIPSE_CALLOUT). Se den [sample Excel file](60489794.xlsx) som används i den här koden och den [output Excel file](60489793.xlsx) som genererats av den. Skärmdumpen visar effekten av koden på den provisoriska Excel-filen.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-SetShapeTypeOfDataLabelsOfChart.java" >}}
