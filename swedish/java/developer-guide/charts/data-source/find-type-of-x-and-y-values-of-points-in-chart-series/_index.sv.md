---
title: Hitta typ av X- och Y-värden för poäng i diagramserier
type: docs
weight: 110
url: /sv/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Möjliga användningsscenarier**

Ibland vill du veta vilken typ av X- och Y-värden för diagrampunkter i en serie. Aspose.Cells tillhandahåller[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)och[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)egenskaper som kan användas för detta ändamål. Observera att du måste ringa[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) innan du kunde använda dessa egenskaper effektivt.

## **Hitta typ av X- och Y-värden för poäng i diagramserier**

Följande exempelkod laddar[exempel på Excel-fil](64716920.xlsx)och kommer åt det första diagrammet i det första kalkylbladet. Den kallar sedan[**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()metod och hittar typen av X- och Y-värden för den första diagrampunkten och skriver ut dem på konsolen. Se konsolutgången nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
