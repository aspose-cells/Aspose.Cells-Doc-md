---
title: 数据验证
type: docs
weight: 90
url: /zh/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel 提供了一些很好的功能来自动筛选或验证工作表数据。Aspose.Cells 完全支持 Microsoft Excel 的数据验证和自动筛选功能。本文介绍如何使用 Microsoft Excel 中的功能，以及如何使用 Aspose.Cells 对其进行编码。

{{% /alert %}}

## **数据验证类型和执行**

数据验证是设置与在工作表上输入的数据有关的规则的能力。例如，使用验证来确保标记为 DATE 的列仅包含日期，或者另一列仅包含数字。您甚至可以确保标记为 DATE 的列仅包含特定范围内的日期。通过数据验证，您可以控制在工作表的单元格中输入的内容。

Microsoft Excel 支持多种不同类型的数据验证。每种类型用于控制将什么类型的数据输入单元格或单元格范围。下面的代码片段说明了如何验证这一点：

- 数字是整数，也就是说，它们没有小数部分。
- 小数遵循正确的结构。代码示例定义了一系列单元格应该有两个小数位。
- 值仅限于值列表。列表验证定义可应用于单元格或单元格区域的单独值列表。
- 日期在特定范围内。
- 时间在特定范围内。
- 文本在给定的字符长度内。

### **使用 Microsoft Excel 进行数据验证**

使用 Microsoft Excel 创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 来自**数据**菜单，选择**验证**.将显示验证对话框。
1. 点击**设置**选项卡并输入设置。

### **使用 Aspose.Cells 进行数据验证**

数据验证是一项强大的功能，用于验证输入到工作表中的信息。通过数据验证，开发人员可以为用户提供选择列表，将数据条目限制为特定类型或大小等。
在 Aspose.Cells 中，每个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类有一个[**验证**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)代表集合的属性[**验证**](https://reference.aspose.com/cells/net/aspose.cells/validation)对象。要设置验证，请设置一些[**验证**](https://reference.aspose.com/cells/net/aspose.cells/validation)类的属性如下：

- 类型——表示验证类型，可以通过使用中的预定义值之一来指定[**验证类型**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)枚举。
- 运算符 - 表示要在验证中使用的运算符，可以通过使用中的预定义值之一来指定[**运算符类型**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)枚举。
- Formula1 – 表示与数据验证的第一部分关联的值或表达式。
- Formula2 – 表示与数据验证的第二部分关联的值或表达式。

当。。。的时候[**验证**](https://reference.aspose.com/cells/net/aspose.cells/validation)对象的属性已经配置好，开发者可以使用[**单元格区域**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)结构来存储有关将使用创建的验证进行验证的单元格范围的信息。

#### **数据验证类型**

这[**验证类型**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)枚举有以下成员：

|**成员名字**|**描述**|
|:- |:- |
|任意值|表示任何类型的值。|
|完整的号码|表示整数的验证类型。|
|十进制|表示十进制数的验证类型。|
|列表|表示下拉列表的验证类型。|
|日期|表示日期的验证类型。|
|时间|表示时间的验证类型。|
|文本长度|表示文本长度的验证类型。|
|风俗|表示自定义验证类型。|

##### **整数数据验证**

通过这种类型的验证，用户只能将指定范围内的整数输入到已验证的单元格中。下面的代码示例展示了如何实现 WholeNumber 验证类型。该示例使用我们在上面使用 Microsoft Excel 创建的 Aspose.Cells 创建相同的数据验证。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **列表数据验证**

这种类型的验证允许用户从下拉列表中输入值。它提供了一个列表：一系列包含数据的行。在该示例中，添加了第二个工作表以保存列表源。用户只能从列表中选择值。验证区域是第一个工作表中的单元格区域 A1:A5。

在这里设置是很重要的[**验证.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)财产给**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **日期数据验证**

通过这种类型的验证，用户可以在指定范围内或满足特定条件的日期值输入到已验证的单元格中。在示例中，用户只能输入 1970 到 1999 之间的日期。这里，验证区域是 B1 单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **时间数据验证**

通过这种类型的验证，用户可以在指定范围内或满足某些条件的时间输入已验证的单元格。在示例中，用户只能输入 09:00 到 11:30 AM 之间的时间。这里，验证区域是 B1 单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **文本长度数据验证**

通过这种类型的验证，用户可以将指定长度的文本值输入到已验证的单元格中。在示例中，用户被限制输入不超过 5 个字符的字符串值。验证区域是 B1 单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **数据验证规则**

实施数据验证后，可以通过在单元格中分配不同的值来检查验证。[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)可用于获取验证结果。以下示例使用不同的值演示了此功能。示例文件可以从以下链接下载进行测试：

[示例数据验证规则.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **检查单元格中的验证是否为下拉列表**

正如我们所见，可以在一个单元格中实现多种类型的验证。如果你想检查验证是否下拉，[**验证.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)属性可用于对此进行测试。以下示例代码演示了此属性的用法。可以从以下链接下载用于测试的示例文件：

[示例验证.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **将 CellArea 添加到现有验证**

在某些情况下，您可能想要添加[**单元格区域**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)对现有的[**验证**](https://reference.aspose.com/cells/net/aspose.cells/validation).当你添加[**单元格区域**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)使用[**Validation.AddArea(CellArea 单元格区域)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea)Aspose.Cells 检查所有现有区域，看新区域是否已经存在。如果文件有大量验证，这会影响性能。为了克服这个问题，API 提供了[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)方法。这*检查交叉路口*参数指示是否检查给定区域与现有验证区域的交集。将其设置为**错误的**将禁用其他区域的检查。这*检查边缘*参数表示是否勾选应用区域。如果新区域成为左上角区域，则内部设置将被重建。如果您确定新区域不是左上角区域，您可以将此参数设置为**错误的**.

下面的代码片段演示了使用[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1)添加新方法[**单元格区域**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)对现有的[**验证**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

附上源文件和输出 excel 文件以供参考。

[源文件](96928093.xlsx)

[输出文件](96928220.xlsx)


## **推进主题**
- [在 ODS 文件中获取 Cell 验证](/cells/zh/net/get-cell-validation-in-ods-files/)
- [在 Cell 上应用验证](/cells/zh/net/get-validation-applied-on-a-cell/)
- [验证 Cell 值是否满足数据验证规则](/cells/zh/net/verify-that-cell-value-satisfies-data-validation-rules/)
