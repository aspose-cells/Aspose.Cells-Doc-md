---
title: Bestäm vilken axel som finns i diagrammet
description: Lär dig hur du bestämmer vilken axel som finns i ett diagram som skapats med Aspose.Cells for .NET. Vår guide hjälper dig att förstå hur du identifierar och får åtkomst till de olika axlarna i ett diagram, inklusive kategori , värde och sekundära axlar.
keywords: Aspose.Cells for .NET, diagram, axel, existens, kategori, värde, sekundär.
type: docs
weight: 140
url: /sv/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Ibland behöver användaren veta om en särskild axel finns i diagrammet. Till exempel vill han veta om det finns en sekundär värdeaxel i diagrammet eller inte. Vissa diagram som tartdiagram, uppdelat tårtordiagram, sammanfogat tårtordiagram, tårt- stapeldiagram, 3D-tartdiagram, 3D-uppdelat tårtordiagram, ringdiagram, uppdelat ringdiagram, etc. har inte en axel.

Aspose.Cells tillhandahåller [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) metod för att avgöra om diagrammet har en specifik axel eller inte.

{{% /alert %}}

Följande exempelkodvisar användningen av [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) för att avgöra om det provisoriska diagrammet har primära och sekundära kategori- och värdeaxlar.

## C#-kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Konsolutdata som genereras av exempelkoden

Konsolens utmatning av koden visas nedan, vilket visar true för primär kategori- och värdeaxel och false för sekundär kategori- och värdeaxel.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
