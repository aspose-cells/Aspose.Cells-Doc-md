---
title: 利用智能标记智能地导入和放置数据
linktitle: 智能标记
type: docs
weight: 190
url: /zh/net/using-smart-markers/
description: 使用Aspose.Cells库智能导入和根据模板Excel文件放置数据。
---


## **介绍**
**智能标记**用于让Aspose.Cells知道要将哪些信息放入Microsoft Excel设计器电子表格中。智能标记允许您创建仅包含特定信息和格式的模板。
## **设计器电子表格和智能标记**
设计器电子表格是包含视觉格式、公式和智能标记的标准Excel文件。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。将智能标记编写到要放置信息的单元格中。

所有智能标记都以&=开头。数据标记的示例是&=Party.FullName。如果数据标记导致多个项目，例如完整行，则其后的行会自动向下移动以腾出空间来放置新信息。因此，可以在数据标记后紧接着的行上放置小计和总计，以便根据插入的数据进行计算。要在插入行上进行计算，请使用**动态公式**。

智能标记由**数据源**和**字段名称**部分组成以获取大多数信息。特殊信息也可以通过变量和变量数组传递。变量总是只填充一个单元格，而变量数组可能填充多个。每个单元格只能使用一个数据标记。未使用的智能标记将被移除。

智能标记还可以包含参数。参数允许修改信息的布局方式。它们附加在智能标记的末尾，以逗号分隔的列表形式。
### **智能标记选项**
&=数据源.字段名称 
&=［数据源］。字段名称 
&=$变量名称 
&=$变量数组 
&==动态公式 
&=&=重复动态公式
### **参数**
允许使用以下参数：

- **noadd** - 不添加额外行以适应数据。
- **skip:n** - 跳过每行数据的n行。
- **ascending:n** 或 **descending:n** - 对智能标记中的数据进行排序。若n为1，则该列是排序器的第一个键。数据将在处理数据源后排序。例如：&=Table1.Field3(ascending:1)。
- **horizontal** - 将数据从左到右写入，而不是从上到下。
- **numeric** - 如有可能，将文本转换为数字。
- **shift** - 向下或向右移动，创建额外行或列以适应数据。Shift参数的工作方式与Microsoft Excel相同。例如，在Microsoft Excel中，当选择一系列单元格时，右键单击并选择**插入**，然后指定**向下移动单元格**、**向右移动单元格**或其他选项。简而言之，**shift**参数为垂直/普通（从上到下）或水平（从左到右）智能标记提供相同的功能。
- **copystyle** - 将基本单元格的样式复制到该列中的所有单元格。

noadd和skip参数可以组合使用以在交替行上插入数据。由于模板从底部到顶部处理，因此应在第一行上添加noadd以避免在交替行之前插入额外行。

如果有多个参数，请用逗号分隔它们，但不留空格：parameterA,parameterB,parameterC

以下屏幕截图展示如何在每隔一行插入数据。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **动态公式**
动态公式允许您在单元格中插入Excel公式，即使公式引用将在导出过程中插入的行。

动态公式允许以下额外选项:

- r - 当前行号。
- 2, -1 - 对当前行号的偏移。

例如:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

在动态公式标记中，“-1”分别表示在B列和C列中对当前行的偏移，用于除法运算，跳过参数为一行。此外，我们应指定以下字符:

{{< highlight java >}}

 "~"

{{< /highlight >}}

作为分隔字符，以应用动态公式中的进一步参数。

以下截图演示了重复的动态公式以及生成的Excel工作表。

|**模板文件**|**输出文件**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
单元格“C1”包含公式**= A1*B1**，单元格“C2”包含**= A2*B2**，单元格“C3”包含**= A3*B3**。

处理智能标记非常简单。以下示例代码显示了如何在智能标记中使用动态公式。我们加载 [模板文件](templateDynamicFormulas.xlsx) 并创建测试数据，处理标记以填充数据到单元格对应的标记中。 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **使用变量数组**
以下示例代码显示了如何在智能标记中使用变量数组。我们将一个变量数组标记动态放置在工作簿的第一个工作表的A1单元格中，其中包含我们为标记设置的值字符串，处理标记以填充数据到单元格对应的标记中。最后，我们保存Excel文件。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **分组数据**
在某些Excel报告中，您可能需要将数据分组以便更轻松地阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells智能标记允许您通过字段对数据进行分组，并在数据集或数据组之间放置汇总行。例如，如果通过Customers.CustomerID对数据进行分组，您可以在每次组更改时添加一个汇总记录。
### **参数**
以下是用于对数据进行分组的智能标记参数之一。
#### **group:normal/merge/repeat**
我们支持三种可供选择的分组类型。

- **normal** - 不会为相应列中的记录重复组的值; 而是每个数据组仅打印一次。
- **merge** - 与普通参数的行为相同，只不过它会合并每个组集的组合字段单元格。
- **repeat** - 为相应记录重复组的值。

例如: &=Customers.CustomerID(group:merge)
#### **skip**
在每个分组后跳过指定数量的行。

