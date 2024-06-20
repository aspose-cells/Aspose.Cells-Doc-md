---
title: Копировать только данные диапазона
type: docs
weight: 330
url: /ru/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, копируя только данные, а не форматирование. Aspose.Cells предлагает эту функцию, предоставив метод [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)).

{{% /alert %}} 
## **Копировать только данные диапазона**
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Создать диапазон.
1. Создать объект стиля с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создайте другой диапазон ячеек.
1. Скопируйте данные первого диапазона в этот второй диапазон, используя метод [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
