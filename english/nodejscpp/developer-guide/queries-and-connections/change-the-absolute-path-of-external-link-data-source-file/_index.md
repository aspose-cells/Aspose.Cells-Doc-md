---
title: Change the Absolute Path of External Link Data Source File with Node.js via C++
linktitle: Change the Absolute Path of External Link Data Source File
type: docs
weight: 290
url: /nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Learn how to change the absolute path of the external link data source file using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Possible Usage Scenarios

If you want to change the absolute path of the external link data source file, please use the [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) property. Initially, this property will be set to the path from where the Excel file was loaded. You can set it to an empty string, a local folder path, or a remote network path. Whenever you change this property, the path of the external link data source file will also be changed.

## Change the Absolute Path of External Link Data Source File

The following sample code loads the [sample Excel file](5115146.xlsx) which contains an external link. It first prints the external link data source, showing the remote path. Then it removes the remote path and prints again; this time, it prints the external link data source with the local path. After that, it changes the [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) property to a local path and then to a remote path, printing the external link data source again. The changes are reflected in the console output.

Here is the console output after the execution of the above sample code with the [sample Excel file](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http://ws874dmErit/WebFiles/Files/300/ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
