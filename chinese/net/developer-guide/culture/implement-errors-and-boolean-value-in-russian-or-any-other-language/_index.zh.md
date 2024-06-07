---
title: 在俄语或其他任何语言中实现错误和布尔值
type: docs
weight: 40
url: /zh/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能的使用场景**

如果您使用俄语区域设置或语言或任何其他区域设置或语言的Microsoft Excel，它将根据该区域设置或语言显示错误和布尔值。您可以通过使用**[Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)属性来实现类似的行为。您需要重写[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类的以下方法。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **在俄语或其他任何语言中实现错误和布尔值**

以下示例代码说明了如何在俄语或其他任何其他语言中实现错误和布尔值。请检查本代码中使用的[示例Excel文件](73990159.xlsx)及其生成的[输出PDF](73990160.pdf)。屏幕截图显示了示例Excel文件与输出PDF之间的差异。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
