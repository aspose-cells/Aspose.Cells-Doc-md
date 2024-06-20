---
title: Копировать только данные диапазона
type: docs
weight: 600
url: /ru/python-net/copy-range-data-only/
description: В этой статье описано, как копировать только данные диапазона с помощью библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python для работы с Excel, Как скопировать только данные диапазона в Python, Как скопировать только данные диапазона в Python с помощью библиотеки Python Excel.
---

{{% alert color="primary" %}}

Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, копируя только данные, но не форматирование. Aspose.Cells для Python via .NET предлагает эту функцию.

В этой статье предоставлен образец кода, использующий Aspose.Cells для Python via .NET для копирования диапазона данных.

{{% /alert %}}

Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Создайте [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).
1. Создайте объект [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создайте другой диапазон ячеек.
1. Скопируйте данные из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CopyRangeDataOnly-1.py" >}}
