---
title: Найдите тип значений X и Y точек в серии графика
description: Узнайте, как определить тип X и Y значений в точках серии диаграммы с помощью Aspose.Cells для Python via .NET. Наше руководство объяснит разные типы данных и покажет, как получать к ним доступ и работать с ними в ваших диаграммах.
keywords: Aspose.Cells для Python via .NET, построение графиков, значения X, значения Y, типы данных, доступ, работа с, серии диаграмм.
type: docs
weight: 150
url: /ru/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Возможные сценарии использования**
 Иногда вам нужно узнать тип X и Y значений в точках серии диаграммы. Aspose.Cells для Python via .NET предоставляет свойства [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) и [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/), которые можно использовать для этой цели. Обратите внимание, что перед использованием этих свойств необходимо вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#).

## **Найдите тип значений X и Y точек в серии графика**
 Следующий пример кода загружает [образец Excel файла](64716905.xlsx) и получает доступ к первому графику внутри первого листа. Затем он вызывает метод [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) и определяет тип X и Y значений первой точки графика, выводя их в консоль. Для справки см. пример вывода ниже.

## **Образец кода**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
