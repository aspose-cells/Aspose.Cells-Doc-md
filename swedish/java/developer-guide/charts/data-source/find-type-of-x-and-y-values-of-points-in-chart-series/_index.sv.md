---
title: Hitta typ av X och Y värden för punkter i diagramserier
type: docs
weight: 110
url: /sv/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Möjliga användningsscenario**

Ibland vill du veta typen av X- och Y-värden för diagrampunkterna i en serie. Aspose.Cells tillhandahåller egenskaperna [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) och [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) som kan användas för detta ändamål. Observera att du måste anropa metoden [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) innan du effektivt kan använda dessa egenskaper.

## **Hitta typ av X- och Y-värden för punkter i diagramserier**

Följande exempelkod laddar in [sample Excel file](64716920.xlsx) och får åtkomst till det första diagrammet i den första kalkylbladet. Sedan anropas metoden [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) och tar reda på typen av X- och Y-värden för första diagrampunkten och skriver ut dem i konsolen. Se nedan för en referens till utskriften i konsolen.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsoloutput**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
