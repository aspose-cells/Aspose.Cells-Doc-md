---
title: Настройка цветов круговой диаграммы
type: docs
weight: 30
url: /ru/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета для сегментов в круговой диаграмме. По умолчанию круговые диаграммы используют шаблон по умолчанию Microsoft Excel. Чтобы использовать другие цвета, можно переопределить цвета в диаграмме.

{{% /alert %}}

Для установки пользовательского цвета для отдельных сегментов круговой диаграммы:

1. Обратитесь к [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) обьекту [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1. Назначьте цвет по вашему выбору, используя метод [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor).

Эта статья также объясняет, как установить:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) не является специфичным для круговых диаграмм, но может использоваться для всех типов диаграмм.

{{% /alert %}}

**Пользовательские цвета сегментов в круговой диаграмме**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
