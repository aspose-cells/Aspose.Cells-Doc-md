---
title: 对行进行分组并创建小计
type: docs
weight: 70
url: /zh/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb 可以为您的数据创建轮廓。这使您可以通过单击大纲符号“+”和“-”来显示和隐藏详细级别，以仅显示为工作表中的部分提供摘要或标题的行。您可以使用符号查看单个摘要或标题下的详细信息。

对行进行分组时，仅选择组成该组的详细信息行很重要。不要包括相关的摘要行。例如，如果第 6 行包含第 3 行至第 5 行数据的总计，则仅选择第 3 行至第 5 行来定义组。 Aspose.Cells.GridWeb 控件显示**查看详细**(+) 和**隐藏细节**行标题旁边的 (-) 符号指定工作表中的组。

Aspose.Cells.GridWeb 还允许您根据任何数据字段创建小计。小计不一定是总和：它可以是平均值、计数、最小值、最大值或其他统计计算。

本主题讨论使用 Aspose.Cells.GridWeb API 对行进行分组和创建小计。开发人员可以使用任何嵌套级别对行进行分组并轻松创建小计。

{{% /alert %}} 
## **分组行**
对特定数量的行进行分组：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问工作表。
1. 在行中选择所需的单元格数。
1. 对行进行分组。

对行进行分组时，展开/折叠按钮会显示在行的摘要行的顶部。您可以更改方向设置。 WebWorksheet.IsSummaryRowBelow 属性是一个布尔值属性。将其设置为 false（默认），摘要行将位于详细信息行之上。将其设置为 true，摘要行将位于详细信息行下方。单击展开/折叠按钮以展开或折叠分组的行。

以下示例对从第 2 行到第 10 行的行进行分组。

**分组行** 

![待办事项：图片_替代_文本](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **嵌套分组行**
您可以在对一组行进行分组时创建组织级别。您可以在分组的行中对行进行分组。以下示例显示嵌套分组行。

**分组行** 

![待办事项：图片_替代_文本](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **内部流程：控制如何运作？**
工作表的每一行都有一个大纲编号。大纲编号的默认值为零。每次对行进行分组时，大纲编号增加 1。您可以通过调用 GridWorksheet.Cells.GetRowOutlineLevel() 方法获取大纲编号。
## **取消组合行**
Aspose.Cells.GridWeb 允许您取消分组行。

要取消组合特定数量的行：

1. 在工作表的行中选择多个单元格以取消分组。
1. 取消组合行。

以下示例取消对从第 2 行到第 10 行的行进行分组。



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

当您调用 GridWorksheet.Cells.UngroupRows() 方法时，分组行的大纲编号设置为零。

{{% /alert %}} 
## **创建小计**
该控件的小计功能可以将工作表中的行与指定的列进行分组，并计算列的汇总。 Aspose.Cells.GridWeb 可以自动计算列表的小计值。当您实现小计时，该控件勾勒出列表，以便您可以显示和隐藏每个小计的详细信息行。在添加小计之前，对您希望小计的字段进行排序。要创建小计，请使用任何版本的重载 WebWorksheet.CreateSubtotal 方法。



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **参数表**

|**不。**|**参数名称**|**描述**|
|:- |:- |:- |
|1|列名行索引|列名行的行索引。|
|2|数据行|数据行数。|
|3|groupByColumnIndex|要分组的列的列索引。|
|4|小计功能|小计函数类型枚举。|
|5|小计列索引列表|要小计的列索引。|
### **汇总函数列表**
{[SubtotalFunction}} 枚举支持多种类型的汇总函数：

|**不。**|**函数名称**|**描述**|
|:- |:- |:- |
|1|平均的|计算值的平均值。|
|2|数数|计算单元格中的数值。|
|3|伯爵|计算单元格中的非数字数据。|
|4|最大限度|计算最大值。|
|5|最小值|计算最小值。|
|6|产品|计算值的乘积。|
|7|和|计算值的总和。|
以下示例生成小计，计算按工作表中第二列分组的非数字值。

**小计** 

![待办事项：图片_替代_文本](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **删除小计**
要删除小计，请使用 WebWorksheet.RemoveSubtotal 方法。以下示例删除小计。



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **关于 SUBTOTAL 函数**
GridWeb 控件使用公式函数 SUBTOTAL 来计算小计值。

语法：SUBTOTAL(function_num, ref1, ref2, ...)

function_num 是一个数字，指定小计计算中使用的函数类型。

|**1**|**平均的**|
|:- |:- |
|2|数数|
|3|伯爵|
|4|最大限度|
|5|最小值|
|6|产品|
|7|和|
ref1、ref2 是要小计的区域。如果 ref1、ref2、... 包含其他小计函数，则忽略引用的单元格以避免重复计算。
