---
title: Настройка цветов круговой диаграммы
description: Узнайте, как использовать Aspose.Cells для Python via .NET для настройки цветов срезов и секторов в круговой диаграмме. Наш гид покажет, как назначать уникальные цвета каждому срезу, сектору или сегменту для улучшения визуальной привлекательности и представления данных.
keywords: Aspose.Cells для Python via .NET, Круговая диаграмма, Настройка цветов срезов, Секторная настройка, Визуальный эффект, Представление данных.
type: docs
weight: 60
url: /ru/python-net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета к сегментам/секторам круговой диаграммы. По умолчанию круговые диаграммы используют шаблон Microsoft Excel по умолчанию. Чтобы использовать другие цвета, перепределите цвета в диаграмме.

{{% /alert %}}

Чтобы установить пользоватский цвет для отдельных секторов или секторов круговой диаграммы:

1. Обратитесь к [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) обьекту [**ChartPoint**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint).
1. Назначьте цвет вашего выбора, используя свойство [**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color).

В этой статье также объясняется, как:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.area.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/area/foreground_color) не является специфичным для круговых диаграмм, но может быть использован для всех типов диаграмм.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CustomSliceSectorColorsPieChart-1.py" >}}
