---
title: 使用智能标记
type: docs
weight: 40
url: /zh/java/using-smart-markers/
---

## **介绍**

{{% alert color="primary" %}}

**智能标记**用于让Aspose.Cells知道要在Microsoft Excel [设计器电子表格]中放置什么信息。智能标记允许您创建只包含相关信息和格式的模板。

{{% /alert %}}

## **设计器电子表格和智能标记**

设计器电子表格是包含可视格式、公式和智能标记的标准Excel文件。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。智能标记被写入您想要信息的单元格中。

所有智能标记都以&=开头。数据标记的示例是&=Party.FullName。如果数据标记导致多个条目，例如完整的一行，则自动将下面的行向下移动，以便为新信息腾出空间。因此，可以在数据标记后的行上放置小计和总计，以便根据插入的数据进行计算。要在插入的行上进行计算，请使用[动态公式]。

智能标记由**数据源**和**字段名称**部分组成。还可以使用变量和变量数组传递特殊信息。变量始终只填充一个单元格，而变量数组可以填充多个单元格。每个单元格只使用一个数据标记。未使用的智能标记将被移除。

智能标记还可以包含参数。参数允许您修改信息的布局方式。它们作为逗号分隔的列表附加到智能标记的后面。

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
- *ascending:n 或 descending:n* - 对智能标记中的数据进行排序。如果 n 为 1，则列是排序器的第一个键。数据源处理后进行排序。例如：&=Table1.Field3(ascending:1)。
- **horizontal** - 将数据从左至右书写，而不是从上至下。
- **numeric** - 如果可能的话，将文本转换为数字。
- **shift** - 向下或向右移动，创建额外的行或列以适应数据。shift 参数的工作方式与 Microsoft Excel 中的相同。例如，在 Microsoft Excel 中，当您选择一系列单元格、右键单击并选择 **Insert**，然后指定 **shift cells down**、**shift cells right** 和其他选项。简言之，shift 参数用于垂直/正常（自上而下）或水平（自左至右）智能标记的相同功能。
- **bean** - 表示数据源是一个简单的 POJO。仅在 Java API 中受支持。

参数 noadd 和 skip 可以结合在一起，在交替行上插入数据。因为模板是从底部到顶部处理的，所以您应该在第一行添加 noadd 以避免在交替行之前插入额外的行。

如果有多个参数，请用逗号分隔，但不要留空格：parameterA，parameterB，parameterC

以下屏幕截图显示了如何在每隔一行插入数据。

![todo:image_alt_text](using-smart-markers_1.png)

**变为...**

![todo:image_alt_text](using-smart-markers_2.png)

### **动态公式**

动态公式允许您将 Excel 公式插入单元格，即使公式引用在导出过程中将被插入的行。动态公式可以针对每个插入的行重复，或者仅使用数据标记所在的单元格。

动态公式允许以下附加选项：

- r - 当前行数。
- 2、-1 - 相对于当前行数的偏移量。

以下是一个重复动态公式和生成的 Excel 工作表的示例。

![todo:image_alt_text](using-smart-markers_3.png)

**变为...**

![todo:image_alt_text](using-smart-markers_4.png)

单元格 C1 包含公式 =A1*B1，C2 包含 = A2*B2，C3 包含 = A3*B3。

处理智能标记非常简单。以下示例代码展示了如何在智能标记中使用动态公式。我们加载[模板文件](templateDynamicFormulas.xlsx)并创建测试数据，处理标记以填充数据到与标记相对应的单元格中。 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **使用可变数组**

以下示例代码显示了如何在智能标记中使用可变数组。我们动态地将可变数组标记放入工作簿的第一个工作表的 A1 单元格中，它包含我们为标记设置的一系列值，处理标记以将数据填充到与标记相对应的单元格中。最后，我们保存 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **数据分组**

在一些 Excel 报告中，您可能需要将数据分成组，以便更容易阅读和分析。将数据分成组的主要目的之一是对每组记录运行计算（执行摘要操作）。

Aspose.Cells 智能标记允许您按字段集分组数据，并在数据集或数据组之间放置摘要行。例如，如果按 Customers.CustomerID 对数据进行分组，您可以在每次组变化时添加摘要记录。

### **参数**

以下是一些用于数据分组的智能标记参数。

#### **group:normal/merge/repeat**

我们支持三种您可以选择的分组类型。

- **normal** - 分组字段的值不会为相应列中的记录重复；相反，它们每个数据组仅打印一次。
- **merge** - 与 normal 参数的行为相同，只是它合并了每个组集的分组字段单元格。
- **repeat** - 分组字段的值将为相应记录重复。

例如：&=Customers.CustomerID(group:merge)

#### **skip**

在每个分组后跳过特定数量的行。

例如 &=Employees.EmployeeID(group:normal,skip:1)

#### **subtotalN**

对与分组字段相关的特定字段数据执行摘要操作。N 代表 1 到 11 之间的数字，用于指定在数据列表中计算小计时使用的函数（1=平均值，2=计数，3=COUNTA，4=最大值，5=最小值......9=求和等）。有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

格式实际上规定为：
subtotalN:Ref 其中 Ref 指的是按分组列。

例如，

- &=Products.Units(subtotal9:Products.ProductID) 指定对 **Units** 字段的摘要函数，相对于 **Products** 表中的 **ProductID** 字段。
- &=Tabx.Col3(subtotal9:Tabx.Col1) 指定了表 Tabx 中以 **Col1** 分组的 **Col3** 字段的摘要函数。
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定了表 Table1 中以 **ColumnA** 和 **ColumnB** 分组的 **ColumnD** 字段的摘要函数。

## **使用嵌套对象**

Aspose.Cells 支持智能标记中的嵌套对象，嵌套对象应该是简单的。

我们使用一个简单的模板文件。请查看包含一些嵌套智能标记的设计电子表格。

**设计文件的第一个工作表显示了嵌套智能标记。

![todo:image_alt_text](using-smart-markers_5.png)

下面的示例展示了这是如何工作的。运行下面的代码将得到下面的输出。

**输出文件的第一个工作表显示了结果数据。

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **使用泛型列表作为嵌套对象**

Aspose.Cells 现在还支持使用泛型列表作为嵌套对象。请查看使用以下代码生成的输出 Excel 文件的屏幕截图。如您在截图中所见，一个 Teacher 对象包含多个嵌套的 student 对象。

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **使用智能标记的 HTML 属性**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **在使用智能标记合并数据时获取通知**

有时，在完成之前可能需要获取有关正在处理的单元格引用或特定智能标记的通知。可以使用 [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) 属性和 [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) 来实现。

有关示例代码和详细解释，请参阅本文。

- [在使用智能标记合并数据时获取通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
