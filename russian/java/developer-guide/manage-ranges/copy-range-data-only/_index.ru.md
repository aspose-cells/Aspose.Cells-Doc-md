---
title: Копировать только данные диапазона
type: docs
weight: 330
url: /ru/java/copy-range-data-only/
---
{{% alert color="primary" %}} 

Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, копируя только данные, а не форматирование. Aspose.Cells предлагает эту функцию, предоставляя[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) метод.

{{% /alert %}} 
## **Копировать только данные диапазона**
В этом примере показано, как:

1. Создайте рабочую книгу.
1. Добавьте данные в ячейки на первом листе.
1. Создайте диапазон.
1. Создайте объект стиля с указанными атрибутами форматирования.
1. Примените форматирование стиля к диапазону.
1. Создайте еще один диапазон ячеек.
1.  Скопируйте данные первого диапазона в этот второй диапазон, используя кнопку[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
