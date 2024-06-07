---
title: 在俄语或其他任何语言中实现错误和布尔值
type: docs
weight: 30
url: /zh/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能的使用场景**
如果您在俄罗斯区域设置或语言设置等其他区域或语言环境中使用Microsoft Excel，它将按照该区域设置或语言设置显示错误和布尔值。您可以通过使用Aspose.Cells [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)方法或属性来实现类似的行为。您需要覆盖[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)类的以下方法。

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **在俄语或其他任何语言中实现错误和布尔值**
以下示例代码说明如何在俄语或其他语言中实现错误和布尔值。 请查看此代码中使用的示例Excel文件及其输出PDF。 屏幕截图显示了[示例Excel文件](48496697.xlsx)和[输出PDF](48496696.pdf)之间的差异。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
