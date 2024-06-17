---
title: 分组行并创建小计
type: docs
weight: 70
url: /zh/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: 本文介绍如何对行/列进行分组/取消分组，并且如何在GridWeb中使用小计功能。
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb可以为您的数据创建大纲。这让您可以通过点击大纲符号 "+" 和 "-" 来显示和隐藏详细级别，以仅显示提供摘要或章节标题的行，您可以使用这些符号来查看工作表中各个摘要或标题下的详细信息。

在分组行时，重要的是选择只包含组成该组的详细行不要包括相关的摘要行。例如，如果第6行包含行3到5中的数据总和，请选择只有第3至5行以定义该组。 Aspose.Cells.GridWeb控件在工作表中的行标头旁边显示**显示详细信息**（+）和**隐藏具体信息**（-）符号以指定工作表中的组。

Aspose.Cells.GridWeb还允许您根据任何数据字段创建小计。小计不一定是求和：它可以是平均值、计数、最小值、最大值或其他统计计算。

本主题讨论了使用Aspose.Cells.GridWeb API对行进行分组并创建小计。开发人员可以轻松地对行进行任何嵌套级别的分组，并创建小计。

{{% /alert %}} 
## **分组行**
要对特定数量的行进行分组：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单中。
1. 访问工作表。
1. 选择目标行中所需数量的单元格。
1. 对行进行分组。

当行被分组时，展开/折叠按钮会显示在行摘要行的顶部。您可以更改方向设置。WebWorksheet.IsSummaryRowBelow属性是一个布尔属性。将其设置为false（默认值），摘要行就会显示在详细行上方，将其设置为true，摘要行就会显示在详细行下方。单击展开/折叠按钮可展开或折叠分组的行。

以下示例将从第2行到第10行分组的行。

**分组行** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **嵌套分组行**
在对一组行进行分组时，您可以创建组织层次结构级别。您可以在已分组的行中对行进行分组。以下示例显示了嵌套已分组行。

**分组行** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **内部流程：控件如何运作？**
工作表的每一行都有一个大纲号。大纲号的默认值为零。每次对行进行分组时，大纲号都会加1。您可以通过调用GridWorksheet.Cells.GetRowOutlineLevel()方法来获取大纲号。
## **取消组合行**
Aspose.Cells.GridWeb允许您取消对分组行的分组。

取消对指定行数的行进行分组：

1. 在工作表中选择要取消分组的行中的单元格数。
1. 取消行的分组。

以下示例取消了从第2行到第10行的行的分组。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

当调用GridWorksheet.Cells.UngroupRows()方法时，分组行的轮廓编号将设置为零。

{{% /alert %}} 
## **创建小计**
控件的小计功能可以根据指定的列对工作表中的行进行分组，并计算列的汇总。Aspose.Cells.GridWeb可以自动计算列表的小计值。实现小计时，控件会概述列表，以便您可以显示和隐藏每个小计的详细行。在添加小计之前，按照您希望进行小计的字段进行排序。要创建小计，请使用WebWorksheet.CreateSubtotal方法的任何版本。



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
|1|columnNameRowIndex|列名称行的行索引。|
|2|dataRows|数据行的行数。|
|3|groupByColumnIndex|要进行分组的列的列索引。|
|4|subtotalFunction|小计函数类型枚举。|
|5|subtotalColumnIndexList|要进行小计的列索引。|
### **摘要函数列表**
由{{SubtotalFunction}}枚举支持的几种摘要函数类型：

|**编号**|**函数名称**|**描述**|
| :- | :- | :- |
|1|AVERAGE|计算值的平均值。|
|2|COUNT|计算单元格中数值的数量。|
|3|COUNTA|计算单元格中非数字数据的数量。|
|4|MAX|计算最大值。|
|5|MIN|计算最小值。|
|6|PRODUCT|计算数值的乘积。|
|7|SUM|计算数值的总和。|
以下示例生成通过工作表中的第二列分组计算非数字值的小计。

**小计** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **移除小计**
要移除小计，请使用 WebWorksheet.RemoveSubtotal 方法。以下示例移除小计。



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **关于 SUBTOTAL 函数**
GridWeb 控件使用 SUBTOTAL 公式函数来计算小计值。

语法：SUBTOTAL(function_num, ref1, ref2, ...)

function_num 是指定小计计算中使用的函数类型的数字。

|**1**|**平均值**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
ref1、ref2 等为小计计算的区域。如果 ref1、ref2 ... 包含其他小计函数，则忽略引用的单元格，以避免重复计算。
