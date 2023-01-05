---
title: 使用智能标记
type: docs
weight: 40
url: /zh/java/using-smart-markers/
---
## **介绍**

{{% alert color="primary" %}}

**智能标记**用于让 Aspose.Cells 知道在 Microsoft Excel 中放置什么信息[设计师电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/).智能标记允许您创建仅包含相关信息和格式的模板。

{{% /alert %}}

## **设计师电子表格和智能标记**

Designer 电子表格是标准的 Excel 文件，其中包含视觉格式、公式和智能标记。它们可以包含引用一个或多个数据源的智能标记，例如来自项目的信息和相关联系人的信息。智能标记被写入您需要信息的单元格中。

所有智能标记都以 &= 开头。 &=Party.FullName 是数据标记的示例。如果数据标记产生多个项目，例如，一个完整的行，则随后的行会自动向下移动以为新信息腾出空间。因此，小计和总计可以放在数据标记之后的行上，以根据插入的数据进行计算。要对插入的行进行计算，请使用[动态公式](/cells/zh/java/using-smart-markers/#dynamic-formulas).

智能标记包括**数据源**和**字段名称**大多数信息的部分。特殊信息也可以与变量和变量数组一起传递。变量始终只填充一个单元格，而变量数组可能填充多个单元格。每个细胞只使用一个数据标记。未使用的智能标记将被删除。

智能标记还可以包含参数。参数允许您修改信息的布局方式。它们作为逗号分隔列表附加到括号中的智能标记的末尾。

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
- *ascending:n 或 descending:n - 对智能标记中的数据进行排序。如果 n 为 1，则该列是排序器的第一个键。对数据源进行处理后对数据进行排序。例如：&=Table1.Field3(升序:1)。
- **水平的** 从左到右而不是从上到下写入数据。
- **数字** 如果可能，将文本转换为数字。
- **转移** 向下或向右移动，创建额外的行或列以适应数据。 shift 参数的工作方式与 Microsoft Excel 中的相同。例如在Microsoft Excel中，当您选择一个单元格区域时，右键单击并选择**插入**并指定**向下移动单元格**, **右移单元格**和其他选项。简而言之，shift 参数为垂直/正常（从上到下）或水平（从左到右）智能标记填充相同的功能。
- **豆** 表示数据源是一个简单的 POJO。仅在 Java API 支持。

可以组合参数 noadd 和 skip 以在交替行上插入数据。因为模板是从下往上处理的，所以应该在第一行添加noadd，避免在备用行之前插入额外的行。

如果您有多个参数，请用逗号分隔它们，但不要使用空格：parameterA,parameterB,parameterC

以下屏幕截图显示了如何每隔一行插入数据。

![待办事项：图片_替代_文本](using-smart-markers_1.png)

**变成...**

![待办事项：图片_替代_文本](using-smart-markers_2.png)

### **动态公式**

动态公式允许您将 Excel 公式插入到单元格中，即使公式引用了将在导出过程中插入的行。动态公式可以为每个插入的行重复或仅使用放置数据标记的单元格。

动态公式允许以下附加选项：

- r - 当前行号。
- 2, -1 - 当前行号的偏移量。

下面说明了一个重复的动态公式和生成的 Excel 工作表。

![待办事项：图片_替代_文本](using-smart-markers_3.png)

**变成……**

![待办事项：图片_替代_文本](using-smart-markers_4.png)

Cell C1包含公式=A1*B1，C2包含= A2*B2 和 C3 = A3*B3。

处理智能标记非常容易。以下代码片段显示了它是如何完成的。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **使用变量数组**

以下示例代码显示了如何在智能标记中使用变量数组。我们将一个可变数组标记动态地放入工作簿的第一个工作表的 A1 单元格中，其中包含我们为标记设置的一串值，处理标记以将数据填充到针对标记的单元格中。最后，我们保存 Excel 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **分组数据**

在某些 Excel 报告中，您可能需要将数据分组以使其更易于阅读和分析。将数据分组的主要目的之一是对每组记录运行计算（执行汇总操作）。

Aspose.Cells 智能标记允许您按字段集对数据进行分组，并在数据集或数据组之间放置摘要行。例如，如果按 Customers.CustomerID 对数据进行分组，您可以在每次组更改时添加一条摘要记录。

### **参数**

以下是一些用于分组数据的智能标记参数。

#### **组：正常/合并/重复**

我们支持三种类型的组，您可以在其中进行选择。

- **普通的** group by field(s) 值对于列中的相应记录不重复；相反，它们每个数据组打印一次。
- **合并** 与正常参数相同的行为，除了它按每个组集的字段合并组中的单元格。
- **重复** 对相应记录重复按字段分组的值。

例如：&=Customers.CustomerID(group:merge)

#### **跳过**

在每组之后跳过特定数量的行。

例如 &=Employees.EmployeeID(group:normal,skip:1)

#### **小计N**

对group by字段相关的指定字段数据进行汇总操作。 N 表示 1 到 11 之间的数字，指定在计算数据列表中的小计时使用的函数。 （1=AVERAGE、2=COUNT、3=COUNTA、4=MAX、5=MIN、...9=SUM 等）有关详细信息，请参阅 Microsoft Excel 帮助中的小计参考。

格式实际上声明为：
subtotalN:Ref 其中 Ref 指的是按列分组。

例如，

-  &=Products.Units(subtotal9:Products.ProductID) 指定汇总函数**单位**领域相对于**产品编号**中的字段**产品**桌子。
-  &=Tabx.Col3(subtotal9:Tabx.Col1) 指定汇总函数**列3**字段分组依据**列1**在表中**制表符**.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) 指定汇总函数**D列**字段分组依据**列A**和**B列**在表中**表格1**.

## **使用嵌套对象**

Aspose.Cells 智能标记支持嵌套对象，嵌套对象要简单。

我们使用一个简单的模板文件。请参阅包含一些嵌套智能标记的设计器电子表格。

**显示嵌套智能标记的设计器文件的第一个工作表。**

![待办事项：图片_替代_文本](using-smart-markers_5.png)

下面的例子展示了它是如何工作的。运行下面的代码会产生下面的输出。

**显示结果数据的输出文件的第一个工作表。**

![待办事项：图片_替代_文本](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **使用通用列表作为嵌套对象**

Aspose.Cells 现在也支持使用通用列表作为嵌套对象。请检查使用以下代码生成的输出 excel 文件的屏幕截图。正如您在屏幕截图中看到的，一个教师对象包含多个嵌套的学生对象。

![待办事项：图片_替代_文本](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **使用智能标记的 HTML 属性**

以下示例代码解释了智能标记的 HTML 属性的用法。当它被处理时，它会将“Hello World”中的“World”显示为粗体，因为 HTML \<b>标签。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **使用智能标记合并数据时获取通知**

有时，可能需要在完成之前获得有关单元格引用或正在处理的特定智能标记的通知。这可以通过使用[**工作簿设计器.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)财产和[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

示例代码和详细解释请看这篇文章。

- [使用智能标记合并数据时获取通知](/cells/zh/java/getting-notifications-while-merging-data-with-smart-markers/)
