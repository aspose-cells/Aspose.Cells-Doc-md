---
title: 添加和检索数据
type: docs
weight: 20
url: /zh/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

在[访问工作表单元格](/cells/zh/java/accessing-cells-of-a-worksheet/)中，我们讨论了访问工作表单元格的基本方法。本文使用其中一种方法向单元格添加不同类型的数据。

{{% /alert %}} 
## **向单元格添加数据**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项表示[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的一个对象。

Aspose.Cells允许开发人员通过调用[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)属性向工作表的单元格添加数据。通过使用[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)属性，可以向单元格添加布尔值、字符串、双精度型、整型或日期/时间等值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **提高效率**
{{% alert color="primary" %}} 

如果您使用[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)属性向工作表添加大量数据，应先按行然后按列向单元格添加值。这种方法极大地提高了应用程序的效率。

{{% /alert %}} 

在处理工作表时，用户可能会在单元格中添加不同类型的数据。这些数据项可以包括布尔值、整数、浮点数、文本或日期/时间值。您可以使用Aspose.Cells根据其数据类型从单元格中获取适当的值。
## **从单元格检索数据**
Aspose.Cells提供了一个代表Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合每个项表示[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的一个对象。

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供了几个属性，允许开发人员根据其数据类型从单元格中检索值。这些属性包括：

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue)，单元格的字符串值。
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue)，返回单元格的双精度值。
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue)，单元格的布尔值。
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue)，单元格的日期/时间值。
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue)，单元格的浮点值。
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue)，单元格的整数值。

此外，还可以使用[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)属性来检查单元格中包含的数据类型。事实上，[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的[Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type)属性基于[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)枚举，其预定义的值如下所示：

|**单元格值类型**|**描述**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-BOOL)|指定单元格值为布尔类型。|
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-DATE-TIME)|指定单元格值为日期/时间。|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-ERROR)|表示单元格包含错误值|
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NULL)|表示空白单元格。|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-NUMERIC)|指定单元格值为数字类型。|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-STRING)|指定单元格值为字符串。|
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS-UNKNOWN)|指定单元格值为未知。|
您还可以使用上述预定义的单元格值类型与每个单元格中的数据类型进行比较。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
{{< app/cells/assistant language="java" >}}
