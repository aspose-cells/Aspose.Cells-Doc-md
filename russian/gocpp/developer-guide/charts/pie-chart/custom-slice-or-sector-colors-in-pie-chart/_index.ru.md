---
title: Настраиваемые цвета срезов или секторов в круговой диаграмме с помощью Golang через C++
linktitle: Настройка цветов круговой диаграммы
description: Узнайте, как использовать Aspose.Cells for C++ для настройки цветов срезов и сегментов в круговой диаграмме. Наше руководство покажет, как назначить уникальные цвета каждому срезу, сегменту или колонне для улучшения визуальной привлекательности и представления данных.
keywords: Aspose.Cells for C++, Круговая диаграмма, Пользовательские цвета срезов, Пользовательские цвета сегментов, Визуальная привлекательность, Представление данных.
type: docs
weight: 60
url: /ru/go-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета к сегментам/секторам круговой диаграммы. По умолчанию круговые диаграммы используют шаблон Microsoft Excel по умолчанию. Чтобы использовать другие цвета, перепределите цвета в диаграмме.

{{% /alert %}}

Чтобы установить пользоватский цвет для отдельных секторов или секторов круговой диаграммы:

1. Обратитесь к [**Series**](https://reference.aspose.com/cells/go-cpp/series/) обьекту [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/).
1. Назначьте цвет вашего выбора, используя свойство [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/).

В этой статье также объясняется, как:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/go-cpp/area/getforegroundcolor/) не является специфичным для круговых диаграмм, но может быть использован для всех типов диаграмм.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomSliceOrSectorColorsInPieChart.go" >}}
