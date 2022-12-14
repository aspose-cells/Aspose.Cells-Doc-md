---
title: Skaffa arbetsblad av diagrammet
type: docs
weight: 80
url: /sv/java/get-worksheet-of-the-chart/
---
{{% alert color="primary" %}}

 Ibland vill du komma åt ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) egenskap som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

## Exempel

 Följande exempel visar hur du använder[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet) fast egendom. Koden skriver först ut namnet på kalkylbladet och kommer sedan åt det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen med hjälp av[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)fast egendom.

### Java-kod för att komma åt arbetsbladet i diagrammet

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### Konsolutdata genererad av exempelkoden

Nedan är konsolutgången som exempelkoden resulterar i. Som du kan se skriver den ut samma kalkylbladsnamn båda gångerna.

{{< highlight "java" >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
