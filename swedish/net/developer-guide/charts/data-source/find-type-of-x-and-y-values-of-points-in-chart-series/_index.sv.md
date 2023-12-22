---
title: Hitta typ av X- och Y-värden för poäng i diagramserier
description: Lär dig hur du bestämmer typen av X- och Y-värden i diagramseriepunkter med hjälp av Aspose.Cells for .NET. Vår guide kommer att förklara de olika typerna av datavärden och visa dig hur du kommer åt och arbetar med dem i dina diagram.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /sv/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Möjliga användningsscenarier**
Ibland vill du veta vilken typ av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells tillhandahåller egenskaperna ChartPoint.XValueType och ChartPoint.YValueType som kan användas för detta ändamål. Observera att du måste anropa metoden Chart.Calculate() innan du kan använda dessa egenskaper effektivt.
##  **Hitta typ av X- och Y-värden för poäng i diagramserier**
 Följande exempelkod laddar[exempel på Excel-fil](64716905.xlsx) och kommer åt det första diagrammet i det första kalkylbladet. Den anropar sedan metoden Chart.Calculate() och hittar typen av X- och Y-värden för första diagrampunkten och skriver ut dem på konsolen. Se konsolutgången nedan för en referens.
##  **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Konsolutgång**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
