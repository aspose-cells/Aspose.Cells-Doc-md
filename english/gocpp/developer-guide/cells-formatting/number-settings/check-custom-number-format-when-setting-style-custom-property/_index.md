---
title: Check Custom Number Format when Setting Style.Custom Property with Golang via C++
description: Aspose.Cells is a C++ library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, C++ libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign an invalid custom number format to [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) property, then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not, then please set the [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) property. Since we have already set [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) property to **true**, therefore it throws an exception, e.g., Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-GO-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}