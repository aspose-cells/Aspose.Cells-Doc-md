---
title: Få ekvationstext av diagramtrendlinje med Golang via C++
linktitle: Trendlinjer
description: Lär dig hur du använder Aspose.Cells for C++ för att hämta ekvationstexten för en trendlinje i ett diagram skapat i Microsoft Excel. Vår guide kommer att visa hur du kommer åt och extraherar ekvationen för trendlinjen för vidare analys eller visning.
keywords: Aspose.Cells for C++, Diagramtrendlinje, Ekvationstext, Microsoft Excel, Dataanalys, Visning.
type: docs
weight: 110
url: /sv/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Du kan hämta ekvations text av diagramtrendlinje med Aspose.Cells. Aspose.Cells tillhandahåller egenskapen [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) som returnerar ekvations texten av diagramtrendlinjen. För att använda denna egenskap måste du först anropa metoden [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Följande skärm visar diagrammet med en trendlinje och dess ekvationstext visas i röd färg. Vi kommer att hämta denna text med hjälp av [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) egenskapen i följande kodexempel.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++-kod för att få ekvationstexten av diagramtrendlinjen

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## Utdata genererad av provkoden

Detta är konsoloutputen för ovanstående exempelkod.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
