---
title: Определите, какая ось существует на диаграмме.
description: Узнайте, как определить, какая ось существует на диаграмме, созданной с помощью Aspose.Cells for .NET. Наше руководство поможет вам понять, как идентифицировать и получить доступ к различным осям на диаграмме, включая категории, значения и вторичные оси.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /ru/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Иногда пользователю необходимо знать, существует ли определенная ось на диаграмме. Например, он хочет знать, существует ли на диаграмме вторичная ось значений или нет. Некоторые диаграммы, такие как Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded и т. д., не имеют оси.

 Aspose.Cells обеспечивает[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) метод, позволяющий определить, имеет ли диаграмма определенную ось или нет.

{{% /alert %}}

 В следующем примере кода показано использование[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)чтобы определить, имеет ли образец диаграммы первичную и вторичную категорию и ось значений.

##  Код C# для определения того, какая ось существует на диаграмме

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Вывод консоли, созданный примером кода

Ниже показан консольный вывод кода, который отображает true для основной категории и оси значений и false для вторичной категории и оси значений.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
