---
title: 使用智能标记
type: docs
weight: 40
url: /zh/java/using-smart-markers/
---
##  **介绍**

{{% alert color="primary" %}}

**智能标记**用于让 Aspose.Cells 知道要在 Microsoft Excel 中放置哪些信息[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/)。智能标记允许您创建仅包含相关信息和格式的模板。

{{% /alert %}}

##  **设计电子表格和智能标记**

设计器电子表格是标准 Excel 文件，包含可视格式、公式和智能标记。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。智能标记被写入您需要信息的单元格中。

所有智能标记均以 &= 开头。数据标记的示例是 &=Party.FullName。如果数据标记产生多个项目（例如，完整的行），则后面的行会自动下移，以为新信息腾出空间。因此，可以将小计和总计放置在紧接数据标记之后的行上，以根据插入的数据进行计算。要对插入的行进行计算，请使用[动态公式](/cells/zh/java/using-smart-markers/#dynamic-formulas).

智能标记包括**数据源**和**字段名称**大多数信息的部分。特殊信息也可以通过变量和变量数组传递。变量总是只填充一个单元格，而变量数组可能填充多个单元格。每个单元格仅使用一个数据标记。未使用的智能标记将被删除。

智能标记还可以包含参数。参数允许您修改信息的布局方式。它们作为逗号分隔列表附加到智能标记末尾的括号中。

###  **智能标记选项**

&=数据源.字段名称
&=[数据源].[字段名称]
&=$变量名
&=$VariableArray
&==动态公式
&=&=重复动态公式

###  **参数**

允许使用以下参数：

- **无添加** 不要添加额外的行来适应数据。
- **跳过：n** - 每行数据跳过 n 行。
- *升序：n 或降序：n - 对智能标记中的数据进行排序。如果 n 为 1，则该列是排序器的第一个键。对数据源进行处理后，对数据进行排序。例如：&=Table1.Field3(升序：1)。
- **水平的** 从左到右写入数据，而不是从上到下。
- **数字** 如果可能，将文本转换为数字。
- **转移** 向下或向右移动，创建额外的行或列以适应数据。移位参数的工作方式与 Microsoft Excel 中的相同。例如，在 Microsoft Excel 中，当您选择单元格区域时，右键单击并选择**插入**并指定**向下移动单元格**，**向右移动单元格**和其他选项。简而言之，shift 参数对于垂直/正常（从上到下）或水平（从左到右）智能标记具有相同的功能。
- **豆** 表示数据源是一个简单的POJO。仅在 Java API 中受支持。

参数 noadd 和skip 可以组合起来在交替的行上插入数据。由于模板是从下到上处理的，因此您应该在第一行添加 noadd 以避免在备用行之前插入额外的行。

如果有多个参数，请用逗号分隔，但不能使用空格：parameterA,parameterB,parameterC

以下屏幕截图显示了如何每隔一行插入数据。

![待办事项：图像_替代_文本](using-smart-markers_1.png)

**变成...**

![待办事项：图像_替代_文本](using-smart-markers_2.png)

###  **动态公式**

动态公式允许您将 Excel 公式插入到单元格中，即使公式引用将在导出过程中插入的行也是如此。动态公式可以对每个插入的行重复或仅使用放置数据标记的单元格。

动态公式允许以下附加选项：

- r - 当前行号。
- 2、-1 - 到当前行号的偏移量。

下面说明了重复的动态公式和生成的 Excel 工作表。

![待办事项：图像_替代_文本](using-smart-markers_3.png)

**变成……**

![待办事项：图像_替代_文本](using-smart-markers_4.png)

Cell C1 包含公式 =A1*B1，C2 包含 = A2*B2 和 C3 = A3*B3。

处理智能标记非常容易。以下示例代码显示了如何在智能标记中使用动态公式。我们加载[模板文件](templateDynamicFormulas.xlsx)并创建测试数据，处理标记以根据标记将数据填充到单元格中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **使用变量数组**

以下示例代码展示了如何在智能标记中使用变量数组。我们动态地将一个变量数组标记放入工作簿第一个工作表的 A1 单元格中，其中包含我们为标记设置的一串值，处理标记以将数据填充到标记的单元格中。最后，我们保存Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **数据分组**

在某些 Excel 报告中，您可能需要将数据分成几组，以便于阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells 智能标记允许您按字段集对数据进行分组，并将汇总行放置在数据集或数据组之间。例如，如果按 Customers.CustomerID 对数据进行分组，则可以在每次组更改时添加摘要记录。

###  **参数**

以下是一些用于对数据进行分组的智能标记参数。

####  **组：正常/合并/重复**

我们支持三种类型的群组，您可以选择。

- **普通的** 列中相应记录的分组依据字段值不会重复；相反，它们每个数据组打印一次。
- **合并** 与正常参数的行为相同，不同之处在于它会合并每个组集的字段分组中的单元格。
- **重复** 对相应记录重复按字段值分组。

例如：&=Customers.CustomerID(group:merge)

####  **跳过**

在每组之后跳过特定数量的行。

例如 &=Employees.EmployeeID(group:normal,skip:1)

####  **小计N**

对与group by字段相关的指定字段数据进行汇总操作。 N 代表 1 到 11 之间的数字，指定计算数据列表中小计时使用的函数。 （1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM 等）有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

该格式实际上表示为：
subtotalN:Ref 其中 Ref 指的是按列分组。

例如，

-  &=Products.Units(subtotal9:Products.ProductID) 指定汇总函数**单位**场关于**产品ID**领域中的**产品**桌子。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) 指定汇总函数**第3栏**字段分组依据**第 1 列**在表 *Tabx** 中。
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定汇总函数**D栏**字段分组依据**A列**和**B栏**在表*表1**中。

##  **使用嵌套对象**

Aspose.Cells 支持智能标记中的嵌套对象，嵌套对象应该很简单。

我们使用一个简单的模板文件。请参阅包含一些嵌套智能标记的设计器电子表格。

**显示嵌套智能标记的设计器文件的第一个工作表。**

![待办事项：图像_替代_文本](using-smart-markers_5.png)

下面的示例展示了其工作原理。运行下面的代码会产生下面的输出。

**输出文件的第一个工作表显示结果数据。**

![待办事项：图像_替代_文本](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **使用通用列表作为嵌套对象**

Aspose.Cells 现在还支持使用通用列表作为嵌套对象。请检查使用以下代码生成的输出 Excel 文件的屏幕截图。正如您在屏幕截图中看到的，教师对象包含多个嵌套的学生对象。

![待办事项：图像_替代_文本](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **使用智能标记的 HTML 属性**

以下示例代码解释了智能标记的 HTML 属性的使用。处理时，会将“Hello World”中的“World”显示为粗体，因为 HTML \<b>标签。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **将数据与智能标记合并时获取通知**

有时，可能需要在完成之前获取有关单元格引用或正在处理的特定智能标记的通知。这可以通过使用来实现[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)财产和[**智能标记回调**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

示例代码和详细解释请参见这篇文章。

- [将数据与智能标记合并时获取通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/)
