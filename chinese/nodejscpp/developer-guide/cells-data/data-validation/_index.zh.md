---  
title: 数据验证
type: docs  
weight: 90  
url: /zh/nodejs-cpp/data-validation/  
description: 学习如何通过Aspose.Cells for Node.js via C++ API添加数据验证。  
keywords: 通过C++在Node.js中添加数据验证，在Node.js中获取验证值，在C++中添加整体数字类型验证，在C++中添加列表验证，在C++中添加日期验证，在C++中添加时间验证，在C++中添加文本长度验证，在C++中向已有验证添加CellArea，检查单元格中的验证是否为下拉菜单，在C++中添加自定义验证  
---  

{{% alert color="primary" %}}  
微软Excel提供一些良好的自动筛选和验证工作表数据的功能。Aspose.Cells全面支持微软Excel的数据验证和自动筛选功能。本文介绍如何在微软Excel中使用这些功能，以及如何使用Aspose.Cells for Node.js via C++编写代码实现。  
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

### **使用Aspose.Cells for Node.js via C++进行数据验证**  

数据验证是一项强大的功能，可验证输入工作表的信息。借助数据验证，开发人员可以为用户提供选择列表，限制数据输入为特定类型或大小等功能。  
在 Aspose.Cells for Node.js via C++ 中，每个 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类都有一个 [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) 方法，代表一组 [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) 对象。为了设置验证，将一些 [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) 类的属性设为如下：  

- 类型——代表验证类型，可以使用 [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) 枚举中的预定义值之一进行指定。  
- 运算符——代表用于验证的运算符，可以使用 [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype) 枚举中的预定义值之一进行指定。  
- Formula1 – 表示与数据验证的第一部分关联的值或表达式。  
- Formula2 – 表示与数据验证的第二部分关联的值或表达式。  

当 [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) 对象的属性配置完成后，开发者可以使用 [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) 结构存储有关使用创建的验证进行验证的单元格范围的信息。  

#### **数据验证类型**  

[**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) 枚举具有以下成员：  

|**成员名称**|**描述**|  
| :- | :- |  
|AnyValue|表示任何类型的值。  
|WholeNumber|表示整数的验证类型。  
|Decimal|表示十进制数字的验证类型。  
|List|表示下拉列表的验证类型。  
|Date|表示日期的验证类型。  
|Time|表示时间的验证类型。  
|TextLength|表示文本长度的验证类型。  
|Custom|表示自定义验证类型。  

##### **整数数据验证**  

使用此类型的验证，用户只能在验证的单元格中输入指定范围内的整数。接下来的代码示例展示了如何实现整数字验证类型。该示例使用 Aspose.Cells for Node.js via C++ 创建了与上述 Microsoft Excel 中相同的数据验证。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **列表数据验证**  

这种类型的验证允许用户从下拉列表中输入值。它提供了一个列表：包含数据的一系列行。在示例中，添加了第二个工作表来保存列表源。用户只能从列表中选择值。验证区域是第一个工作表中的单元格范围 A1:A5。  

这里重要的是要将 [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) 属性设为 **true**。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **日期数据验证**  

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的日期值。在此示例中，用户被限制只能输入1970年至1999年之间的日期。这里，验证区域是B1单元格。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **时间数据验证**  

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的时间值。在此示例中，用户被限制只能输入上午09:00至11:30之间的时间。这里，验证区域是B1单元格。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **文本长度数据验证**  

使用此类型的验证，用户可以在验证单元格中输入指定长度的文本值。在此示例中，用户被限制只能输入不超过5个字符的字符串值。验证区域是B1单元格。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **数据验证规则**  

当实现数据验证后，可以通过在单元格中设定不同值来检测验证结果。可以使用 [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) 获取验证结果。以下示例用不同的值展示了此功能。测试用的示例文件可以通过以下链接下载：  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **检查单元格中的验证是否为下拉列表**  

正如我们所见，单元格中可以实现许多类型的验证。如果你想检查验证是否为下拉菜单， 可以使用 [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) 方法进行测试。以下示例代码展示了此属性的用法。可以从以下链接下载测试的示例文件：  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **为现有验证添加CellArea**  

可能存在你想向现有 [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) 添加 [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) 的情况。使用 [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-) 添加 [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) 时，Aspose.Cells 会检查所有现有区域，查看新区域是否已存在。如果文件中验证数量较多，可能会影响性能。为了解决此问题，API 提供了 [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) 方法。*checkIntersection* 参数表示是否检测给定区域与现有验证区域的交集。设为 **false** 将禁用对其他区域的检测。*checkEdge* 参数表示是否检查应用区域。如果新区域成为左上角区域，内部设置会被重建。若确定新区域不是左上角区域，可将此参数设为 **false**。  

以下代码片段演示了如何使用 [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) 方法向现有 [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) 添加一个新 [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

源和输出的Excel文件已附上供参考。  

[源文件](96928093.xlsx)  

[输出文件](96928220.xlsx)  

## **高级主题**  
- [获取ODS文件中的单元格验证](/cells/zh/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [获取应用于单元格的验证](/cells/zh/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [验证单元格值是否满足数据验证规则](/cells/zh/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
