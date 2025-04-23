---
title: Hitta typ av X och Y värden för punkter i diagramserier
description: Lär dig hur du bestämmer typen av X och Y värden i diagramseriepunkter med hjälp av Aspose.Cells for .NET. Vår guide kommer att förklara de olika typerna av datavärden och visa dig hur du får åtkomst till dem och arbetar med dem i dina diagram.
keywords: Aspose.Cells for .NET, diagram, X värden, Y värden, datatyper, åtkomst, arbeta med, diagramserie.
type: docs
weight: 150
url: /sv/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**
Ibland vill du veta typen av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells tillhandahåller egenskaperna ChartPoint.XValueType och ChartPoint.YValueType som kan användas för detta ändamål. Observera att du måste anropa Chart.Calculate() metoden innan du effektivt kan använda dessa egenskaper.
## **Hitta typ av X- och Y-värden för punkter i diagramserier**
Följande kodexempel laddar den [provsökta Excel-filen](64716905.xlsx) och får åtkomst till den första diagrammet i den första kalkylbladet. Sedan anropas Chart.Calculate()-metoden och typen av X- och Y-värden för den första diagrampunkten hittas och skrivs ut på konsolen. Se konsoloutputen nedan som referens.

## **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
