---
title: Поиск и замена данных в диапазоне
type: docs
weight: 60
url: /ru/java/search-and-replace-data-in-a-range/
description: В этой статье показано, как искать и заменять данные в диапазоне в Excel, используя код Java.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

Иногда вам нужно искать и заменять определенные данные в диапазоне, игнорируя любые значения ячеек за пределами желаемого диапазона. Aspose.Cells позволяет ограничить поиск определенным диапазоном. В этой статье объясняется, как.

{{% /alert %}}

Aspose.Cells обеспечивает[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) способ указания диапазона при поиске данных.

 Предположим, вы хотите найти строку**"поиск"** и замените его на**"заменять"** В диапазоне**Е3:Н6**. На скриншоте ниже строка «поиск» видна в нескольких ячейках, но мы хотим заменить ее только в заданном диапазоне, здесь выделенном желтым цветом.

**Входной файл**

![дело:изображение_альтернативный_текст](search-and-replace-data-in-a-range_1.png)

После выполнения кода выходной файл выглядит так, как показано ниже. Все строки «поиск» в пределах диапазона были заменены на «заменить».

**Выходной файл**

![дело:изображение_альтернативный_текст](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Статьи по Теме

- [Поиск или поиск данных](/cells/ru/java/find-or-search-data/)
