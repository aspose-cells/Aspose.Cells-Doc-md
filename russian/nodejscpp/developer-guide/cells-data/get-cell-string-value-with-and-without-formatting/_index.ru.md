---
title: Получить строковое значение ячейки с или без форматирования
type: docs
weight: 240
url: /ru/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Узнайте, как получить значение строки ячейки с форматированием и без него через API Aspose.Cells for Node.js via C++.
keywords: Получение значения строки ячейки с форматированием и без форматирования через Node.js с помощью C++, получение значения строки ячейки с форматированием и без него через Node.js с помощью C++, получение значения строки ячейки с форматированием и без него через Node.js с помощью C++
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--), который можно использовать для получения строкового значения ячейки с или без форматирования. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали её для отображения двух знаков после запятой. В Excel она будет отображаться как 0.01. Вы можете получить строковые значения как 0.01, так и 0.012345 с помощью метода [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Он принимает в качестве параметра [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) перечисление, которое имеет следующие значения:

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Следующий пример кода объясняет использование метода [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
