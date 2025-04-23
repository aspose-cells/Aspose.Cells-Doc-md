---
title: Копировать только данные диапазона
type: docs
weight: 330
url: /ru/java/copy-range-data-only/
---

{{% alert color="primary" %}} 

Иногда нужно скопировать данные из одного диапазона ячеек в другой, копируя только данные, без форматирования. Aspose.Cells предоставляет такую возможность с помощью метода [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-)

{{% /alert %}} 
## **Копировать только данные диапазона**
Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Создать диапазон.
1. Создать объект стиля с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создайте другой диапазон ячеек.
1. Скопируйте данные из первого диапазона в второй с помощью метода [Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData-com.aspose.cells.Range-)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
{{< app/cells/assistant language="java" >}}
