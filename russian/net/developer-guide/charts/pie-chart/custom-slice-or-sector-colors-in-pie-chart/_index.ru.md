---
title: Настройка цветов круговой диаграммы
description: Узнайте, как использовать Aspose.Cells for .NET для настройки цветов сегментов и секторов в круговой диаграмме. Наше руководство покажет, как назначить уникальные цвета для каждого сегмента, сектора или легиона для улучшения визуального обращения и представления данных.
keywords: Aspose.Cells for .NET, Круговая диаграмма, настраиваемые цвета сегментов, настраиваемые цвета секторов, визуальное обращение, представление данных.
type: docs
weight: 60
url: /ru/net/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета к сегментам/секторам круговой диаграммы. По умолчанию круговые диаграммы используют шаблон Microsoft Excel по умолчанию. Чтобы использовать другие цвета, перепределите цвета в диаграмме.

{{% /alert %}}

Чтобы установить пользоватский цвет для отдельных секторов или секторов круговой диаграммы:

1. Обратитесь к [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) обьекту [**ChartPoint**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint).
1. Назначьте цвет вашего выбора, используя свойство [**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor).

В этой статье также объясняется, как:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.Area.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/area/properties/foregroundcolor) не является специфичным для круговых диаграмм, но может быть использован для всех типов диаграмм.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomSliceSectorColorsPieChart-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
