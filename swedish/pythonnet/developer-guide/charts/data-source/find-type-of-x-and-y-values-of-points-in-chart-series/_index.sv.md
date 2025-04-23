---
title: Hitta typ av X och Y värden för punkter i diagramserier
description: Lär dig hur du avgör typen av X och Y värden i diagramseriernas punkter med Aspose.Cells för Python via .NET. Vår guide förklarar de olika datatyperna och visar hur du kommer åt och arbetar med dem i dina diagram.
keywords: Aspose.Cells för Python via .NET, diagram, X värden, Y värden, datatyper, åtkomst, arbete med, diagramserie.
type: docs
weight: 150
url: /sv/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**
Ibland vill du veta typen av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells för Python via .NET tillhandahåller [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) och [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/)-egenskaper som kan användas för detta ändamål. Observera att du måste anropa [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)-metoden innan du kan använda dessa egenskaper effektivt.

## **Hitta typ av X- och Y-värden för punkter i diagramserier**
Följande exempelkod laddar filen [exempel Excel-fil](64716905.xlsx) och får åtkomst till det första diagrammet i det första arbetsbladet. Den anropar sedan [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#)-metoden, hittar typen av X- och Y-värden för den första diagrampunkten och skriver ut dem i konsolen. Se konsolutmatningen nedan som referens.

## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Konsoloutput**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
