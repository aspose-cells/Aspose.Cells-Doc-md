---
title: Bestäm vilken axel som finns i diagrammet
type: docs
weight: 130
url: /sv/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Ibland behöver användaren veta om en viss axel finns i diagrammet. Till exempel vill han veta om en sekundär värdeaxel finns i diagrammet eller inte. Vissa diagram som Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded etc. har ingen axel.

 Aspose.Cells tillhandahåller[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) metod för att avgöra om diagrammet har en viss axel eller inte.

{{% /alert %}}

## Bestäm vilken axel som finns i diagrammet

Följande skärmdump visar ett diagram som endast har den primära kategorin och värdeaxeln. Den har ingen sekundär kategori och värdeaxel.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

 Följande exempelkod visar användningen av[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)för att avgöra om provdiagrammet har primär och sekundär kategori och värdeaxel. Konsolutmatningen av koden har visats nedan som visar sant för primär kategori och värdeaxel och falskt för sekundär kategori och värdeaxel.

### Java-kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Konsolutdata genererad av exempelkoden

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
