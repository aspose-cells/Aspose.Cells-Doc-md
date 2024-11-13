---
title: Check Custom Number Format when Setting Style.Custom Property
description: Aspose.Cells is a Python library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, Python libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign invalid custom number format to [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) property, then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not, then please set the [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) property. Since, we have already set [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) property to **true**, therefore it throws exception e.g. Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

