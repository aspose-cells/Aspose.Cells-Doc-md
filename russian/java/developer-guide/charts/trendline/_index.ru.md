---
title: Получить текст уравнения линии тренда диаграммы
linktitle: линия тренда
type: docs
weight: 90
url: /ru/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 Вы можете получить текст уравнения линии тренда диаграммы, используя Aspose.Cells. Aspose.Cells обеспечивает[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) свойство, которое возвращает текст уравнения линии тренда диаграммы. Чтобы использовать это свойство, вам сначала нужно будет вызвать[**Диаграмма.рассчитать()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) метод.

{{% /alert %}}

## **Пример**

 На следующем снимке экрана показана диаграмма с линией тренда, а текст уравнения выделен красным цветом. Мы получим этот текст с помощью[**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)свойство в следующем примере кода.

![дело:изображение_альтернативный_текст](get-equation-text-of-chart-trendline_1.png)

### Код Java для получения текста уравнения линии тренда диаграммы

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Вывод, сгенерированный примером кода

Это консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
