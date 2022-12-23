---
title: Anpassade segment- eller sektorfärger i cirkeldiagram
type: docs
weight: 30
url: /sv/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Den här artikeln förklarar hur du lägger till anpassade färger till cirkeldiagramsegment/sektorer. Som standard använder cirkeldiagram standardmallen Microsoft Excel. För att använda andra färger är det möjligt att omdefiniera färgerna i diagrammet.

{{% /alert %}}

Så här ställer du in den anpassade färgen för ett cirkeldiagrams enskilda segment eller sektorer:

1.  Få tillgång till[**Serier**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) föremål[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Tilldela en valfri färg med hjälp av[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)metod.

Den här artikeln förklarar också hur du ställer in:

- Ett diagrams kategoridata.
- En diagramtitel kopplad till en cell.
- Teckensnittsinställningarna för diagramtiteln.
- Legendens position.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) är inte specifik för cirkeldiagram men kan användas för alla typer av diagram.

{{% /alert %}}

**Anpassade segmentfärger i cirkeldiagrammet**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
