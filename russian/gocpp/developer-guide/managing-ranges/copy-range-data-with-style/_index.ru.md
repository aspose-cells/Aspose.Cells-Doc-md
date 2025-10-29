---
title: Копировать данные диапазона с стилями в C++
linktitle: Копировать данные диапазона со стилем
type: docs
weight: 610
url: /ru/go-cpp/copy-range-data-with-style/
description: Копировать данные диапазона, включая стили ячеек, в файлах Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Только копирование данных диапазона](/cells/ru/cpp/copy-range-data-only/) объясняет, как копировать данные ячеек между диапазонами. Эта статья демонстрирует, как копировать диапазоны ячеек с сохранением их форматов с помощью Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells предоставляет классы и методы для работы с диапазонами, включая [**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) и [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Этот пример демонстрирует, как:

1. Создать рабочую книгу
1. Заполнить ячейки данными
1. Создать [**Range**](https://reference.aspose.com/cells/go-cpp/range/)
1. Создать и настроить объект [**Style**](https://reference.aspose.com/cells/go-cpp/style/)
1. Применить стили к диапазону
1. Создать второй диапазон
1. Копировать отформатированные данные между диапазонами

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
