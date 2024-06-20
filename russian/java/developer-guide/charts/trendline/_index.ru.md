---
title: Получение текста уравнения трендовой линии диаграммы
linktitle: Линия тренда
type: docs
weight: 90
url: /ru/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендовой линии диаграммы с помощью Aspose.Cells. Aspose.Cells предоставляет свойство [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text), которое возвращает текст уравнения трендовой линии диаграммы. Для использования этого свойства сначала нужно вызвать метод [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **Пример**

На следующем скриншоте показана диаграмма с трендовой линией, и ее текст уравнения показан красным цветом. Мы получим этот текст с помощью свойства [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) в следующем образце кода.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Код Java для получения текста уравнения линии тренда графика

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Результат, сгенерированный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
