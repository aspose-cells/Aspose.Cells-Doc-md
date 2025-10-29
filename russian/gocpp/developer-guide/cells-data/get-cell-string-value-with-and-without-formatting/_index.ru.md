---
title: Получить строковое значение ячейки с форматированием и без с Golang через C++
linktitle: Получить строковое значение ячейки
type: docs
weight: 240
url: /ru/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Узнайте, как получать строковое значение ячейки с форматированием и без него через API Aspose.Cells for C++.
keywords: Получение значения строки ячейки с и без форматирования, извлечение значения строки ячейки с и без форматирования, получение значения строки ячейки с и без форматирования
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/), который можно использовать для получения строкового значения ячейки с любым или без форматирования. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали его так, чтобы отображать только два знака после запятой. В Excel оно будет отображаться как 0.01. Вы можете получить строковые значения как 0.01, так и 0.012345, используя метод [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Он принимает параметр типа [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/), который имеет следующие значения:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Приведенный ниже образец кода объясняет использование метода [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
