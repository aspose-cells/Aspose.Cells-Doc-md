---
title: Bestäm vilken axel som finns i diagrammet
description: Lär dig hur man avgör vilken axel som finns i ett diagram skapat med Aspose.Cells för Python via .NET. Vår guide hjälper dig att förstå hur man identifierar och får åtkomst till de olika axlarna i ett diagram, inklusive kategori , värde och sekundära axlar.
keywords: Aspose.Cells för Python via .NET, diagram, axel, existens, kategori, värde, sekundär.
type: docs
weight: 140
url: /sv/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Ibland behöver användaren veta om en särskild axel finns i diagrammet. Till exempel vill han veta om det finns en sekundär värdeaxel i diagrammet eller inte. Vissa diagram som tartdiagram, uppdelat tårtordiagram, sammanfogat tårtordiagram, tårt- stapeldiagram, 3D-tartdiagram, 3D-uppdelat tårtordiagram, ringdiagram, uppdelat ringdiagram, etc. har inte en axel.

Aspose.Cells för Python via .NET tillhandahåller [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) metod för att avgöra om diagrammet har en viss axel eller inte.

{{% /alert %}}

Följande exempelkodvisar användningen av [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) för att avgöra om det provisoriska diagrammet har primära och sekundära kategori- och värdeaxlar.

## C#-kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Konsolutdata som genereras av exempelkoden

Konsolens utmatning av koden visas nedan, vilket visar true för primär kategori- och värdeaxel och false för sekundär kategori- och värdeaxel.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
