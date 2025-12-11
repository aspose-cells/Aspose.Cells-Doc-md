---
title: Change the Absolute Path of External Link Data Source File
type: docs
weight: 290
url: /python-net/change-the-absolute-path-of-external-link-data-source-file/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Possible Usage Scenarios

If you want to change the absolute path of the external link data source file, then please use the [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) property. Initially, this property will be set to the path from which the Excel file was loaded. But you can set it to an empty string or you can set it to some local folder path or remote network path. Whenever you change this property, the path of the external link data source file will also be changed.

## Change the Absolute Path of External Link Data Source File

The following sample code loads the [sample Excel file](5115146.xlsx) which contains an external link. It first prints the external link data source, which shows the remote path. Then it removes the remote path and prints again; this time it prints the external link data source with the local path. Then it changes the [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) property to a local and a remote path, prints the external link data source again, and the changes are reflected in the console output.

Here is the console or debug output after executing the above sample code with the sample Excel file.

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
