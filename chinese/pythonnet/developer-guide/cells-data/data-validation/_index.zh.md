---
title: 数据验证
type: docs
weight: 90
url: /zh/python-net/data-validation/
description: 通过Aspose.Cells for Python via .NET API学习如何添加数据验证。
keywords: Python Excel库，Python添加数据验证，Python获取验证值，Python添加整数数据验证，Python添加列表数据验证，Python添加日期数据验证，Python添加时间数据验证，Python添加文本长度数据验证，Python向现有验证添加CellArea，Python检查单元格中的验证是否为下拉式，添加自定义验证  
---

{{% alert color="primary" %}}

Microsoft Excel提供了一些很好的自动筛选或验证工作表数据的功能。Aspose.Cells for Python via .NET完全支持Microsoft Excel的数据验证和自动筛选功能。本文解释了如何在Microsoft Excel中使用这些功能，并介绍了如何使用Aspose.Cells for Python via .NET进行编码。

{{% /alert %}}

## **数据验证类型和执行**

数据验证是设置有关工作表上输入的数据的规则的能力。例如，使用验证可确保标有日期的列仅包含日期，或者另一列仅包含数字。甚至可以确保标有日期的列仅包含特定范围内的日期。通过数据验证，可以控制输入工作表中单元格的内容。

Microsoft Excel 支持许多不同类型的数据验证。 每种类型用于控制输入到单元格或单元格范围中的数据类型。 下面的代码片段说明了如何验证：

- 数字是整数，即它们没有小数部分。
- 十进制数遵循正确的结构。代码示例定义了一组单元格应具有两个小数位。
- 值受限于值列表。列表验证定义了可应用于单元格或单元格范围的单独值列表。
- 日期在特定范围内。
- 时间在特定范围内。
- 文本在给定的字符长度内。

### **Microsoft Excel中的数据验证**

要使用Microsoft Excel创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 从**数据**菜单中选择**验证**。将显示验证对话框。
1. 单击**设置**选项卡并输入设置。

### **Aspose.Cells for Python Excel Library Data Validation**

数据验证是一项强大的功能，可验证输入工作表的信息。借助数据验证，开发人员可以为用户提供选择列表，限制数据输入为特定类型或大小等功能。
在 Aspose.Cells for Python via .NET 中，每个 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 类都有一个 [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) 属性，该属性表示一个 [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) 对象的集合。要设置验证，请将一些 [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) 类的属性设置如下:

- type – 表示验证类型，可以通过在 [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) 枚举中使用预定义的值来指定。
- Operator – 表示验证中要使用的运算符，可以通过在 [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) 枚举中使用预定义的值来指定。
- formula1 – 表示与数据验证的第一部分关联的值或表达式。
- formula2 – 表示与数据验证的第二部分关联的值或表达式。

当配置了 [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) 对象的属性后，开发人员可以使用 [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) 结构来存储有关使用创建的验证进行验证的单元格范围的信息。

#### **数据验证类型**

[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) 枚举具有以下成员:

|**成员名称**|**描述**|
| :- | :- |
|ANY_VALUE|表示任何类型的值。
|WHOLE_NUMBER|表示整数的验证类型。
DECIMAL表示小数的验证类型。
LIST表示下拉列表的验证类型。
|DATE| 用于日期的验证类型。
TIME表示时间的验证类型。
|TEXT_LENGTH|表示文本长度的验证类型。
CUSTOM表示自定义验证类型。

##### **整数数据验证**

使用这种类型的验证，用户只能在验证的单元格中输入指定范围内的整数。接下来的代码示例显示了如何实现 WholeNumber 验证类型。该示例创建了与我们在 Microsoft Excel 中创建的相同数据验证使用 Aspose.Cells for Python via .NET。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **列表数据验证**

这种类型的验证允许用户从下拉列表中输入值。它提供了一个列表：包含数据的一系列行。在示例中，添加了第二个工作表来保存列表源。用户只能从列表中选择值。验证区域是第一个工作表中的单元格范围 A1:A5。

在这里重要的是，将 [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) 属性设置为 **true**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **日期数据验证**

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的日期值。在此示例中，用户被限制只能输入1970年至1999年之间的日期。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **时间数据验证**

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的时间值。在此示例中，用户被限制只能输入上午09:00至11:30之间的时间。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **文本长度数据验证**

使用此类型的验证，用户可以在验证单元格中输入指定长度的文本值。在此示例中，用户被限制只能输入不超过5个字符的字符串值。验证区域是B1单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **数据验证规则**

当数据验证被实施时，可以通过在单元格中分配不同的值来检查验证。[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 可以用于获取验证结果。以下示例演示了如何使用不同的值实现此功能。测试样本文件可从以下链接下载：

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **检查单元格中的验证是否为下拉列表**

正如我们所见，可以在单元格中实施许多类型的验证。如果要检查验证是否为下拉列表，可以使用[**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/)属性来测试。以下示例代码演示了如何使用此属性。测试样本文件可从以下链接下载：

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **为现有验证添加CellArea**

可能存在这样的情况，您可能希望通过使用[**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea)向现有的[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)添加[**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)。当您使用[**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea)添加[**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)时，Aspose.Cells将检查所有现有区域，以查看新区域是否已经存在。如果文件具有大量验证，这会导致性能下降。为了克服这个问题，API提供了[**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool)方法。*checkIntersection*参数指示是否检查给定区域与现有验证区域的交集。将其设置为**false**将禁用对其他区域的检查。*checkEdge*参数指示是否检查应用区域。如果新区域成为左上角区域，则内部设置将被重新构建。如果您确定新区域不是左上角区域，可以将此参数设置为**false**。

以下代码片段演示了如何使用[**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool)方法向现有的[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)添加新的[**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

源和输出的Excel文件已附上供参考。

[源文件](96928093.xlsx)

[输出文件](96928220.xlsx)


## **高级主题**
- [获取ODS文件中的单元格验证](/cells/zh/python-net/get-cell-validation-in-ods-files/)
- [获取应用于单元格的验证](/cells/zh/python-net/get-validation-applied-on-a-cell/)
- [验证单元格值是否满足数据验证规则](/cells/zh/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="python-net" >}}
