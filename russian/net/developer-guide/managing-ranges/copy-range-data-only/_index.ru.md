---
title: Копировать только данные диапазона
type: docs
weight: 600
url: /ru/net/copy-range-data-only/
---

{{% alert color="primary" %}}

Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, скопируя только данные, а не форматирование. Aspose.Cells предлагает эту функцию.

Эта статья предоставляет пример кода, который использует Aspose.Cells для копирования диапазона данных.

{{% /alert %}}

Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Создайте [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Создайте объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создайте другой диапазон ячеек.
1. Скопируйте данные из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataOnly-1.cs" >}}
