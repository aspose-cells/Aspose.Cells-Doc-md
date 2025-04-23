---
title: Получение текста уравнения трендовой линии диаграммы
description: Узнайте, как использовать Aspose.Cells for .NET для извлечения текста уравнения трендовой линии на диаграмме, созданной в Microsoft Excel. Наше руководство продемонстрирует, как получить доступ к уравнению трендовой линии для дальнейшего анализа или отображения.
keywords: Aspose.Cells for .NET, Трендовая линия диаграммы, Текст уравнения, Microsoft Excel, Анализ данных, Отображение.
linktitle: Трендовые линии
type: docs
weight: 110
url: /ru/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендовой линии диаграммы с помощью Aspose.Cells. Aspose.Cells предоставляет свойство [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text), которое возвращает текст уравнения трендовой линии диаграммы. Для использования этого свойства сначала нужно вызвать метод [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

На следующем скриншоте показана диаграмма с трендовой линией, и ее текст уравнения показан красным цветом. Мы получим этот текст с помощью свойства [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) в следующем образце кода.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Пример кода на C# для получения текста уравнения трендовой линии диаграммы

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
