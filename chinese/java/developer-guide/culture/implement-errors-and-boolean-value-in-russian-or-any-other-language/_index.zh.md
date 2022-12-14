---
title: 用俄语或任何其他语言实现错误和布尔值
type: docs
weight: 30
url: /zh/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **可能的使用场景**
如果您在俄语区域设置或语言或任何其他区域设置或语言中使用 Microsoft Excel，它将根据该区域设置或语言显示错误和布尔值。您可以使用 Aspose.Cells 实现类似的行为[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)方法或属性。您将不得不重写以下方法[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)班级。

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **用俄语或任何其他语言实现错误和布尔值**
以下示例代码说明了如何用俄语或任何其他语言实现错误和布尔值。请检查此代码中使用的示例 Excel 文件及其输出 PDF。屏幕截图显示了两者之间的区别[示例 Excel 文件](48496697.xlsx)和[输出PDF](48496696.pdf)供参考。

![待办事项：图片_替代_文本](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
