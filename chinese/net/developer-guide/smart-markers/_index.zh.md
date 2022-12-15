---
title: 使用智能标记智能导入和放置数据
linktitle: 智能标记
type: docs
weight: 190
url: /zh/net/using-smart-markers/
description: 根据模板Excel文件与Aspose.Cells库智能导入和放置数据。
---
## **介绍**
**智能标记**用于让 Aspose.Cells 知道在 Microsoft Excel 设计器电子表格中放置哪些信息。智能标记允许您创建仅包含特定信息和格式的模板。
## **设计师电子表格和智能标记**
Designer 电子表格是标准的 Excel 文件，其中包含视觉格式、公式和智能标记。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。智能标记被写入您需要信息的单元格中。

所有智能标记都以 &= 开头。 &=Party.FullName 是数据标记的示例。如果数据标记产生多个项目，例如，一个完整的行，则随后的行会自动向下移动以为新信息腾出空间。因此，小计和总计可以放在数据标记之后的行上，以根据插入的数据进行计算。要对插入的行进行计算，请使用**动态公式**.

智能标记包括**数据源**和**字段名称**大多数信息的部分。特殊信息也可以与变量和变量数组一起传递。变量始终只填充一个单元格，而变量数组可能填充多个单元格。每个细胞只使用一个数据标记。未使用的智能标记将被删除。

智能标记也可能包含参数。参数允许您修改信息的布局方式。它们作为逗号分隔列表附加到括号中的智能标记的末尾。
### **智能标记选项**
 &=数据源.字段名
&=[数据源].[字段名]&=$变量名
&=$变量数组
&==动态公式
&=&=重复动态公式
### **参数**
允许使用以下参数：

- **没有添加** 不要添加额外的行来适应数据。
- **跳过：n** - 为每行数据跳过 n 行。
- **升序：n**或者**降序：n** - 在智能标记中对数据进行排序。如果 n 为 1，则该列是排序器的第一个键。对数据源进行处理后对数据进行排序。例如：&=Table1.Field3(升序:1)。
- **水平的** 从左到右而不是从上到下写入数据。
- **数字** 如果可能，将文本转换为数字。
- **转移** 向下或向右移动，创建额外的行或列以适应数据。 shift 参数的工作方式与 Microsoft Excel 中的相同。例如在Microsoft Excel中，当您选择一个单元格区域时，右键单击并选择**插入**并指定**向下移动单元格**, **右移单元格**和其他选项。简而言之，**转移**参数为垂直/正常（从上到下）或水平（从左到右）智能标记填充相同的功能。
- **文案风格** 将基本单元格的样式复制到该列中的所有单元格。

可以组合参数 noadd 和 skip 以在交替行上插入数据。因为模板是从下往上处理的，所以你应该在第一行添加noadd以避免在备用行之前插入额外的行。

如果您有多个参数，请用逗号分隔它们，但不要使用空格：parameterA,parameterB,parameterC

以下屏幕截图显示了如何每隔一行插入数据。

|**模板文件**|**输出文件**|
|:- |:- |
|![待办事项：图像_替代_文本](using-smart-markers_1.jpg)|![待办事项：图像_替代_文本](using-smart-markers_2.jpg)|
### **动态公式**
动态公式允许您将 Excel 公式插入到单元格中，即使公式引用了将在导出过程中插入的行。动态公式可以为每个插入的行重复或仅使用放置数据标记的单元格。

动态公式允许以下附加选项：

- r - 当前行号。
- 2, -1 - 当前行号的偏移量。

例如：

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

在动态公式标记中，“-1”分别表示B列和C列到当前行的偏移量，将设置除法运算，skip参数为一行。此外，我们应该指定以下字符：

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

作为分隔符以在动态公式中应用更多参数。

以下屏幕截图说明了一个重复的动态公式和生成的 Excel 工作表。

|**模板文件**|**输出文件**|
|:- |:- |
|![待办事项：图像_替代_文本](using-smart-markers_3.jpg)|![待办事项：图像_替代_文本](using-smart-markers_4.jpg)|
Cell “C1”包含公式**A1*B1** ，单元格“C2”包含**A2*B2**单元格“C3”包含**A3*B3**.

处理智能标记非常容易。下面是两个代码片段，一个在 C# 中，一个在 VB 中，展示了它是如何完成的。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **使用变量数组**
以下示例代码显示了如何在智能标记中使用变量数组。我们将一个可变数组标记动态地放入工作簿的第一个工作表的 A1 单元格中，其中包含我们为标记设置的字符串值，处理标记以将数据填充到针对标记的单元格中。最后我们保存 Excel 文件。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **分组数据**
在某些 Excel 报告中，您可能需要将数据分组以使其更易于阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells 智能标记允许您按字段对数据进行分组，并在数据集或数据组之间放置汇总行。例如，如果按 Customers.CustomerID 对数据进行分组，您可以在每次组更改时添加一条摘要记录。
### **参数**
以下是一些用于分组数据的智能标记参数。
#### **组：正常/合并/重复**
我们支持三种类型的组，您可以在其中进行选择。

- **普通的** group by field(s) 值对于列中的相应记录不重复；相反，它们每个数据组打印一次。
- **合并** 与正常参数相同的行为，除了它按每个组集的字段合并组中的单元格。
- **重复** 对相应记录重复按字段分组的值。

例如：&=Customers.CustomerID(group:merge)
#### **跳过**
在每组之后跳过指定数量的行。

