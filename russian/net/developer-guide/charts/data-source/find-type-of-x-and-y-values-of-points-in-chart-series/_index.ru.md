---
title: Найдите тип значений X и Y точек в серии диаграмм
type: docs
weight: 150
url: /ru/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Возможные сценарии использования**
Иногда вам нужно знать тип значений X и Y точек диаграммы в серии. Aspose.Cells предоставляет свойства ChartPoint.XValueType и ChartPoint.YValueType, которые можно использовать для этой цели. Обратите внимание, что вам нужно будет вызвать метод Chart.Calculate(), прежде чем вы сможете эффективно использовать эти свойства.
## **Найдите тип значений X и Y точек в серии диаграмм**
 Следующий пример кода загружает[образец файла Excel](64716905.xlsx) и обращается к первой диаграмме внутри первого рабочего листа. Затем он вызывает метод Chart.Calculate() и находит тип значений X и Y первой точки диаграммы и выводит их на консоль. Для справки см. вывод консоли, показанный ниже.
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Консольный вывод**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
