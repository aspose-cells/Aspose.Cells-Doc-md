---
title: Check Custom Number Format when Setting Style.Custom Property
description: Aspose.Cells is a Python library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, Python libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /python-net/check-custom-number-format-when-setting-style-custom-property/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

If you assign an invalid custom number format to the [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) property, Aspose.Cells will not throw any exception. However, if you want Aspose.Cells to check whether the assigned custom number format is valid, set the [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to the [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) property. Since we have already set the [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) property to **true**, it throws an exception, e.g., Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

{{< app/cells/assistant language="python-net" >}}
