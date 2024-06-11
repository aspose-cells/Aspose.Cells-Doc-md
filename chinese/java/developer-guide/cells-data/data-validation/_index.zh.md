---
title: 数据验证
type: docs
weight: 70
url: /zh/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel 提供一些良好的功能来自动过滤或验证工作表数据。

[数据验证](/cells/zh/java/data-validation/)是设置有关工作表上输入的数据规则的能力。 例如，使用验证来确保标记为日期的列仅包含日期，或者另一列仅包含数字。 甚至可以确保标记为日期的列只包含特定范围内的日期。 通过数据验证，您可以控制输入到工作表单元格中的内容。 Aspose.Cells 完全支持 Microsoft Excel 的数据验证和自动筛选功能。 本文解释了如何在 Microsoft Excel 中使用这些功能，以及如何使用 Aspose.Cells 对其进行编码。

{{% /alert %}} 
## **数据验证类型和执行**
Microsoft Excel 支持许多不同类型的数据验证。 每种类型用于控制输入到单元格或单元格范围中的数据类型。 下面的代码片段说明了如何验证：

- [数字是整数](/cells/zh/java/data-validation/)，即它们没有小数部分。
- [十进制数字遵循正确结构](/cells/zh/java/data-validation/)。代码示例定义了一个范围的单元格应具有两个小数位数。
- [值受限于值列表](/cells/zh/java/data-validation/)。列表验证定义了可应用于单元格或单元格范围的单独值列表。
- [日期落在特定范围内](/cells/zh/java/data-validation/)。
- [时间在特定范围内](/cells/zh/java/data-validation/)。
- [文本在给定字符长度内](/cells/zh/java/data-validation/)。
### **Microsoft Excel中的数据验证**
要使用Microsoft Excel创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 从**数据**菜单中，选择**验证**。
   将显示验证对话框。
1. 单击**设置**选项卡，并输入下方显示的设置。 

   **数据验证设置** 

![todo:image_alt_text](data-validation_1.png)
### **Aspose.Cells中的数据验证**
数据验证是一项强大的功能，可验证输入工作表的信息。借助数据验证，开发人员可以为用户提供选择列表，限制数据输入为特定类型或大小等功能。
在Aspose.Cells中，每个[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类都有一个[Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)对象，该对象表示一组[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)对象。要设置验证，请设置[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)类的一些属性：

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type)：表示验证类型，可以使用[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)枚举中的预定义值来指定。
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator)：表示验证中要使用的运算符，可以使用[OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)枚举中的预定义值来指定。
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1)：表示与数据验证第一部分相关联的值或表达式。
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2)：表示与数据验证第二部分相关联的值或表达式。

当[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)对象的属性配置完成后，开发人员可以使用[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)结构来存储关于将使用创建的验证进行验证的单元格范围的信息。
#### **数据验证类型**
数据验证允许您在每个单元格中构建业务规则，以便不正确的输入会导致错误消息。业务规则是管理业务运作的政策和程序。Aspose.Cells支持所有重要类型的数据验证。

[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)枚举具有以下成员:

|**成员名称**|**描述**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|表示任何类型的值。
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|表示整数验证类型。
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|表示小数验证类型。
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|表示下拉列表验证类型。
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|表示日期验证类型。
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|表示时间验证类型。
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|表示文本长度验证类型。
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|表示自定义验证类型。
#### **编程示例：整数数据验证**
使用此类型的验证，用户只能在验证的单元格中输入指定范围内的整数。接下来的代码示例展示了如何实现[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)验证类型。示例创建了一个与我们在Microsoft Excel中创建的相同的数据验证，使用Aspose.Cells。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **编程示例：小数数据验证**
使用此类型的验证，用户可以在验证的单元格中输入小数。在示例中，用户被限制只能输入小数值，并且验证区域是A1:A10。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **编程示例：列表数据验证**
此验证类型允许用户从下拉列表中输入值。它提供了一个列表：包含数据的一系列行。用户只能从列表中选择值。验证区域是第一个工作表中的单元格范围A1:A5。

在这里很重要的是将[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)属性设置为**true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **编程示例: 日期数据验证**
使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的日期值。在此示例中，用户被限制只能输入1970年至1999年之间的日期。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **编程示例: 时间数据验证**
使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的时间值。在此示例中，用户被限制只能输入上午09:00至11:30之间的时间。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **编程示例: 文本长度数据验证**
使用此类型的验证，用户可以在验证单元格中输入指定长度的文本值。在此示例中，用户被限制只能输入不超过5个字符的字符串值。验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **数据验证规则**
当实施数据验证时，可以通过在单元格中分配不同的值来检查验证。[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) 可用于获取验证结果。以下示例演示了使用不同值的此功能。可从以下链接下载示例文件进行测试:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **检查单元格中的验证是否为下拉框**
正如我们所见，可以在单元格中实施许多类型的验证。如果您想检查验证是否为下拉框，可以使用[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) 属性进行测试。以下示例代码演示了该属性的用法。可从以下链接下载示例文件进行测试:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **为现有验证添加CellArea**
也许会有这样的情况，您可能希望向现有验证添加[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)。通过使用[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\))，Aspose.Cells会检查所有现有区域，看看新区域是否已经存在。如果文件具有大量验证，这将影响性能。为解决此问题，API提供了[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) 方法。*checkIntersection*参数指示是否检查给定区域与现有验证区域的交集。将其设置为**false**将禁用其他区域的检查。*checkEdge*参数指示是否检查已应用的区域。如果新区域成为左上角区域，内部设置将重新构建。如果您确信新区域不是左上角区域，可以将此参数设置为**false**。

以下代码片段演示了使用[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) 方法向现有验证添加新的[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

源和输出的Excel文件已附上供参考。

[源文件](PivotTableHideAndSortSample.xlsx)

[输出文件](ValidationsSample_out.xlsx)


## **高级主题**
- [获取ODS文件中的单元格验证](/cells/zh/java/get-cell-validation-in-ods-files/)
- [获取应用于单元格的验证](/cells/zh/java/get-validation-applied-on-a-cell/)
- [验证单元格值是否满足数据验证规则](/cells/zh/java/verify-that-cell-value-satisfies-data-validation-rules/)
