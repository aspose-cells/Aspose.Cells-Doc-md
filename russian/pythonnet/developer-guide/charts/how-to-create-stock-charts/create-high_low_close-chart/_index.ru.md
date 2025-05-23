---
title: Создание диаграммы акций HLC (High Low Close)
description: Узнайте, как создавать график акций с высоким, низким и закрывающим ценами с помощью Aspose.Cells для Python via .NET. Наш пошаговый гид покажет, как отображать данные фондового рынка, включая высокие, низкие и закрывающие цены, на графике для лучшего анализа и визуализации.
keywords: Aspose.Cells для Python via .NET, График акций с высоким, низким, закрывающим ценами, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 181
url: /ru/python-net/create-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
График цен акций High-Low-Close (HLC) использует четыре столбца данных. Первый столбец представляет собой категорию, обычно дату, но также можно использовать имена акций. Следующие три столбца по порядку предназначены для отображения высокой, низкой и закрывающей цены. Диапазон цен для каждой категории указывается вертикальной линией, отображающей диапазон от низкой к высокой цене, а за закрытие отмечается метка, выходящая вправо от этой линии.

![todo:image_alt_text](sample.png)

## **Улучшения видимости на графике**
Иногда, чтобы сделать график более интуитивно понятным, мы можем изменить внешний вид маркера (закрытия) или отображать его на вторичной оси.

![todo:image_alt_text](sample2.png)

## **Образец кода**
Нижеприведенный образец кода загружает [образец файла Excel](High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-high-low-close-stock-chart.py" >}}
