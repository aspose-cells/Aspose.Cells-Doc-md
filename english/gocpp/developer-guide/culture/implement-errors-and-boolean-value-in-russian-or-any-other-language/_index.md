---
title: Implement Errors and Boolean Values in Russian or Any Other Language with Golang via C++
linktitle: Implement Errors and Boolean Values
type: docs
weight: 40
url: /go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Learn how to implement errors and boolean values in Russian or any other language using Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

If you are using Microsoft Excel in the Russian locale or language, or any other locale or language, it will display errors and Boolean values according to that locale or language. You can achieve similar behavior using Aspose.Cells by using the [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/) property. You will have to override the following methods of the [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Implement Errors and Boolean Values in Russian or Any Other Language**

The following sample code illustrates how to implement errors and Boolean values in Russian or any other language. Please check the [Sample Excel File](73990159.xlsx) used by this code and its [Output PDF](73990160.pdf). The screenshot shows the difference between the sample Excel file and the output PDF for reference.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}