---
title: 数据验证
type: docs
weight: 70
url: /zh/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel提供了一些很好的功能来自动筛选或验证工作表数据。

[数据验证](/cells/zh/java/data-validation/)是设置与工作表上输入的数据相关的规则的能力。例如，使用验证确保名为DATE的列仅包含日期，或者另一列仅包含数字。甚至可以确保名为DATE的列仅包含某个范围内的日期。使用数据验证，您可以控制将输入到工作表单元格中的内容。Aspose.Cells完全支持Microsoft Excel的数据验证和自动筛选功能。本文解释了如何在Microsoft Excel中使用这些功能，以及如何在Aspose.Cells中编写它们的代码。

{{% /alert %}} 
## **数据验证类型和执行**
Microsoft Excel支持许多不同类型的数据验证。每种类型用于控制输入到单元格或单元格范围的数据类型。下面，代码片段说明了如何验证：

- [数字是整数](/cells/zh/java/data-validation/)，即它们没有小数部分。
- [十进制数遵循正确的结构](/cells/zh/java/data-validation/)。代码示例定义了一组单元格应该具有两个小数位。
- [值被限制为一组值](/cells/zh/java/data-validation/)。列表验证定义了可以应用于单元格或单元格范围的单独值列表。
- [日期在特定范围内](/cells/zh/java/data-validation/)。
- [时间在特定范围内](/cells/zh/java/data-validation/)。
- [文本在给定的字符长度内](/cells/zh/java/data-validation/)。
### **Microsoft Excel数据验证**
使用Microsoft Excel创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 从**数据**菜单中，选择**验证**。
   显示验证对话框。
1. 单击**设置**选项卡，并输入如下设置。 

   **数据验证设置** 

![todo:image_alt_text](data-validation_1.png)
### **Aspose.Cells数据验证**
数据验证是用于验证输入到工作表的信息的强大功能。使用数据验证，开发人员可以为用户提供选择列表，将数据条目限制为特定类型或大小，等等。
在Aspose.Cells中，每个[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类都有一个[Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)对象，该对象表示一个[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)对象的集合。要设置验证，设置一些[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)类的属性:

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type)：表示验证类型，可以使用[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)枚举中的预定义值来指定。
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator)：表示在验证中要使用的运算符，可以使用[OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)枚举中的预定义值来指定。
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1)：表示与数据验证的第一部分关联的值或表达式。
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2)：表示与数据验证的第二部分关联的值或表达式。

配置了[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)对象的属性后，开发人员可以使用[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)结构存储有关将使用创建的验证来验证的单元格范围的信息。
#### **数据验证类型**
数据验证允许您在每个单元格中构建业务规则，以便不正确的输入会导致错误消息。业务规则是管理企业运营方式的政策和程序。Aspose.Cells支持所有重要类型的数据验证。

[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)枚举具有以下成员:

|**成员名称**|**描述**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|表示任何类型的值|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|表示整数的验证类型|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|表示小数的验证类型|
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|表示下拉列表的验证类型|
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|表示日期的验证类型|
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|表示时间的验证类型|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|表示文本长度的验证类型|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|表示自定义验证类型|
#### **编程示例: 整数数据验证**
使用此类型的验证，用户只能输入指定范围内的整数到验证单元格中。接下来的代码示例显示了如何实现[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)验证类型。该示例创建了与我们在Microsoft Excel中创建的相同数据验证的Aspose.Cells数据验证。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **编程示例: 小数数据验证**
使用此类型的验证，用户可以将小数输入验证的单元格中。在示例中，用户被限制仅输入小数值，验证区域为A1:A10。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **编程示例: 列表数据验证**
这种验证类型允许用户从下拉列表中输入值。它提供一个列表: 一系列包含数据的行。用户只能从列表中选择值。第一个工作表中的验证区域是单元格范围A1:A5。

在这里重要的是将[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)属性设置为**true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **编程示例: 日期数据验证**
使用这种类型的验证，用户在指定范围内输入日期值，或满足特定标准，进入验证的单元格。在示例中，用户被限制在1970年至1999年之间输入日期。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **编程示例: 时间数据验证**
使用这种类型的验证，用户可以在指定范围内输入时间，或满足一些标准，进入验证的单元格。在示例中，用户被限制在上午09:00至11:30之间输入时间。这里，验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **编程示例: 文本长度数据验证**
使用这种类型的验证，用户可以在验证的单元格中输入指定长度的文本值。在示例中，用户被限制在字符串值中不超过5个字符。验证区域是B1单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **数据验证规则**
当数据验证实现后，可以通过为单元格分配不同值来检查验证。[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\))可以用于获取验证结果。以下示例演示了如何使用不同值进行此操作。可以从以下链接下载样本文件进行测试:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **检查单元格中的验证是否为下拉列表**
正如我们所见，有许多种类型的验证可以在单元格内实现。如果您想要检查验证是否为下拉框，请使用[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown)属性进行测试。以下示例代码演示了如何使用此属性。可从以下链接下载用于测试的示例文件：

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **将CellArea添加到现有验证**
可能会出现一种情况，您可能希望将[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)添加到现有的[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)中。当您使用[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\))添加[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)时，Aspose.Cells将检查所有现有区域，以查看新区域是否已存在。如果文件中有大量的验证，这会影响性能。为了解决这个问题，API提供了[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\))方法。*checkIntersection*参数指示是否检查给定区域与现有验证区域的交集。将其设置为**false**将禁用对其他区域的检查。*checkEdge*参数指示是否检查应用区域。如果新区域成为左上区域，内部设置将被重建。如果您确信新区域不是左上区域，可以将此参数设置为**false**。

以下代码片段演示了如何使用[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\))方法向现有的[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)中添加新的[CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

源和输出的 Excel 文件附在下面供参考。

[源文件](PivotTableHideAndSortSample.xlsx)

[输出文件](ValidationsSample_out.xlsx)


## **高级主题**
- [获取ODS文件中的单元格验证](/cells/zh/java/get-cell-validation-in-ods-files/)
- [获取应用在单元格上的验证](/cells/zh/java/get-validation-applied-on-a-cell/)
- [验证单元格值是否符合数据验证规则](/cells/zh/java/verify-that-cell-value-satisfies-data-validation-rules/)
