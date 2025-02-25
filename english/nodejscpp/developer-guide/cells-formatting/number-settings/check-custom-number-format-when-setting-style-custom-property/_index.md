---
title: Check Custom Number Format when Setting Style.Custom Property
linktitle: Check Custom Number Format when Setting Style.Custom Property
description: Aspose.Cells is a Node.js library for working with spreadsheet files, which supports checking custom number formats when styling. This article will show you how to use the Aspose.Cells library to check custom number formats to ensure that the styling is correct.
keywords: Aspose.Cells, Node.js libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign an invalid custom number format to [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) method, then Aspose.Cells for Node.js via C++ will not throw any exception. But if you want Aspose.Cells to check if the assigned custom number format is valid or not, then please set the [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) method to **true**.

## **Check Custom Number Format when setting Style.setCustom(string) method**

The following sample code assigns an invalid custom number format to [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) method. Since we have already set the [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) method to **true**, it throws an exception, e.g., Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

