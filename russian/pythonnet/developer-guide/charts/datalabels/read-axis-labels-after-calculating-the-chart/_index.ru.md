---
title: Чтение меток оси после вычисления диаграммы
description: Узнайте, как читать метки оси в Aspose.Cells для Python via .NET после вычисления диаграммы. Наш гид покажет, как получить доступ и извлечь метки оси, включая их форматирование и позиционирование.
keywords: Aspose.Cells для Python via .NET, диаграмма, метки осей, вычисление, чтение, доступ, извлечение, форматирование, позиционирование.
type: docs
weight: 90
url: /ru/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Возможные сценарии использования**

Вы можете прочитать подписи осей вашей диаграммы после вычисления их значений с помощью метода [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/). Для этой цели используйте метод [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts), который вернет список подписей осей.

## **Чтение меток оси после вычисления диаграммы**

Пожалуйста, см. следующий образец кода, который загружает [образец файла Excel](ReadAxisLabels.xlsx) и читает подписи осей категорий диаграммы на первом листе. Затем выводятся значения подписей осей на консоль. См. пример вывода на консоль приведенный ниже в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **Вывод в консоль**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
