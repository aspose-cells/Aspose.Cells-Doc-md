---
title: Hitta typ av X och Y värden för punkter i diagramserien med Golang via C++
linktitle: Hitta typ av X och Y värden för punkter i diagramserier
description: Lär dig hur du avgör typen av X och Y värden i diagramseriepunkter med Aspose.Cells for C++. Vår guide förklarar de olika datatyperna och visar hur du får åtkomst till och arbetar med dem i dina diagram.
keywords: Aspose.Cells for C++, diagram, X värden, Y värden, datatyper, åtkomst, arbeten, diagramserier.
type: docs
weight: 150
url: /sv/go-cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**
Ibland vill du veta vilken typ av X- och Y-värden i diagrampunkter i en serie. Aspose.Cells tillhandahåller metoderna `ChartPoint::get_XValueType` och `ChartPoint::get_YValueType` som kan användas för detta ändamål. Observera att du måste anropa `Chart::Calculate()`-metoden innan du kan använda dessa egenskaper effektivt.

## **Hitta typ av X- och Y-värden för punkter i diagramserier**
Följande exempelkod laddar [exempel-Excel-filen](64716905.xlsx) och får tillgång till det första diagrammet i den första arbetsbladet. Den anropar sedan `Chart::Calculate()`-metoden och hittar typen av X- och Y-värden för den första diagrampunkten och skriver ut dem på konsolen. Se konsolutmatningen nedan som en referens.

## **Exempelkod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindTypeOfXAndYValuesOfPointsInChartSeries.go" >}}
## **Konsoloutput**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
