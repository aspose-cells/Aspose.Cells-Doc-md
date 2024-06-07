---
title: 使用智能标记
type: docs
weight: 40
url: /zh/java/using-smart-markers/
---

## **介绍**

{{% alert color="primary" %}}

**智能标记**用于让Aspose.Cells知道要在Microsoft Excel [设计者电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)中放置什么信息。智能标记允许您创建仅包含相关信息和格式的模板。

{{% /alert %}}

## **设计器电子表格和智能标记**

设计者电子表格是包含视觉格式、公式和智能标记的标准Excel文件。它们可以包含引用一个或多个数据源的智能标记，例如项目信息和相关联系人信息。智能标记在您希望获取信息的单元格中编写。

所有智能标记均以&=开始。数据标记的示例是&=Party.FullName。如果数据标记产生多个项目，例如一整行，则随后的行会自动下移，以腾出空间放置新信息。因此，可以在紧随数据标记的行上放置小计和总计，以便基于插入数据进行计算。要对插入的行进行计算，请使用[动态公式](/cells/zh/java/using-smart-markers/#dynamic-formulas)。

智能标记由**数据源**和**字段名称**部分组成以获取大多数信息。特殊信息也可以通过变量和变量数组传递。变量总是只填充一个单元格，而变量数组可能填充多个。每个单元格只能使用一个数据标记。未使用的智能标记将被移除。

智能标记也可以包含参数。参数允许您修改信息的布局方式。它们以逗号分隔的列表附加到智能标记的末尾括号中。

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
- *ascending:n 或 descending:n* - 对智能标记中的数据进行排序。如果n为1，那么该列是排序器的第一个键。在处理数据源后对数据进行排序。例如：&=Table1.Field3(ascending:1)。
- **horizontal** - 将数据从左到右写入，而不是从上到下。
- **numeric** - 如有可能，将文本转换为数字。
- **shift** - 向下或向右移动，创建额外的行或列以适应数据。shift参数的工作方式与Microsoft Excel相同。例如在Microsoft Excel中，当选择一系列单元格，右键单击并选择**插入**，然后指定**向下移动单元格**、**向右移动单元格**和其他选项。简而言之，shift参数对垂直/正常（从上到下）或水平（从左到右）的智能标记填充相同的功能。
- **bean** - 表示数据源是简单的POJO。仅在Java API中受支持。

noadd和skip参数可以组合，以在交替行中插入数据。由于模板是由底部到顶部处理的，因此应在第一行上添加noadd以避免在交替行之前插入额外的行。

如果有多个参数，请使用逗号而没有空格进行分隔：parameterA,parameterB,parameterC

以下屏幕截图展示如何在每隔一行插入数据。

![todo:image_alt_text](using-smart-markers_1.png)

**变成...**

![todo:image_alt_text](using-smart-markers_2.png)

### **动态公式**

动态公式允许您在单元格中插入Excel公式，即使公式引用将在导出过程中插入的行。

动态公式允许以下额外选项:

- r - 当前行号。
- 2, -1 - 对当前行号的偏移。

以下是一个重复动态公式以及生成的Excel工作表的示例。

![todo:image_alt_text](using-smart-markers_3.png)

**变成…**

![todo:image_alt_text](using-smart-markers_4.png)

单元格C1包含公式=A1*B1，C2包含=A2*B2，C3包含=A3*B3。

处理智能标记非常简单。以下示例代码显示了如何在智能标记中使用动态公式。我们加载 [模板文件](templateDynamicFormulas.xlsx) 并创建测试数据，处理标记以填充数据到单元格对应的标记中。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **使用变量数组**

以下示例代码演示了如何在智能标记中使用变量数组。我们将动态地将变量数组标记放入工作簿的第一个工作表的单元格A1中，该数组包含我们为标记设置的一组值，处理标记以填充单元格中的数据。最后，我们保存Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **分组数据**

在某些Excel报告中，您可能需要将数据分组以便更轻松地阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells智能标记允许您按设置的字段对数据进行分组，并在数据集或数据组之间放置摘要行。例如，如果按Customers.CustomerID对数据进行分组，您可以在每次组更改时添加摘要记录。

### **参数**

以下是用于分组数据的一些智能标记参数。

#### **group:normal/merge/repeat**

我们支持三种可供选择的分组类型。

- **normal** - 不会为相应列中的记录重复组的值; 而是每个数据组仅打印一次。
- **merge** - 与普通参数的行为相同，只不过它会合并每个组集的组合字段单元格。
- **repeat** - 为相应记录重复组的值。

例如: &=Customers.CustomerID(group:merge)

#### **skip**

在每个组后跳过特定数量的行。

例如&=Employees.EmployeeID(group:normal,skip:1)

#### **subtotalN**

对与分组字段相关的指定字段数据执行汇总运算。 N代表数字1到11之间的数字，用于指定在数据列表中计算小计时使用的函数。（1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SUM等）有关详细信息，请参阅Microsoft Excel帮助中的Subtotal参考。

实际格式如下:
subtotalN:Ref，其中Ref是分组依据的列。

例如,

- &=Products.Units(subtotal9:Products.ProductID) 指定在 **Products** 表中相对于 **ProductID** 字段汇总函数的 **Units** 字段。
- &=Tabx.Col3(subtotal9:Tabx.Col1) 指定在表 **Tabx** 中按 **Col1** 分组 **Col3** 字段的汇总函数。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定在表Table1中，按ColumnA和ColumnB对ColumnD字段分组的摘要函数。

## **使用嵌套对象**

Aspose.Cells支持智能标记中的嵌套对象，嵌套对象应该是简单的。

我们使用一个简单的模板文件。 请参阅包含一些嵌套智能标记的设计电子表格。

**设计师文件的第一个工作表展示了嵌套的智能标记。**

![todo:image_alt_text](using-smart-markers_5.png)

下面的示例将展示其工作原理。 运行下面的代码会得到以下输出。

**输出文件的第一个工作表展示了结果数据。**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **使用通用列表作为嵌套对象**

Aspose.Cells 现在还支持将泛型列表作为嵌套对象使用。请检查使用以下代码生成的输出 Excel 文件的屏幕截图。从屏幕截图中可以看到，一个 Teacher 对象包含多个嵌套的 student 对象。

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **使用智能标记的HTML属性**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **在合并智能标记数据时获取通知**

有时，可能需要在完成之前获取有关正在处理的单元格引用或特定智能标记的通知。这可以通过 [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) 属性和 [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) 来实现

有关示例代码和详细解释，请参阅此文章。

- [在合并智能标记数据时获取通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/)
