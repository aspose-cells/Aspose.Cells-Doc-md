---
title: Получить строковое значение Cell с форматированием и без него
type: docs
weight: 230
url: /ru/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

 Aspose.Cells предоставляет метод[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)), который можно использовать для получения строкового значения ячейки с форматированием или без него. Предположим, у вас есть ячейка со значением 0,012345, и вы отформатировали ее для отображения только двух знаков после запятой. Затем он будет отображаться как 0,01 в Excel. Вы можете получить строковые значения как 0,01, так и 0,012345, используя[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ) метод. Занимает[CellValueFormatStrategy](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)enum как параметр, который имеет следующие значения

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **Получить строковое значение Cell с форматированием и без него**
 В следующем примере кода объясняется использование[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **Консольный вывод**
Ниже приведен консольный вывод приведенного выше примера кода.

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
