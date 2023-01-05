---
title: Определите, какая ось существует в диаграмме
type: docs
weight: 130
url: /ru/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

Иногда пользователю необходимо знать, существует ли на диаграмме определенная ось. Например, он хочет знать, существует ли внутри диаграммы вторичная ось значений. Некоторые диаграммы, такие как Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded и т. д., не имеют оси.

 Aspose.Cells предоставляет[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) метод, чтобы определить, имеет ли диаграмма определенную ось или нет.

{{% /alert %}}

## Определите, какая ось существует в диаграмме

На следующем снимке экрана показана диаграмма, которая имеет только основную категорию и ось значений. У него нет вторичной категории и оси ценностей.

![дело:изображение_альтернативный_текст](determine-which-axis-exists-in-the-chart_1.png)

 Следующий пример кода демонстрирует использование[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)), чтобы определить, есть ли в образце диаграммы первичная и вторичная категории и оси значений. Ниже показан консольный вывод кода, в котором отображается true для основной категории и оси значений и false для вторичной категории и оси значений.

### Код Java для определения того, какие оси существуют на диаграмме

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Консольный вывод, сгенерированный примером кода

Вот консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
