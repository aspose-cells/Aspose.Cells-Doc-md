---
title: Change the Absolute Path of External Link Data Source File
type: docs
weight: 1020
url: /java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Possible Usage Scenarios**
If you want to change the absolute path of the external link data source file, then please use the [Workbook.AbsolutePath](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#AbsolutePath) property. Initially, this property will be set to the path from where the excel file was loaded. But you can set it to an empty string or you can set it to some local folder path or remote network path. Whenever you will change this property, the path of external link data source file will also be changed.
## **Change the Absolute Path of External Link Data Source File**
The following sample code loads the [sample excel file](5472589.xlsx) which contains an external link. It first prints the external link data source which prints the remote path. Then it removes the remote path and prints again, this time, it prints external link data source with the local path. Then it changes the [Workbook.AbsolutePath](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#AbsolutePath) property to a local and remote path and prints the external link data source again and changes are reflected in the console output.
## **Sample Code**
{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Console Output**
Here is the console or debug output after the execution of the above sample code with the [sample excel file](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
