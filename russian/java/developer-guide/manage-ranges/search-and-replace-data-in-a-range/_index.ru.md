---
title: Поиск и замена данных в диапазоне
type: docs
weight: 60
url: /ru/java/search-and-replace-data-in-a-range/
description: Эта статья показывает, как выполнять поиск и замену данных в диапазоне в Excel с использованием Java кода.
keywords: поиск и замена данных в Excel на Java, поиск данных в Excel на Java, поиск и замена данных в диапазоне на Java, поиск данных в диапазоне на Java, поиск данных в диапазоне на Java, поиск данных в диапазоне на Java, поиск данных в Excel на Java, поиск данных в диапазоне на Java, поиск и замена данных в Excel с помощью Java, поиск и замена данных в диапазоне с помощью Java, поиск и замена данных в диапазоне с помощью Java
---

{{% alert color="primary" %}}

Иногда вам нужно найти и заменить конкретные данные в диапазоне, игнорируя значения ячеек за пределами желаемого диапазона. Aspose.Cells позволяет ограничить поиск определенным диапазоном. В этой статье объясняется, как это сделать.

{{% /alert %}}

Aspose.Cells предоставляет метод [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) для указания диапазона при поиске данных.

Предположим, вы хотите найти строку **"поиск"** и заменить ее на **"замена"** в диапазоне **E3:H6**. На скриншоте ниже показано, что строка "поиск" есть в нескольких ячейках, но мы хотим заменить ее только в заданном диапазоне, отмеченном здесь желтым цветом.

**Входной файл**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

После выполнения кода выходной файл выглядит так, как показано на рисунке ниже. Все строки "поиска" в диапазоне были заменены на "замена".

**Файл вывода**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Связанные статьи

- [Поиск или поиск данных](/cells/ru/java/find-or-search-data/)
