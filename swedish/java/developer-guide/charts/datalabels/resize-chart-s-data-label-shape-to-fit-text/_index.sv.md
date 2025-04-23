---
title: Ändra diagrammets datamärkenes form för att passa texten
type: docs
weight: 190
url: /sv/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

Excel-programmet tillhandahåller alternativet **Ändra storlek på formen så att texten passar** för diagrammets datamarkörer för att öka storleken på formen så att texten passar inuti den. Detta alternativ kan nås i Excel-gränssnittet genom att välja någon av datamarkörerna i diagrammet. Högerklicka och välj **Formatera datamarkörer**-menyn. På fliken **Storlek och egenskaper** expanderar **Uppställning** för att avslöja relaterade egenskaper inklusive alternativet **Ändra storlek på formen så att texten passar**.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Ändra diagrammets datamärkesform för att passa texten**

För att efterlikna Excels funktion att ändra datamärkesformen för att passa texten har Aspose.Cells API: er exponerat egenskapen av booleskt typ [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText). Följande kod visar det enkla användningsscenario av [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText).

Diagrammet ser ut så här innan koden exekveras.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Diagrammet ser ut så här efter att koden exekveras.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
{{< app/cells/assistant language="java" >}}