例如，&=Employees.EmployeeID(group:normal,skip:1)
#### **subtotalN**
对与分组字段相关的指定字段数据执行汇总运算。 N代表数字1到11之间的数字，用于指定在数据列表中计算小计时使用的函数。（1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SUM等）有关详细信息，请参阅Microsoft Excel帮助中的Subtotal参考。

实际格式如下:
subtotalN:Ref，其中Ref是分组依据的列。

例如,

- &=Products.Units(subtotal9:Products.ProductID) 指定在 **Products** 表中相对于 **ProductID** 字段汇总函数的 **Units** 字段。
- &=Tabx.Col3(subtotal9:Tabx.Col1) 指定在表 **Tabx** 中按 **Col1** 分组 **Col3** 字段的汇总函数。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定在表 **Table1** 中按 **ColumnA** 和 **ColumnB** 分组 **ColumnD** 字段的汇总函数。

这个示例展示了一些分组参数的实际应用。它使用了 Northwind.mdb 微软访问数据库，并从名为“Order Details”的表中提取数据。我们在 Microsoft Excel 中创建了一个名为 SmartMarker_Designer.xls 的设计文件，并将智能标记放置在工作表的各个单元格中。这些标记将被处理以填充工作表。数据将通过分组字段放置和组织。

设计文件有两个工作表。在第一个工作表中，我们按照以下截图所示放置了带有分组参数的智能标记。放置了三个带有分组参数的智能标记：
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), 和
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) 分别放在 A5、B5 和 C5 中。

|**SmartMarker_Designer.xls 文件中的第一个工作表，包含智能标记**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
在设计文件的第二个工作表中，我们按照下图所示放置了更多的智能标记。我们放置了以下智能标记：
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), 和
&=subtotal9:Order Details.OrderID 分别放置在 A5、B5、C5、D5 和 C6 中。

|**SmartMarker_Designer.xls 文件的第二个工作表，展示了混合的智能标记**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
这里是示例中使用的源代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

如果您需要向摘要行添加自定义标签，或者想要将字段的名称与标签连接起来，例如“订单小计”，Aspose.Cells 提供了 Label 和 LabelPosition 属性，因此您可以将自定义标签放置在智能标记中，同时与分组数据中的小计行连接起来。请参阅有关如何在智能标记中添加自定义标签以与小计行连接的文档。

{{% /alert %}} 
## **使用匿名类型或自定义对象**
Aspose.Cells 还支持智能标记中的匿名类型或自定义对象。以下示例展示了这是如何工作的。要使用智能标记从动态对象导入数据，请访问以下文章。

[将动态对象导入为数据源](/cells/zh/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **图像标记**
Aspose.Cells 智能标记还支持图像标记。本节介绍如何使用智能标记插入图片。
### **图像参数**
用于管理图像的智能标记参数。

- **Picture:FitToCell** - 将图像自适应到单元格的行高和列宽。
- **Picture:ScaleN** - 按 N 百分比缩放高度和宽度。
- **Picture:Width:Nin&Height:Nin** - 渲染图像为 N 英寸高，N 英寸宽。您还可以指定左侧和顶部位置（点数）。

这里是示例中使用的源代码。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **使用嵌套对象**
Aspose.Cells支持智能标记中的嵌套对象，这些嵌套对象应该是简单的。我们使用一个简单的模板文件。查看设计人员电子表格，其中包含一些嵌套的智能标记。

|**SM_NestedObjects.xlsx文件的第一个工作表显示了嵌套的智能标记。**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
接下来的示例显示了这是如何工作的。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **使用通用列表作为嵌套对象**
Aspose.Cells现在还支持将通用列表用作嵌套对象。请查看使用以下代码生成的输出Excel文件的屏幕截图。正如您在屏幕截图中看到的，一个Teacher对象包含多个嵌套的Student对象。

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |




{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **使用智能标记的HTML属性**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **非逐行**
当前的默认处理方法是逐行处理智能标记。但有时需要一起处理同一数据表的智能标记，无论它们是否在同一行中，然后您必须在调用处理之前指定命名范围"_CellsSmartMarkers"并将WorkbookDesigner.LineByLine指定为false。 
如果数据太大，则自动填充智能标记数据到其他工作表

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **在合并智能标记数据时获取通知**
有时，可能需要在完成之前获取有关正在处理的单元格引用或特定智能标记的通知。可以使用WorkbookDesigner.CallBack属性和ISmartMarkerCallBack实现这一点

## **高级主题**
- [将匿名对象或自定义对象添加到SmartMarkers](/cells/zh/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [如果数据太大，则自动填充智能标记数据到其他工作表。](/cells/zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [格式化智能标记](/cells/zh/net/formatting-smart-markers/)
- [在合并智能标记数据时获取通知](/cells/zh/net/getting-notifications-while-merging-data-with-smart-markers/)
- [为WorkbookDesigner设置自定义DataSource](/cells/zh/net/set-custom-datasource-for-workbookdesigner/)
- [在单元格中显示前导撇号](/cells/zh/net/show-leading-apostrophe-in-cells/)
- [在智能标记字段中使用Formula参数](/cells/zh/net/using-formula-parameter-in-smart-marker-field/)
- [在智能标记中分组数据时使用图片标记](/cells/zh/net/using-image-markers-while-grouping-data-in-smart-markers/)


