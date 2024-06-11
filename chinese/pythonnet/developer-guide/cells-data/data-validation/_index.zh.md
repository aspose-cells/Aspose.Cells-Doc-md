---
title: 数据验证
type: docs
weight: 90
url: /zh/python-net/data-validation/
description: 通过使用Aspose.Cells for Python通过.NET API学习如何通过数据验证。
keywords: Python Excel库，Python添加数据验证，Python获取验证值，Python添加整数数据验证，Python添加列表数据验证，Python添加日期数据验证，Python添加时间数据验证，Python添加文本长度数据验证，Python添加单元格区域到现有验证，Python检查单元格中的验证是否是下拉列表，添加自定义验证  
---

{{% alert color="primary" %}}

Microsoft Excel提供了自动筛选或验证工作表数据的一些好功能。Aspose.Cells for Python通过.NET完全支持Microsoft Excel的数据验证和自动筛选功能。本文说明了如何在Microsoft Excel中使用这些功能，并如何使用Aspose.Cells for Python通过.NET对其进行编码。

{{% /alert %}}

## **数据验证类型和执行**

数据验证是设置有关在工作表上输入的数据的规则的能力。例如，使用验证来确保标有日期的列仅包含日期，或另一列仅包含数字。您甚至可以确保标有日期的列仅包含特定范围内的日期。使用数据验证，可以控制输入到工作表中单元格中的内容。

Microsoft Excel支持许多不同类型的数据验证。每种类型用于控制输入到单元格或单元格范围的数据类型。下面，代码片段说明了如何验证：

- 数字是整数，即它们没有小数部分。
- 小数遵循正确的结构。代码示例定义一系列单元格应具有两个小数位。
- 值受限于值列表。列表验证定义了一个可应用于单元格或单元格范围的值列表。
- 日期在特定范围内。
- 时间在特定范围内。
- 文本长度在给定的字符长度内。

### **Microsoft Excel数据验证**

使用Microsoft Excel创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 从**数据**菜单中，选择**验证**。将显示验证对话框。
1. 单击**设置**选项卡，输入设置。

### **使用Aspose.Cells for Python Excel库进行数据验证**

数据验证是用于验证输入到工作表的信息的强大功能。使用数据验证，开发人员可以为用户提供选择列表，将数据条目限制为特定类型或大小，等等。
在Aspose.Cells for Python通过.NET中，每个[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类都有一个[**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/)属性，代表[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)对象的集合。要设置验证，设置一些[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)类属性如下:

- type - 表示验证类型，可以通过[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype)枚举中的预定义值之一指定。
- 运算符 - 表示在验证中要使用的运算符，可以使用[**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype)枚举中预定义的值之一指定。
- formula1 - 表示与数据验证第一部分关联的值或表达式。
- formula2 - 表示与数据验证第二部分关联的值或表达式。

当[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)对象的属性已配置好后，开发人员可以使用[**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)结构来存储有关将使用创建的验证进行验证的单元格范围的信息。

#### **数据验证类型**

[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype)枚举具有以下成员：

|**成员名称**|**描述**|
| :- | :- |
|ANY_VALUE|表示任何类型的值。|
|WHOLE_NUMBER|表示整数验证类型。|
|DECIMAL|表示十进制数验证类型|
|LIST|表示下拉列表验证类型|
|DATE|表示日期验证类型|
|TIME|表示时间验证类型|
|TEXT_LENGTH|表示文本长度的验证类型。|
|CUSTOM|表示自定义验证类型|

##### **整数数据验证**

通过此类型的验证，用户只能在验证的单元格中输入指定范围内的整数。接下来的代码示例展示了如何实现WholeNumber验证类型。 该示例使用Aspose.Cells for Python通过.NET创建了与在Microsoft Excel中创建的相同的数据验证。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **列表数据验证**

这种类型的验证允许用户从下拉列表中输入值。它提供了一个列表: 包含数据的一系列行。在示例中，添加了第二个工作表来存储列表源。用户只能从列表中选择值。验证区域是第一个工作表中的A1:A5单元格范围。

重要的是，要将 [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) 属性设置为 **true**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **日期数据验证**

使用这种类型的验证，用户在指定范围内输入日期值，或满足特定标准，进入验证的单元格。在示例中，用户被限制在1970年至1999年之间输入日期。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **时间数据验证**

使用这种类型的验证，用户可以在指定范围内输入时间，或满足一些标准，进入验证的单元格。在示例中，用户被限制在上午09:00至11:30之间输入时间。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **文本长度数据验证**

使用这种类型的验证，用户可以在验证的单元格中输入指定长度的文本值。在示例中，用户被限制在字符串值中不超过5个字符。验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **数据验证规则**

实现数据验证后，可以通过在单元格中分配不同的值来检查验证。 [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 可用于获取验证结果。 以下示例演示了如何使用不同的值来进行此功能。 可以从以下链接下载示例文件进行测试：

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **检查单元格中的验证是否是下拉列表**

如我们所见，可以在单元格中实现许多类型的验证。如果要检查验证是否是下拉列表，可以使用 [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) 属性进行测试。以下示例代码演示了如何使用此属性。可以从以下链接下载示例文件进行测试:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **将CellArea添加到现有验证**

可能会有这样的情况，您可能希望将 [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) 添加到现有的 [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)。当使用 [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea) 添加 [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) 时，Aspose.Cells 会检查所有现有区域，看看新区域是否已存在。如果文件中有大量的验证，这会导致性能下降。为了克服这个问题，API 提供了 [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) 方法。*checkIntersection* 参数指示是否检查给定区域与现有验证区域的交集。将其设置为 **false** 将禁用对其他区域的检查。*checkEdge* 参数指示是否检查应用程序区域。如果新区域成为左上角区域，则会重新构建内部设置。如果确信新区域不是左上角区域，可以将此参数设置为 **false**。

以下代码片段演示了使用 [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) 方法将新的 [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) 添加到现有的 [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

源和输出的 Excel 文件附在下面供参考。

[源文件](96928093.xlsx)

[输出文件](96928220.xlsx)


## **高级主题**
- [获取ODS文件中的单元格验证](/cells/zh/python-net/get-cell-validation-in-ods-files/)
- [获取应用在单元格上的验证](/cells/zh/python-net/get-validation-applied-on-a-cell/)
- [验证单元格值是否符合数据验证规则](/cells/zh/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
