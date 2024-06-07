---
title: 分组行并创建小计
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb，小计，分组，取消分组
description: 本文介绍如何在GridWeb中分组/取消分组行/列以及如何使用小计。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb可以为您的数据创建概要。这样，您可以通过单击概要符号“+”和“-”来显示和隐藏详细级别，仅显示提供工作表部分摘要或标题的行。您可以使用这些符号来查看单个摘要或标题下的详细信息。

在分组行时，重要的是只选择组成组的详细行。不要包括相关的摘要行。例如，如果第6行包含第3到第5行数据的总计，请仅选择第3到第5行来定义该组。Aspose.Cells.GridWeb控件在工作表中指定组的行标题旁显示“显示详细信息”（+）和“隐藏详细信息”（-）符号。

Aspose.Cells.GridWeb还允许您基于任何数据字段创建小计。小计不一定是求和：它可以是平均值、计数、最小值、最大值或其他统计计算。

本主题讨论了如何使用Aspose.Cells.GridWeb API对行进行分组和创建小计。开发人员可以轻松地对行进行分组，嵌套任何层级，并创建小计。

{{% /alert %}} 
## **分组行**
要对特定数量的行进行分组：

1. 将Aspose.Cells.GridWeb控件添加到Web表单中。
1. 访问工作表。
1. 选择要在行中进行分组的所需单元格数量。
1. 对行进行分组。

当对行进行分组时，在行的摘要行顶部会显示展开/折叠按钮。您可以更改方向设置。WebWorksheet.IsSummaryRowBelow属性是一个布尔属性。将其设置为false（默认值），摘要行将位于详细行上方。将其设置为true，摘要行将位于详细行下方。单击展开/折叠按钮以展开或折叠分组的行。

以下示例将第2行到第10行进行分组。

分组行 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **嵌套分组的行**
在对一组行进行分组时，您可以创建组织级别。您可以对嵌套行中的行进行分组。以下示例显示了嵌套分组的行。

分组行 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **内部流程：控件如何工作？**
工作表的每行都有一个概述编号。概述编号的默认值为零。每次对行进行分组时，概述编号就会增加1。您可以通过调用GridWorksheet.Cells.GetRowOutlineLevel()方法获取概述编号。
## **取消分组行**
Aspose.Cells.GridWeb允许您取消分组的行。

要取消特定数量的行的分组：

1. 选择工作表中行的单元格数量来取消分组。
1. 取消分组行。

以下示例将第2行到第10行的行取消分组。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

当调用GridWorksheet.Cells.UngroupRows()方法时，已分组行的概述编号将设置为零。

{{% /alert %}} 
## **创建小计**
控件的小计功能可以根据工作表中的指定列对行进行分组，并计算列的汇总。Aspose.Cells.GridWeb可以自动为列表计算小计值。在实现小计时，控件会为列表制作概述，以便您可以显示和隐藏每个小计的详细行。在添加小计之前，对希望进行小计的字段进行排序。要创建小计，请使用WebWorksheet.CreateSubtotal方法的任何版本。



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **参数列表**

|**编号**|**参数名称**|**描述**|
| :- | :- | :- |
|1|columnNameRowIndex|列名行的行索引。|
|2|dataRows|数据行的数量。|
|3|groupByColumnIndex|要分组的列的列索引。|
|4|subtotalFunction|小计功能类型枚举。|
|5|subtotalColumnIndexList|要小计的列索引。|
### **汇总函数列表**
由{[SubtotalFunction}}枚举支持几种汇总函数类型：

|**编号**|**函数名称**|**描述**|
| :- | :- | :- |
|1|AVERAGE|计算值的平均值。|
|2|COUNT|计算单元格中数值的数量。|
|3|COUNTA|计算单元格中非数值数据的数量.|
|4|MAX|计算最大值.|
|5|MIN|计算最小值.|
|6|PRODUCT|计算数值的乘积.|
|7|SUM|计算数值的和.|
以下示例生成小计，计算工作表中第二列分组的非数字值。

**小计** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **删除小计**
要删除小计，请使用 WebWorksheet.RemoveSubtotal 方法。 以下示例移除小计。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **SUBTOTAL 函数介绍**
GridWeb 控件利用公式函数 SUBTOTAL 计算小计值。

语法：SUBTOTAL(function_num, ref1, ref2, ...)

function_num 是指定在小计计算中使用的函数类型的编号。

|**1**|**平均值**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1、ref2 是要进行小计的区域。如果 ref1、ref2 等包含其他小计函数，则会忽略引用的单元格，以避免重复计算。
