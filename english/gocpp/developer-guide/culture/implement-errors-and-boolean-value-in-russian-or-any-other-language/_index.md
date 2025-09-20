---
title: Implement Errors and Boolean Value in Russian or Any Other Language with Golang via C++
linktitle: Implement Errors and Boolean Value
type: docs
weight: 40
url: /go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Learn how to implement errors and boolean values in Russian or any other language using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve a similar behavior using Aspose.Cells by using the [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/) property. You will have to override the following methods of [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Implement Errors and Boolean Value in Russian or Any Other Language**

The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the [Sample Excel File](73990159.xlsx) used in this code and its [Output PDF](73990160.pdf). The screenshot shows the difference between Sample Excel File and the Output PDF for a reference.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}