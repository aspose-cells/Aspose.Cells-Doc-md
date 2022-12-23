---
title: Найдите тип значений X и Y точек в серии диаграмм
type: docs
weight: 110
url: /ru/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Возможные сценарии использования**

Иногда вам нужно знать тип значений X и Y точек диаграммы в серии. Aspose.Cells предоставляет[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)и[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)свойства, которые можно использовать для этой цели. Обратите внимание, вам придется позвонить[**Диаграмма.рассчитать()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()), прежде чем вы сможете эффективно использовать эти свойства.

## **Найдите тип значений X и Y точек в серии диаграмм**

Следующий пример кода загружает[образец файла Excel](64716920.xlsx)и обращается к первой диаграмме внутри первого рабочего листа. Затем он вызывает[**Диаграмма.рассчитать()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()и находит тип значений X и Y первой точки графика и выводит их на консоль. Для справки см. вывод консоли, показанный ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
