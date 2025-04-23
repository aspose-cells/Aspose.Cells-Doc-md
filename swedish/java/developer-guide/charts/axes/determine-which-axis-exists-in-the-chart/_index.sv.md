---
title: Bestäm vilken axel som finns i diagrammet
type: docs
weight: 130
url: /sv/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Ibland behöver användaren veta om en särskild axel finns i diagrammet. Till exempel vill han veta om en sekundär värdeaxel finns i diagrammet eller inte. Vissa diagram som tårt-, tårtspräckt-, tårtpie-, tårtpie-, tårtstång-, tårt3D-, tårt3Dspräckt-, ringdiagram, ringdiagramspräckt etc. har inte någon axel.

Aspose.Cells tillhandahåller [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) metod för att avgöra om diagrammet har en specifik axel eller inte.

{{% /alert %}}

## Bestäm vilken axel som finns i diagrammet

Nedanstående skärmbild visar ett diagram som bara har primär kategori- och värdeaxel. Det har ingen sekundär kategori- och värdeaxel.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Nedanstående exempelkod visar användningen av [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) för att avgöra om det angivna diagrammet har primär och sekundär kategori- och värdeaxel. Konsolutmatningen av koden har visats nedan, vilket visar true för primär kategori- och värdeaxel och false för sekundär kategori- och värdeaxel.

### Java-kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Konsoloutput som genereras av provkoden

Här är konsolutmatningen för ovanstående exempelkod.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
