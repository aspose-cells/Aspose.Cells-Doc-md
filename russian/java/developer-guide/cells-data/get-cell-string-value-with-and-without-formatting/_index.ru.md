---
title: Получить строковое значение ячейки с или без форматирования
type: docs
weight: 230
url: /ru/java/get-cell-string-value-with-and-without-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет метод [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-), который можно использовать для получения строкового значения ячейки с любым форматированием или без него. Предположим, у вас есть ячейка со значением 0.012345, и вы отформатировали её так, чтобы показывать только два знака после запятой. Тогда в Excel она отобразится как 0.01. Вы можете получить строковые значения как 0.01, так и 0.012345, используя метод [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-). Он принимает [CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy) в качестве параметра, который имеет следующие значения

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL-STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY-STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Получение строкового значения ячейки с или без форматирования**
Следующий пример кода объясняет использование метода [Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue-int-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Вывод в консоль**
Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

 0.01

0.012345

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
