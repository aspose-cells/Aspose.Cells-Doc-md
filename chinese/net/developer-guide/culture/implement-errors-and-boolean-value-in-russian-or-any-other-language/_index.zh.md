---
title: 以俄语或其他任何语言实现错误和布尔值
type: docs
weight: 40
url: /zh/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能的使用场景**

如果您在俄罗斯区域设置或语言或任何其他区域设置或语言中使用Microsoft Excel，它将根据该语言或区域设置显示错误和布尔值。您可以通过使用**[Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) 属性实现类似的行为。您将需要覆盖[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类的以下方法。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **以俄语或其他任何语言实现错误和布尔值**

以下示例代码说明了如何在俄语或其他任何语言中实现错误和布尔值。请查看此代码中使用的[Sample Excel File](73990159.xlsx)及其[Output PDF](73990160.pdf)。屏幕截图显示了示例Excel文件和输出PDF之间的差异作为参考。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