例如，&=Employees.EmployeeID(group:normal,skip:1)
#### **小计N**
对group by字段相关的指定字段数据进行汇总操作。 N 表示 1 到 11 之间的数字，指定在计算数据列表中的小计时使用的函数。 （1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM 等）有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

格式实际上声明为：
subtotalN:Ref 其中 Ref 指的是按列分组。

例如，

-  &=Products.Units(subtotal9:Products.ProductID) 指定汇总函数**单位**领域相对于**产品编号**中的字段**产品**桌子。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) 指定汇总函数**列3**字段分组依据**列1**在表中**制表符**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定汇总函数**D列**字段分组依据**列A**和**B列**在表中**表格1**.

此示例显示了一些实际的分组参数。它使用 Northwind.mdb Microsoft Access 数据库并从名为“Order Details”的表中提取数据。我们在 Microsoft Excel 中创建一个名为 SmartMarker_Designer.xls 的设计器文件，并将智能标记放入工作表中的各个单元格中。处理标记以填充工作表。数据按组字段放置和组织。

设计器文件有两个工作表。首先，我们放置带有分组参数的智能标记，如下面的屏幕截图所示。放置了三个智能标记（带有分组参数）：
&=[订单详情].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), and
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID)分别进入A5、B5、C5。

|**SmartMarker_Designer.xls 文件中的第一个工作表，包含智能标记**|
|:- |
|![待办事项：图像_替代_文本](using-smart-markers_5.png)|
在设计器文件的第二个工作表中，我们放置了一些更智能的标记，如下图所示。我们放置以下智能标记：
&=[订单详情].OrderID(group:normal),
&=[订单详情].数量,
&=[订单详情].UnitPrice,
&=&=B(r)*C(r), 和
&=subtotal9:Order Details.OrderID分别为A5、B5、C5、D5、C6。

|**SmartMarker_Designer.xls 文件的第二个工作表，显示混合的智能标记。**|
|:- |
|![待办事项：图像_替代_文本](using-smart-markers_6.png)|
这是示例中使用的源代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

如果您需要将自己的自定义标签添加到摘要行，或者您想要将字段的名称与标签连接起来，例如“订单小计”，Aspose.Cells 为您提供了 Label 和 LabelPosition 属性，因此您可以将自定义标签放在 Smart在分组数据中与小计行连接时的标记。请参阅有关如何添加自定义标签以与智能标记中的小计行连接的文档以供参考。

{{% /alert %}} 
## **使用匿名类型或自定义对象**
Aspose.Cells 还支持智能标记中的匿名类型或自定义对象。下面的示例显示了它是如何工作的。要使用智能标记从动态对象导入数据，请访问以下文章：

[从动态对象导入作为数据源](/cells/zh/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **图像标记**
Aspose.Cells 智能标记也支持图像标记。本节介绍如何使用智能标记插入图片。
### **图像参数**
用于管理图像的智能标记参数。

- **图片：FitToCell** - 使图像自动适合单元格的行高和列宽。
- **图片：ScaleN** - 将高度和宽度缩放到 N%。
- **图片：宽：无&高：无** 渲染图像 N 英寸高和 N 英寸宽。您还可以指定左侧和顶部位置（以磅为单位）。

这是示例中使用的源代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **使用嵌套对象**
Aspose.Cells 智能标记支持嵌套对象，嵌套对象要简单。我们使用一个简单的模板文件。请参阅包含一些嵌套智能标记的设计器电子表格。

|**SM_NestedObjects.xlsx 文件的第一个工作表显示了嵌套的智能标记。**|
|:- |
|![待办事项：图像_替代_文本](using-smart-markers_7.png)|
下面的例子展示了它是如何工作的。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **使用通用列表作为嵌套对象**
Aspose.Cells 现在也支持使用通用列表作为嵌套对象。请检查使用以下代码生成的输出 excel 文件的屏幕截图。正如您在屏幕截图中看到的，一个 Teacher 对象包含多个嵌套的 Student 对象。

|![待办事项：图像_替代_文本](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **使用智能标记的 HTML 属性**
以下示例代码解释了智能标记的 HTML 属性的使用。处理时，由于 HTML，它会将“Hello World”中的“World”显示为粗体<b>标签。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **不是一行一行**
目前默认的处理方式是逐行处理smartmaker。但是有时候同一个数据表的智能标记需要一起处理，不管
如果它们是否在同一行中，则必须在调用处理之前指定命名范围“_CellsSmartMarkers”并将 WorkbookDesigner.LineByLine 指定为 false。

|![待办事项：图像_替代_文本](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **使用智能标记合并数据时获取通知**
有时，可能需要在完成之前获得有关单元格引用或正在处理的特定智能标记的通知。这可以使用 WorkbookDesigner.CallBack 属性和 ISmartMarkerCallBack 来实现

## **推进主题**
- [将匿名或自定义对象添加到 SmartMarkers](/cells/zh/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [如果数据太大，自动将智能标记数据填充到其他工作表](/cells/zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [格式化智能标记](/cells/zh/net/formatting-smart-markers/)
- [使用智能标记合并数据时获取通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/)
- [为 WorkbookDesigner 设置自定义数据源](/cells/zh/net/set-custom-datasource-for-workbookdesigner/)
- [在单元格中显示前导撇号](/cells/zh/net/show-leading-apostrophe-in-cells/)
- [在智能标记字段中使用公式参数](/cells/zh/net/using-formula-parameter-in-smart-marker-field/)
- [在智能标记中分组数据时使用图像标记](/cells/zh/net/using-image-markers-while-grouping-data-in-smart-markers/)


