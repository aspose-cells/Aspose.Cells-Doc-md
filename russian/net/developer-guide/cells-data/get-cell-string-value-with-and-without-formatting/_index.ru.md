---
title: Получить строковое значение Cell с форматированием и без него
type: docs
weight: 240
url: /ru/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет метод[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) который можно использовать для получения строкового значения ячейки с форматированием или без него. Предположим, у вас есть ячейка со значением 0,012345, и вы отформатировали ее для отображения только двух знаков после запятой. Затем он будет отображаться как 0,01 в Excel. Вы можете получить строковые значения как 0,01, так и 0,012345, используя[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) метод. Занимает[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum как параметр, который имеет следующие значения

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 В следующем примере кода объясняется использование[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
