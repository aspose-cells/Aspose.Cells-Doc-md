---
title : "Get Warnings while Loading Excel File" 
description : "" 
weight : 12054 
toc : false
type: docs
url: /java/developerguide/ld-sv-cvt-mng/get+warnings+while+loading+excel+file/
---

# Aspose.Cells for Java : Get Warnings while Loading Excel File


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Get Warnings while Loading Excel File](#get-warnings-while-loading-excel-file)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
## Possible Usage Scenarios

Sometimes the user tries to load the workbook which is somewhat corrupt but loadable. In such case, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [IWarningCallback](https://apireference.aspose.com/java/cells/com.aspose.cells/IWarningCallback) interface and setting [LoadOptions.WarningCallback](https://apireference.aspose.com/java/cells/com.aspose.cells/loadoptions#WarningCallback) property.

## Get Warnings while Loading Excel File

The following sample code explains how to get warnings while loading excel file. The code loads the [sample excel file](https://docs2.aspose.com/cells/java/attachments/25002833/25395234.xlsx) which throws [DuplicateDefinedName](https://apireference.aspose.com/java/cells/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME) warning on loading. This warning is then caught by [IWarningCallback.Warning()](https://apireference.aspose.com/java/cells/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo)) method that prints the warning messages on the console. The code then saves the workbook as [output excel file](https://docs2.aspose.com/cells/java/attachments/25002833/25395233.xlsx). If you open the sample excel file in Microsoft Excel, it will also display you this warning as shown in this screenshot. Please also check the console output of the code given below for more understanding.

![](https://docs2.aspose.com/cells/java/attachments/25002833/25395232.png)

## Sample Code

## Console Output

Here is the console output of the above code when executed with the provided [sample excel file](https://docs2.aspose.com/cells/java/attachments/25002833/25395234.xlsx).

{{< code lang="cs" >}}
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228
Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16
{{< /code >}}

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Get-Warnings-while-Loading-Excel-File.png](https://docs2.aspose.com/cells/java/attachments/25002833/25395232.png) (image/png)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputDuplicateDefinedName.xlsx](https://docs2.aspose.com/cells/java/attachments/25002833/25395233.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleDuplicateDefinedName.xlsx](https://docs2.aspose.com/cells/java/attachments/25002833/25395234.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  

