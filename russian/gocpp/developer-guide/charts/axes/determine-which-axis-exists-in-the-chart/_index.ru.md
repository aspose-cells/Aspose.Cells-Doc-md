---
title: Определить, какая ось существует в диаграмме, с помощью Golang через C++
description: Узнайте, как определить, какая ось существует в диаграмме, созданной с помощью Aspose.Cells for C++. Наше руководство поможет вам понять, как идентифицировать и получать доступ к различным осям в диаграмме, включая категориальные, значенческие и вторичные оси.
keywords: Aspose.Cells for C++, диаграмма, ось, наличие, категория, значение, вторичная.
type: docs
weight: 140
url: /ru/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод {0} для определения, есть ли в диаграмме определенная ось или нет.

В следующем образце кода демонстрируется использование [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) для определения, имеет ли образецная диаграмма основную и вторичную категориальные и числовые оси.

{{% /alert %}}

Следующий пример кода демонстрирует использование [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) для определения наличия в образцовой диаграмме Первичной и Вторичной Категориальной и Значительной Оси.

## Код C++ для определения существования оси в диаграмме

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Консольный вывод, сгенерированный образцовым кодом

Консольный вывод кода показан ниже, отображающий результат true для основной категории и оси значений и false для вторичной категории и оси значений.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
