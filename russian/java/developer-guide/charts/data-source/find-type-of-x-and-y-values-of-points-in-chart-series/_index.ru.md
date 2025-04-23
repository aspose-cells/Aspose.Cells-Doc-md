---
title: Найдите тип значений X и Y точек в серии графика
type: docs
weight: 110
url: /ru/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Возможные сценарии использования**

Иногда вы хотите узнать тип значений X и Y точек графика в серии. Aspose.Cells предоставляет свойства [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) и [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType), которые могут использоваться для этой цели. Пожалуйста, обратите внимание, что вам придется вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) прежде чем вы сможете эффективно использовать эти свойства.

## **Найдите тип значений X и Y точек в серии графика**

Приведенный ниже образец кода загружает [образец Excel-файла](64716920.xlsx) и получает доступ к первой диаграмме в первом листе. Затем он вызывает метод [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) и находит тип значений X и Y первой точки диаграммы и печатает их в консоль. См. приведенный ниже вывод консоли для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
