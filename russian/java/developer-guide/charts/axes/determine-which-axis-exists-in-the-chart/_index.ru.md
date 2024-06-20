---
title: Определите, какая ось существует в диаграмме
type: docs
weight: 130
url: /ru/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Иногда пользователю необходимо знать, существует ли определенная ось на диаграмме. Например, он хочет знать, существует ли в диаграмме вторичная ось для значений или нет. Некоторые диаграммы, такие как круговая, взорванная круговая, комбинированная круговая, круговая с колонками, 3D-круговая, взорванная 3D-круговая, кольцевая, взорванная кольцевая и т. д., не имеют оси.

В следующем образце кода демонстрируется использование [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) для определения, имеет ли образецная диаграмма основную и вторичную категориальные и числовые оси.

{{% /alert %}}

## Определение существующих осей на диаграмме

На следующем снимке экрана показана диаграмма, в которой присутствуют только первичная ось категорий и значений. Отсутствуют какие-либо вторичная ось категорий и значений.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

Приведенный ниже образец кода демонстрирует использование [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) для определения, если у образца диаграммы есть основные и вторичные категории и оси значений. Результат работы кода отображается ниже на экране, который показывает true для основной категории и оси значений, и false - для вторичной категории и оси значений.

### Код на Java для определения существующих осей на диаграмме

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Вывод консоли, сгенерированный примерным кодом

Вот вывод консоли из приведенного выше примерного кода.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
