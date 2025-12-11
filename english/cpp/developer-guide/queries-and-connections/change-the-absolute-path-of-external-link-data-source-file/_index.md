---
title: Change the Absolute Path of External Link Data Source File with C++
linktitle: Change the Absolute Path of External Link Data Source File
type: docs
weight: 290
url: /cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Change the absolute path of external link data source file in Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Possible Usage Scenarios

If you want to change the absolute path of the external link data source file, then please use the [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) method. Initially, this property will be set to the path from where the Excel file was loaded. However, you can set it to an empty string, or you can set it to a local folder path or a remote network path. Whenever you change this property, the path of the external link data source file will also be changed.

## Change the Absolute Path of External Link Data Source File

The following sample code loads the [sample Excel file](5115146.xlsx) which contains an external link. It first prints the external link data source, which shows the remote path. Then it removes the remote path and prints again; this time it prints the external link data source with the local path. Then it changes the `Workbook.AbsolutePath` to a local and a remote path, prints the external link data source again, and the changes are reflected in the console output.

Here is the console/debug output after executing the sample code with the [sample Excel file](5115146.xlsx).

{{< highlight cpp >}}
External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
