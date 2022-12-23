---
title: Пользовательские цвета срезов или секторов в круговой диаграмме
type: docs
weight: 60
url: /ru/net/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета в секторы/срезы круговой диаграммы. По умолчанию для круговых диаграмм используется шаблон Excel по умолчанию Microsoft. Чтобы использовать другие цвета, переопределите цвета на диаграмме.

{{% /alert %}}

Чтобы установить пользовательский цвет для отдельных сегментов или секторов круговой диаграммы:

1.  Доступ к[**Ряд**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) объекты[**Диаграмма**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1.  Назначьте цвет по вашему выбору с помощью[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor)имущество.

В этой статье также объясняется, как:

- Данные категории диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Позиция легенды.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) не является специфичным для круговых диаграмм, но может использоваться для всех типов диаграмм.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
