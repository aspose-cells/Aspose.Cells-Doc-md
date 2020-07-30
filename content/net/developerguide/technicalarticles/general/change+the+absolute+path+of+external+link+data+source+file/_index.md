---
title : "Change the Absolute Path of External Link Data Source File" 
description : "" 
weight : 16585 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/change+the+absolute+path+of+external+link+data+source+file/
---

# Aspose.Cells for .NET : Change the Absolute Path of External Link Data Source File


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Change the Absolute Path of External Link Data Source File](#change-the-absolute-path-of-external-link-data-source-file)
{{< /panel >}}
 

 

## Possible Usage Scenarios

If you want to change the absolute path of the external link data source file, then please use the [Workbook.AbsolutePath](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/absolutepath) property. Initially, this property will be set to the path from where the excel file was loaded. But you can set it to an empty string or you can set it to some local folder path or remote network path. Whenever you will change this property, the path of external link data source file will also be changed.

## Change the Absolute Path of External Link Data Source File

The following sample code loads the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013577/5115146.xlsx) which contains an external link. It first prints the external link data source which prints the remote path. Then it removes the remote path and prints again, this time, it prints external link data source with the local path. Then it changes the [Workbook.AbsolutePath](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/absolutepath) property to a local and remote path and prints the external link data source again and changes are reflected in the console output.

  
Here is the console or debug output after the execution of the above sample code with the [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013577/5115146.xlsx).

External Link Data Source: http:\\\\ws874dmErit\\WebFiles\\Files\\300\\ExternalAccounts.xlsxExternal Link Data Source After Removing Remote Path: D:\\Downloads\\ExternalAccounts.xlsxExternal Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\\Files\\Extra\\ExternalAccounts.xlsxExternal Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/net/attachments/5013577/5115146.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

