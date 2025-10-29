---
title: 使用C++中的Golang实现俄语或其他语言的错误和布尔值
linktitle: 实现错误和布尔值
type: docs
weight: 40
url: /zh/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: 学习如何使用C++中的Golang通过Aspose.Cells实现俄语或其他语言的错误和布尔值
---

## **可能的使用场景**

如果你使用的是俄语或其他任何语言的微软Excel，它会根据该语言显示错误和布尔值。你可以在使用 Aspose.Cells 时通过使用 [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/) 属性实现类似的行为。你需要重写 [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) 类的以下方法。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **以俄语或其他任何语言实现错误和布尔值**

以下示例代码说明了如何在俄语或其他任何语言中实现错误和布尔值。请查看此代码中使用的[Sample Excel File](73990159.xlsx)及其[Output PDF](73990160.pdf)。屏幕截图显示了示例Excel文件和输出PDF之间的差异作为参考。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
