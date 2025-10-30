---
title: Bestäm vilken axel som finns i diagrammet med Golang via C++
description: Lär dig hur du identifierar vilken axel som finns i ett diagram skapat med Aspose.Cells for C++. Vår guide hjälper dig att förstå hur man identifierar och får tillgång till de olika axlarna i ett diagram, inklusive kategori , värde och sekundära axlar.
keywords: Aspose.Cells for C++, diagram, axel,_exists, kategori, värde, sekundär.
type: docs
weight: 140
url: /sv/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Ibland behöver användaren veta om en särskild axel finns i diagrammet. Till exempel vill han veta om det finns en sekundär värdeaxel i diagrammet eller inte. Vissa diagram som tartdiagram, uppdelat tårtordiagram, sammanfogat tårtordiagram, tårt- stapeldiagram, 3D-tartdiagram, 3D-uppdelat tårtordiagram, ringdiagram, uppdelat ringdiagram, etc. har inte en axel.

Aspose.Cells tillhandahåller [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) metod för att avgöra om diagrammet har en specifik axel eller inte.

{{% /alert %}}

 Följande kodexempel demonstrerar användningen av [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) för att avgöra om diagrammet har primär och sekundär kategori- och värdeaxel.

## C++-kod för att avgöra vilken axel som finns i diagrammet

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Konsolutdata som genereras av exempelkoden

Konsolens utmatning av koden visas nedan, vilket visar true för primär kategori- och värdeaxel och false för sekundär kategori- och värdeaxel.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
