---
title: Get Warnings while Loading Excel File
type: docs
weight: 110
url: /net/get-warnings-while-loading-excel-file/
---

## **Possible Usage Scenarios**
Sometimes the user tries to load the workbook which is somewhat corrupt but loadable. In such case, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [IWarningCallback](https://apireference.aspose.com/net/cells/aspose.cells/iwarningcallback) interface and setting [LoadOptions.WarningCallback](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/warningcallback) property.
## **Get Warnings while Loading Excel File**
The following sample code explains how to get warnings while loading excel file. The code loads the [sample excel file](attachments/25002729/25395215.xlsx) which throws [DuplicateDefinedName](https://apireference.aspose.com/net/cells/aspose.cells/warningtype) warning on loading. This warning is then caught by [IWarningCallback.Warning()](https://apireference.aspose.com/net/cells/aspose.cells/iwarningcallback/methods/warning) method that prints the warning messages on the console. The code then saves the workbook as [output excel file](attachments/25002729/25395217.xlsx). If you open the sample excel file in Microsoft Excel, it will also display you this warning as shown in this screenshot. Please also check the console output of the code given below for more understanding.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}
## **Console Output**
Here is the console output of the above code when executed with the provided [sample excel file](attachments/25002729/25395215.xlsx).

{{< highlight java >}}

 Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}