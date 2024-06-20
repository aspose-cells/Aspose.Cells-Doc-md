---
title: Получить строковое значение ячейки с или без форматирования
type: docs
weight: 240
url: /ru/net/get-cell-string-value-with-and-without-formatting/
description: Узнайте, как получить значение строки ячейки с форматированием и без форматирования через API Aspose.Cells for .NET.
keywords: Получение значения строки ячейки с и без форматирования, извлечение значения строки ячейки с и без форматирования, получение значения строки ячейки с и без форматирования
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue), который можно использовать для получения строкового значения ячейки с или без какого-либо форматирования. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали ее для отображения только двух десятичных знаков. Тогда она будет отображаться как 0.01 в Excel. Вы можете извлекать строковые значения как 0.01, так и 0.012345, используя метод [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue). В качестве параметра он принимает [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) перечисление, которое имеет следующие значения

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Приведенный ниже образец кода объясняет использование метода [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
