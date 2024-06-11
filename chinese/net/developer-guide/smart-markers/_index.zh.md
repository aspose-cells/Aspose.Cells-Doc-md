---
title: 通过智能标记智能地导入并放置数据
linktitle: 智能标记
type: docs
weight: 190
url: /zh/net/using-smart-markers/
description: 根据模板Excel文件使用Aspose.Cells库智能地导入并放置数据
---


## **介绍**
**智能标记** 用于让 Aspose.Cells 知道在 Microsoft Excel 设计人员电子表格中放置什么信息。智能标记允许您创建只包含特定信息和格式的模板。
## **设计器电子表格和智能标记**
设计者电子表格是包含可视格式、公式和智能标记的标准 Excel 文件。它们可以包含引用一个或多个数据源的智能标记，例如来自项目和相关联系人信息的信息。智能标记被写入您希望信息放入的单元格中。

所有智能标记都以 &= 开头。数据标记的示例是 &=Party.FullName。如果数据标记结果超过一个项，例如一个完整的行，则接下来的行会被自动移动下来以为新信息腾出空间。因此，可以在数据标记后的行上立即放置小计和总计，以便根据插入的数据进行计算。要在插入行上进行计算，使用**动态公式**。

智能标记由**数据源**和**字段名称**部分组成。还可以使用变量和变量数组传递特殊信息。变量始终只填充一个单元格，而变量数组可以填充多个单元格。每个单元格只使用一个数据标记。未使用的智能标记将被移除。

智能标记还可以包含参数。参数允许您修改信息的布局方式。它们以逗号分隔的列表形式附加在智能标记的末尾作为括号内。
### **智能标记选项**
&=数据源.字段名称 
&=[数据源].[字段名称] 
&=$变量名 
&=$变量数组 
&==动态公式 
&=&=重复动态公式
### **参数**
允许以下参数：

- **noadd** - 不添加额外的行以适应数据。
- **skip:n** - 跳过每个数据行的n行。
- **ascending:n** 或 **descending:n** - 对智能标记中的数据进行排序。如果 n 为 1，则该列是排序器的第一个关键。在处理数据源后对数据进行排序。例如：&=Table1.Field3(ascending:1)。
- **horizontal** - 将数据从左至右书写，而不是从上至下。
- **numeric** - 如果可能的话，将文本转换为数字。
- **shift** - 下移或右移，创建额外的行或列以适应数据。shift参数的工作方式与Microsoft Excel中相同。例如，在Microsoft Excel中，当您选择一系列单元格，右键单击并选择**插入**，然后指定**下移单元格**、**右移单元格**和其他选项。简言之，**shift**参数在垂直/正常（自上而下）或水平（从左到右）的智能标记中具有相同的功能。
- **copystyle** - 将基本单元格的样式复制到该列中的所有单元格。

参数 noadd 和 skip 可以组合在一起，以在交替行中插入数据。因为模板是从底部到顶部进行处理的，所以应在第一行上添加 noadd 以避免在交替行之前插入额外行。

如果有多个参数，请用逗号分隔它们，但不要有空格：parameterA,parameterB,parameterC

以下屏幕截图显示了如何在每隔一行插入数据。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **动态公式**
动态公式允许您将 Excel 公式插入单元格，即使公式引用在导出过程中将被插入的行。动态公式可以针对每个插入的行重复，或者仅使用数据标记所在的单元格。

动态公式允许以下附加选项：

- r - 当前行数。
- 2、-1 - 相对于当前行数的偏移量。

例如:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

在动态公式标记中，“-1” 表示设置 B 列和 C 列的当前行偏移量，用于除法操作，skip 参数为一行。此外，我们应该指定以下字符:

{{< highlight java >}}

 "~"

{{< /highlight >}}

作为分隔符使用，以应用动态公式中的进一步参数。

以下截图展示了一个重复的动态公式以及生成的 Excel 工作表。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
单元格"C1"包含公式 **= A1*B1**，单元格"C2"包含 **= A2*B2**，单元格"C3"包含 **= A3*B3**。

处理智能标记非常简单。以下示例代码展示了如何在智能标记中使用动态公式。我们加载[模板文件](templateDynamicFormulas.xlsx)并创建测试数据，处理标记以填充数据到与标记相对应的单元格中。 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **使用可变数组**
以下示例代码展示了如何在智能标记中使用变量数组。我们将变量数组标记动态地放置到工作簿的第一个工作表的A1单元格中，其中包含我们为标记设置的值字符串，处理标记以将数据填充到标记的单元格中。最后，我们保存Excel文件。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **数据分组**
在一些 Excel 报告中，您可能需要将数据分成组，以便更容易阅读和分析。将数据分成组的主要目的之一是对每组记录运行计算（执行摘要操作）。

Aspose.Cells智能标记允许您按字段分组数据，并在数据集或数据组之间放置摘要行。例如，如果按Customers.CustomerID分组数据，可以在每次分组更改时添加摘要记录。
### **参数**
以下是用于数据分组的一些智能标记参数。
#### **group:normal/merge/repeat**
我们支持三种您可以选择的分组类型。

- **normal** - 分组字段的值不会为相应列中的记录重复；相反，它们每个数据组仅打印一次。
- **merge** - 与 normal 参数的行为相同，只是它合并了每个组集的分组字段单元格。
- **repeat** - 分组字段的值将为相应记录重复。

