---
title: Получить текст уравнения линии тренда диаграммы с Golang через C++
linktitle: Трендовые линии
description: Узнайте, как использовать Aspose.Cells for C++ для получения текста уравнения трендовой линии в диаграмме, созданной в Microsoft Excel. Наше руководство покажет, как получить и извлечь уравнение трендовой линии для дальнейшего анализа или отображения.
keywords: Aspose.Cells for C++, Трендовая линия диаграммы, Текст уравнения, Microsoft Excel, Анализ данных, Отображение.
type: docs
weight: 110
url: /ru/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендовой линии диаграммы с помощью Aspose.Cells. Aspose.Cells предоставляет свойство [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/), которое возвращает текст уравнения трендовой линии диаграммы. Для использования этого свойства сначала нужно вызвать метод [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Следующий скриншот показывает диаграмму с трендлайном и его текст уравнения, выделенный красным цветом. Мы получим этот текст, используя свойство [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) в следующем примере.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++ код для получения текста уравнения трендовой линии диаграммы

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
