---
title: Hämta kalkylbladet för diagrammet
description: Lär dig hur du hämtar kalkylbladet som är kopplat till ett Excel diagram med Aspose.Cells för Python via .NET. Vår guide visar hur du får tillgång till kalkylbladet och utför operationer på det för att manipulera diagrammets underliggande data.
keywords: Aspose.Cells för Python via .NET, Excel diagram, kalkylblad, datamanipulation, underliggande data, operationer.
type: docs
weight: 1000
url: /sv/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Ibland vill du komma åt ett kalkylblad från ett diagramreferens. Aspose.Cells för Python via .NET erbjuder egenskapen [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) som returnerar referensen till kalkylbladet som innehåller diagrammet.

{{% /alert %}}

Följande exempel visar hur man använder egenskapen [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet). Koden skriver först ut namnet på kalkylbladet, får sedan åtkomst till det första diagrammet på kalkylbladet. Den skriver sedan ut kalkylbladets namn igen, med hjälp av egenskapen [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Nedan är konsolresultatet som exempelkoden leder till. Som du kan se skriver den ut arbetsbladsnamnet samma namn båda gångerna.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
