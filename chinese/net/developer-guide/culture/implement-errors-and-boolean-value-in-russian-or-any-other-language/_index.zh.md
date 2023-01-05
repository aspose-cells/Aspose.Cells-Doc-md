---
title: 用俄语或任何其他语言实现错误和布尔值
type: docs
weight: 40
url: /zh/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **可能的使用场景**

如果您在俄语区域设置或语言或任何其他区域设置或语言中使用 Microsoft Excel，它将根据该区域设置或语言显示错误和布尔值。您可以通过使用 Aspose.Cells 实现类似的行为**[工作簿.设置.全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) 属性。您将不得不重写以下方法[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)班级。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **用俄语或任何其他语言实现错误和布尔值**

以下示例代码说明了如何用俄语或任何其他语言实现错误和布尔值。请检查[示例 Excel 文件](73990159.xlsx)在此代码中使用及其[输出 PDF](73990160.pdf).屏幕截图显示了示例 Excel 文件与输出 PDF 之间的差异，以供参考。

![待办事项：图片_替代_文本](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
