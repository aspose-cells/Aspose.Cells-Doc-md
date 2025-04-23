---
title: Копировать только стиль диапазона
type: docs
weight: 620
url: /ru/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[Копирование только данных диапазона](/cells/ru/net/copy-range-data-only/) и [Копирование данных диапазона со стилем](/cells/ru/net/copy-range-data-with-style/) объясняют, как скопировать данные из диапазона в другой только с форматированием или полностью. Также возможно копирование только форматирования. В этой статье показано как.

{{% /alert %}} 

Этот пример создает рабочую книгу, заполняет ее данными и копирует только стиль диапазона.

1. Создать диапазон.
1. Создайте объект [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создать второй диапазон ячеек.
1. Скопируйте формат первого диапазона во второй диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
