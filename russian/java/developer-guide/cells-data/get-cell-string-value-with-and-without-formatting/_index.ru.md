---
title: Получить строковое значение ячейки с или без форматирования
type: docs
weight: 230
url: /ru/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет метод [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)), который можно использовать для получения строкового значения ячейки с или без какого-либо форматирования. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали ее для отображения только двух десятичных знаков. Затем она отобразится как 0.01 в Excel. Вы можете извлечь строковые значения как 0.01, так и как 0.012345, используя метод [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)). Он принимает в качестве параметра перечисление [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy), которое имеет следующие значения

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Получение строкового значения ячейки с или без форматирования**
В следующем примере кода объясняется использование метода [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Вывод в консоль**
Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
