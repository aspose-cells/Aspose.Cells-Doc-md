---
title: Hämta kalkylbladet för diagrammet
description: Lär dig hur du hämtar arbetsbladet associerat med ett Excel diagram med hjälp av Aspose.Cells for .NET. Vår guide kommer att visa dig hur du får tillgång till arbetsbladet och utför operationer på det för att manipulera diagrammets underliggande data.
keywords: Aspose.Cells for .NET, Excel diagram, arbetsblad, datamanipulering, underliggande data, operationer.
type: docs
weight: 1000
url: /sv/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du komma åt ett kalkylblad från ett diagrams referens. Aspose.Cells tillhandahåller egenskapen [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder egenskapen [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet). Koden skriver först ut namnet på kalkylbladet, får sedan åtkomst till det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen, med hjälp av egenskapen [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
