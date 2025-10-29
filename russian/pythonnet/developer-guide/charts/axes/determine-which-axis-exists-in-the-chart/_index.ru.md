---
title: Определите, какая ось существует в диаграмме
description: Узнайте, как определить, какая ось существует на созданной с помощью Aspose.Cells для Python via .NET диаграмме. Наше руководство поможет вам понять, как идентифицировать и получать доступ к различным осям в диаграмме, включая категориальные, значений и вторичные оси.
keywords: Aspose.Cells для Python via .NET, диаграмма, ось, наличие, категория, значение, вторичная.
type: docs
weight: 140
url: /ru/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод {0} для определения, есть ли в диаграмме определенная ось или нет.

Aspose.Cells для Python via .NET предоставляет метод [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) для определения, есть ли у диаграммы определенная ось или нет.

{{% /alert %}}

## Код C#, чтобы определить, какие оси существуют в диаграмме

Вывод консоли кода показан ниже, что отображает true для основной оси категорий и значений и false для вторичной оси категорий и значений.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Консольный вывод, сгенерированный образцовым кодом

Консольный вывод кода показан ниже, отображающий результат true для основной категории и оси значений и false для вторичной категории и оси значений.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
