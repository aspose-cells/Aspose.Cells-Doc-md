---
title: Получение текста уравнения трендовой линии диаграммы
description: Узнайте, как использовать Aspose.Cells для Python via .NET для получения текста уравнения трендлайна, созданной в Microsoft Excel. Наше руководство покажет, как получить и извлечь уравнение трендлайна для дальнейшего анализа или отображения.
keywords: Aspose.Cells для Python via .NET, трендлайн диаграммы, текст уравнения, Microsoft Excel, анализ данных, отображение.
linktitle: Трендовые линии
type: docs
weight: 110
url: /ru/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендлайна диаграммы с помощью Aspose.Cells для Python via .NET. Aspose.Cells для Python via .NET предоставляет свойство, которое возвращает текст уравнения трендлайна диаграммы. Для использования этого свойства сначала необходимо вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate).

{{% /alert %}}

На следующем скриншоте показана диаграмма с трендовой линией, и ее текст уравнения показан красным цветом. Мы получим этот текст с помощью свойства [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) в следующем образце кода.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Пример кода на C# для получения текста уравнения трендовой линии диаграммы

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
