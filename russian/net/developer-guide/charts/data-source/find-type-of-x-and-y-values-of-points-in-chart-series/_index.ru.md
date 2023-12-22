---
title: Найдите тип значений X и Y точек в серии диаграмм
description: Узнайте, как определить тип значений X и Y в точках ряда диаграмм, используя Aspose.Cells for .NET. Наше руководство объяснит различные типы значений данных и покажет, как получить к ним доступ и работать с ними в диаграммах.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /ru/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Возможные сценарии использования**
Иногда вам нужно узнать тип значений X и Y точек диаграммы в серии. Aspose.Cells предоставляет свойства ChartPoint.XValueType и ChartPoint.YValueType, которые можно использовать для этой цели. Обратите внимание: вам придется вызвать метод Chart.Calculate(), прежде чем вы сможете эффективно использовать эти свойства.
##  **Найдите тип значений X и Y точек в серии диаграмм**
 Следующий пример кода загружает[образец файла Excel](64716905.xlsx) и получает доступ к первой диаграмме внутри первого листа. Затем он вызывает метод Chart.Calculate(), находит тип значений X и Y первой точки диаграммы и печатает их на консоли. Для справки см. вывод консоли, показанный ниже.
##  **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Консольный вывод**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
