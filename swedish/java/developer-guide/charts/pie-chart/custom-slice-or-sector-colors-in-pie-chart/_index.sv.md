---
title: Anpassa skiv eller sektorfärger i cirkeldiagram
type: docs
weight: 30
url: /sv/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Den här artikeln förklarar hur du lägger till anpassade färger till tårtdiagramsegment/sektorer. Som standard använder tårtdiagram Microsoft Excels standardmall. För att använda andra färger är det möjligt att omdefiniera färgerna i diagrammet.

{{% /alert %}}

För att ställa in anpassad färg för ett tårtdiagram individuella segment eller sektorer:

1. Öppna [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)s [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. Tilldela en färg efter eget val med hjälp av [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)-metoden.

Den här artikeln förklarar även hur man ställer in:

- En diagrams kategoridata.
- En diagramtitel länkad till en cell.
- Typsnittsinställningar för diagramtiteln.
- Placeringen av legenden.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) är inte specifik för tårtdiagram men kan användas för alla typer av diagram.

{{% /alert %}}

**Anpassade segmentfärger i tårtdiagram**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
{{< app/cells/assistant language="java" >}}
