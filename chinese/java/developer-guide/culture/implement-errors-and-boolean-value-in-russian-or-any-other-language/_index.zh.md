---
title: 以俄语或其他任何语言实现错误和布尔值
type: docs
weight: 30
url: /zh/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能的使用场景**
如果您在俄语区域设置或语言或任何其他区域设置或语言下使用 Microsoft Excel，则它将根据该区域设置或语言显示错误和布尔值。您可以通过使用 Aspose.Cells 的 [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) 方法或属性来实现类似的行为。您将需要覆盖 [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) 类的以下方法。

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString-java.lang.String-)
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString-boolean-)
## **以俄语或其他任何语言实现错误和布尔值**
以下示例代码演示了如何在俄语或其他任何语言中实现错误和布尔值。请检查此代码中使用的示例 Excel 文件及其输出 PDF。屏幕截图显示了 [示例 Excel 文件](48496697.xlsx) 和 [输出 PDF](48496696.pdf) 之间的差异。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **示例代码**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
{{< app/cells/assistant language="java" >}}
