---
title: 添加和检索数据
type: docs
weight: 20
url: /zh/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

在[访问工作表的 Cells](/cells/zh/java/accessing-cells-of-a-worksheet/)，我们讨论了访问工作表中单元格的基本方法。本文使用其中一种方法将不同类型的数据添加到单元格。

{{% /alert %}} 
## **添加数据到 Cells**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Aspose.Cells 允许开发人员通过调用[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级'[设定值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)财产。通过使用[设定值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)属性，可以向单元格添加布尔值、字符串、双精度、整数或日期/时间等值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **提高效率**
{{% alert color="primary" %}} 

如果您使用[设定值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)属性将大量数据添加到工作表，您应该将值添加到单元格，首先按行，然后按列。这种方法极大地提高了应用程序的效率。

{{% /alert %}} 

在处理工作表时，用户可以在单元格中添加不同类型的数据。这些数据项可能包括布尔值、整数、浮点数、文本或日期/时间值。您可以使用 Aspose.Cells 根据单元格的数据类型从单元格中获取适当的值。
## **从 Cells 检索数据**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)表示一个 Excel 文件。[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

这[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供了几个属性，允许开发人员根据单元格的数据类型从单元格中检索值。这些属性包括：

- [字符串值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)，单元格的字符串值。
- [双值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)返回单元格的双精度值。
- [布尔值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)，单元格的布尔值。
- [日期时间值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)，单元格的日期/时间值。
- [浮动值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)，单元格的浮点值。
- [整数值](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)，单元格的整数值。

此外，还可以使用[类型](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)的财产[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。事实上，[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级'[类型](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)财产是基于[单元值类型](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)下面列出了预定义值的枚举：

|**Cell 值类型**|**描述**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|指定单元格值为布尔值。|
|[是_日期_时间](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|指定单元格值为日期/时间。|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|表示单元格包含错误值|
|[一片空白](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|代表一个空白单元格。|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|指定单元格值为数字。|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|指定单元格值是一个字符串。|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|指定单元格值未知。|
您还可以使用上述预定义的单元格值类型来与每个单元格中存在的数据类型进行比较。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
