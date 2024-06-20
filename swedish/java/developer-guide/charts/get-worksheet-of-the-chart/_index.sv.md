---
title: Hämta kalkylbladet för diagrammet
type: docs
weight: 80
url: /sv/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du komma åt ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller egenskapen [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

## Exempel

Följande exempel visar hur man använder egenskapen [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet). Koden skriver först ut namnet på kalkylbladet, får sedan åtkomst till det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen, med hjälp av egenskapen [**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet).

### Java-kod för att komma åt kalkylbladet för diagrammet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Konsoloutput som genereras av provkoden

Nedan finns konsoloutputen som provkoden resulterar i. Som du kan se, skriver den ut samma kalkylbladsnamn båda gångerna.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
