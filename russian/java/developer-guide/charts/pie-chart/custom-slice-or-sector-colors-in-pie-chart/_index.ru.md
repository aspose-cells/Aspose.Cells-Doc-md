---
title: Пользовательские цвета срезов или секторов в круговой диаграмме
type: docs
weight: 30
url: /ru/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета в секторы/срезы круговой диаграммы. По умолчанию для круговых диаграмм используется шаблон Excel по умолчанию Microsoft. Чтобы использовать другие цвета, можно переопределить цвета на диаграмме.

{{% /alert %}}

Чтобы установить пользовательский цвет для отдельных сегментов или секторов круговой диаграммы:

1.  Доступ к[**Серии**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) объекты[**Диаграмма**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Назначьте цвет по вашему выбору с помощью[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)метод.

В этой статье также объясняется, как установить:

- Данные категории диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Позиция легенды.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) не является специфичным для круговых диаграмм, но может использоваться для всех типов диаграмм.

{{% /alert %}}

**Пользовательские цвета фрагментов в круговой диаграмме**

![дело:изображение_альтернативный_текст](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