例如：&=Customers.CustomerID(group:merge)
#### **skip**
在每个分组后跳过指定数量的行。

例如，&=Employees.EmployeeID(group:normal,skip:1)
#### **subtotalN**
对与分组字段相关的特定字段数据执行摘要操作。N 代表 1 到 11 之间的数字，用于指定在数据列表中计算小计时使用的函数（1=平均值，2=计数，3=COUNTA，4=最大值，5=最小值......9=求和等）。有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

格式实际上规定为：
subtotalN:Ref 其中 Ref 指的是按分组列。

例如，

- &=Products.Units(subtotal9:Products.ProductID) 指定对 **Units** 字段的摘要函数，相对于 **Products** 表中的 **ProductID** 字段。
- &=Tabx.Col3(subtotal9:Tabx.Col1) 指定了表 Tabx 中以 **Col1** 分组的 **Col3** 字段的摘要函数。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB)指定了**Table1**中**ColumnD**字段通过**ColumnA**和**ColumnB**分组的摘要函数。

此示例展示了一些分组参数的实际应用。它使用了 Northwind.mdb Microsoft Access 数据库，并从名为 "Order Details" 的表中提取数据。我们在 Microsoft Excel 中创建了一个名为 SmartMarker_Designer.xls 的设计文件，并在工作表的各种单元格中放置智能标记。然后对标记进行处理以填充工作表。数据是通过一个组字段放置和组织的。

设计文件有两个工作表。在第一个工作表中，我们像下面的截图所示，使用了带有分组参数的智能标记。我们放置了三个带有分组参数的智能标记：
&=[Order Details].OrderID(group:merge,skip:1)，
&=[Order Details].Quantity(subtotal9:Order Details.OrderID)，和
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) 分别放置在 A5、B5 和 C5。

|**SmartMarker_Designer.xls 文件中的第一个工作表，完整包含智能标记**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
在设计文件的第二个工作表中，我们像下图所示放置了一些智能标记。我们放置了以下智能标记：
&=[Order Details].OrderID(group:normal)，
&=[Order Details].Quantity，
&=[Order Details].UnitPrice，
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
## **使用匿名类型或自定义对象**
Aspose.Cells 还支持智能标记中的匿名类型或自定义对象。接下来的示例展示了这是如何工作的。如需使用智能标记从动态对象导入数据，请访问以下文章：

[将动态对象导入作为数据源](/cells/zh/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **图像标记**
Aspose.Cells智能标记还支持图片标记。本节将向您展示如何使用智能标记插入图片。
### **图片参数**
管理图像的智能标记参数。

- **Picture:FitToCell** - 自动将图像适合到单元格的行高和列宽。
- **Picture:ScaleN** - 将高度和宽度按N百分比缩放。
- **Picture:Width:Nin和Height:Nin** - 将图像渲染为 N 英寸高和 N 英寸宽。您还可以指定左偏移量和顶部偏移量（以点为单位）。

以下是示例中使用的源代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **使用嵌套对象**
Aspose.Cells支持智能标记中的嵌套对象，这些嵌套对象应该是简单的。我们使用一个简单的模板文件。查看包含一些嵌套智能标记的设计电子表格。

|**SM_NestedObjects.xlsx文件的第一个工作表显示嵌套智能标记。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
以下示例演示了其工作原理。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **使用泛型列表作为嵌套对象**
Aspose.Cells现在还支持将通用列表用作嵌套对象。请查看生成的输出Excel文件的屏幕截图所用的代码。如屏幕截图所示，教师对象包含多个嵌套的学生对象。

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |




{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **使用智能标记的 HTML 属性**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **不逐行**
当前默认的处理方法是逐行处理智能标记。但有时需要一起处理同一数据表的智能标记，无论它们是否在同一行中，那么在调用处理之前，您必须指定名称为“_CellsSmartMarkers”的命名范围，并将WorkbookDesigner.LineByLine指定为false。 
有时可能会需要在完成前获取有关正在处理的单元格引用或特定智能标记的通知。这可以通过WorkbookDesigner.CallBack属性和ISmartMarkerCallBack实现。

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **在使用智能标记合并数据时获取通知**
将匿名或自定义对象添加到智能标记中

## **高级主题**
- [格式化智能标记](/cells/zh/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [如果数据太大，可以将智能标记数据自动填充到其他工作表](/cells/zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [为WorkbookDesigner设置自定义数据源](/cells/zh/net/formatting-smart-markers/)
- [在使用智能标记合并数据时获取通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/)
- [为WorkbookDesigner设置自定义数据源](/cells/zh/net/set-custom-datasource-for-workbookdesigner/)
- [在单元格中显示前导撇号](/cells/zh/net/show-leading-apostrophe-in-cells/)
- [在智能标记变量名为Test及其数据源名称也为Test中嵌入公式的下面样本代码是这样子的 **&=$Test(formula)**，在执行代码后，[最终的输出Excel文件](47153156.xlsx)将在A1到A5单元格中具有公式。](/cells/zh/net/using-formula-parameter-in-smart-marker-field/)
- [在智能标记中分组数据时使用Image Markers](/cells/zh/net/using-image-markers-while-grouping-data-in-smart-markers/)


