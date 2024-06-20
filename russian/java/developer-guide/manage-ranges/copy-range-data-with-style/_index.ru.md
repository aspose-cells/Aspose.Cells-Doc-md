---
title: Копировать данные диапазона со стилем
type: docs
weight: 340
url: /ru/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Копировать только данные диапазона](/cells/ru/java/copy-range-data-only/) объясняет, как скопировать данные из диапазона ячеек в другой диапазон. Aspose.Cells также может скопировать диапазон с форматированием целиком. Эта статья объясняет, как.

{{% /alert %}} 
## **Копировать данные диапазона со стилем**
Aspose.Cells предоставляет ряд классов и методов для работы с диапазонами, например, [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), и т.д.

Этот пример:

1. Создает рабочую книгу.
1. Заполняет ряд ячеек на первом листе данных.
1. Создает диапазон.
1. Создает объект стиля с указанными атрибутами форматирования.
1. Примените стиль к диапазону данных.
1. Создайте второй диапазон ячеек.
1. Скопируйте данные с форматированием из первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

