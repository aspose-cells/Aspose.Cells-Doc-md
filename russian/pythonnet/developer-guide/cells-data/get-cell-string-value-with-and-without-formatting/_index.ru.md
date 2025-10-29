---
title: Получить значение строковой ячейки со стратегией форматирования
type: docs
weight: 240
url: /ru/python-net/get-cell-string-value-with-format-strategy/
description: Узнайте, как получить значение строковой ячейки с форматированием и без него через Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, Получение значения строковой ячейки с и без форматирования, Извлечение значения строки ячейки с и без форматирования, Получение значения строки ячейки с и без форматирования с помощью Python
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET предоставляет метод [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/), который можно использовать для получения строкового значения ячейки с или без какого-либо форматирования. Предположим, у вас есть ячейка со значением 0,012345 и вы отформатировали ее для отображения только двух десятичных знаков. Тогда она будет отображаться как 0,01 в Excel. Вы можете извлекать строковые значения как 0,01, так и как 0,012345 с использованием метода [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). Он принимает в качестве параметра перечисление [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/), которое имеет следующие значения

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Приведенный ниже образец кода объясняет использование метода [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
