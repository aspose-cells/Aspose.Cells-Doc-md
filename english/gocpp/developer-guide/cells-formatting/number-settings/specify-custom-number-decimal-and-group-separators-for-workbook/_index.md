---
title: Specify Custom Number Decimal and Group Separators for Workbook with Golang via C++
linktitle: Specify Custom Number Decimal and Group Separators
type: docs
weight: 110
url: /go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Change the number decimal and group separators in MS Excel using Golang via C++ code by using the Aspose.Cells for C++ API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel c++, specify custom group separator excel, specify custom group separator excel c++, specify custom decimal and group separator excel, specify custom decimal and group separator excel c++, change decimal and group separator excel c++, change decimal and group separator excel, change decimal separator excel, change decimal separator excel c++, change group separator excel, change group separator excel c++
---

{{% alert color="primary" %}}

In Microsoft Excel, you can specify custom decimal and thousands separators instead of using the system separators from the **Advanced Excel Options**, as shown in the screenshot below.

Aspose.Cells provides the [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) and [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) properties to set the custom separators for formatting/parsing numbers.

{{% /alert %}}

## **Specifying Custom Separators using Microsoft Excel**

The following screenshot shows the **Advanced Excel Options** and highlights the section to specify the **Custom Separators**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specifying Custom Separators using Aspose.Cells**

The following sample code illustrates how to specify the custom separators using the Aspose.Cells API. It sets the custom number decimal and group separators to a dot and a space, respectively.

### C++ code to specify custom number decimal and group separators

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}