---
title: 如何在智能标记中分组数据
type: docs
weight: 30
url: /zh/net/how-to-group-data-in-smart-markers/
---

## **可能的使用场景**
在一些 Excel 报告中，您可能需要将数据分成组，以便更容易阅读和分析。将数据分成组的主要目的之一是对每组记录运行计算（执行摘要操作）。

Aspose.Cells智能标记允许您按字段分组数据，并在数据集或数据组之间放置摘要行。例如，如果按Customers.CustomerID分组数据，可以在每次分组更改时添加摘要记录。

## **智能标记中的分组参数**
以下是用于数据分组的一些智能标记参数。
### **group:normal/merge/repeat**
我们支持三种您可以选择的分组类型。

- **normal** - 分组字段的值不会为相应列中的记录重复；相反，它们每个数据组仅打印一次。
- **merge** - 与 normal 参数的行为相同，只是它合并了每个组集的分组字段单元格。
- **repeat** - 分组字段的值将为相应记录重复。

例如：&=Customers.CustomerID(group:merge)
### **skip**
在每个分组后跳过指定数量的行。

例如，&=Employees.EmployeeID(group:normal,skip:1)
### **subtotalN**
对与分组字段相关的特定字段数据执行摘要操作。N 代表 1 到 11 之间的数字，用于指定在数据列表中计算小计时使用的函数（1=平均值，2=计数，3=COUNTA，4=最大值，5=最小值......9=求和等）。有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

格式实际上规定为：
subtotalN:Ref 其中 Ref 指的是按分组列。

例如，

- &=Products.Units(subtotal9:Products.ProductID) 指定对 **Units** 字段的摘要函数，相对于 **Products** 表中的 **ProductID** 字段。
- &=Tabx.Col3(subtotal9:Tabx.Col1) 指定了表 Tabx 中以 **Col1** 分组的 **Col3** 字段的摘要函数。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB)指定了**Table1**中**ColumnD**字段通过**ColumnA**和**ColumnB**分组的摘要函数。

## **如何在智能标记中进行数据分组**

此示例展示了一些分组参数的实际应用。它使用了 Northwind.mdb Microsoft Access 数据库，并从名为 "Order Details" 的表中提取数据。我们在 Microsoft Excel 中创建了一个名为 SmartMarker_Designer.xls 的设计文件，并在工作表的各种单元格中放置智能标记。然后对标记进行处理以填充工作表。数据是通过一个组字段放置和组织的。

设计文件有两个工作表。在第一个工作表中，我们像下面的截图所示，使用了带有分组参数的智能标记。我们放置了三个带有分组参数的智能标记：
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID)，和
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) 分别放置在 A5、B5 和 C5。

|**SmartMarker_Designer.xls 文件中的第一个工作表，完整包含智能标记**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
在设计文件的第二个工作表中，我们像下图所示放置了一些智能标记。我们放置了以下智能标记：
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r)，和
&=subtotal9:Order Details.OrderID 分别放置在 A5、B5、C5、D5 和 C6。

|**SmartMarker_Designer.xls 文件的第二个工作表，显示混合智能标记。**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
以下是示例中使用的源代码。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

如果您需要向摘要行添加自定义标签，或者希望将字段名称与标签连接起来，例如"订单小计"，Aspose.Cells 提供了标签和标签位置属性，因此您可以在智能标记中放置自定义标签，同时与分组数据的小计行连接起来。请参阅有关如何向智能标记添加自定义标签以与小计行连接的文档。

{{% /alert %}} 
