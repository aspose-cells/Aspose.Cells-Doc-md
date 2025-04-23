---
title: Lägga till anpassade etiketter till datapunkter i diagramserien
type: docs
weight: 380
url: /sv/java/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}} 

Du kan lägga till anpassade etiketter till datapunkterna i diagrammets serie. Aspose.Cells tillhandahåller egenskapen [ChartPoint.getDataLabels().setText()](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) för att lägga till dessa anpassade etiketter. Den här artikeln förklarar hur du använder den här egenskapen för att lägga till anpassade etiketter till datapunkterna i diagrammets serie.

{{% /alert %}} 
## **Lägg till anpassade etiketter till datapunkter i diagramserien**
Följande kod skapar ett spridningsdiagram som är anslutet med linjer med data markörer och lägger sedan till anpassade etiketter till datamarkörerna i diagrammets serie. Varje anpassad etikett visar seriens namn och punktens namn. Du kan använda vilken annan text som helst istället för det. Efter att koden har exekverats skapas följande Excel-fil. Som du kan se inuti diagrammet har varje datapunkt en anpassad etikett.

![todo:image_alt_text](adding-custom-labels-to-data-points-in-the-series-of-the-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddCustomLabelsToDataPoints-AddCustomLabelsToDataPoints.java" >}}
{{< app/cells/assistant language="java" >}}
