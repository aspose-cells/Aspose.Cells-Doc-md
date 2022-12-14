---
title: Определите, какая ось существует в диаграмме
type: docs
weight: 140
url: /ru/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Иногда пользователю необходимо знать, существует ли на диаграмме определенная ось. Например, он хочет знать, существует ли внутри диаграммы вторичная ось значений. Некоторые диаграммы, такие как Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded и т. д., не имеют оси.

 Aspose.Cells предоставляет[**Chart.HasAxis (AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) метод, чтобы определить, имеет ли диаграмма определенную ось или нет.

{{% /alert %}}

 Следующий пример кода демонстрирует использование[**Chart.HasAxis (AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)чтобы определить, есть ли в образце диаграммы первичная и вторичная категории и оси значений.

## C# код, чтобы определить, какая ось существует в диаграмме

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Консольный вывод, сгенерированный примером кода

Ниже показан консольный вывод кода, в котором отображается true для основной категории и оси значений и false для вторичной категории и оси значений.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
