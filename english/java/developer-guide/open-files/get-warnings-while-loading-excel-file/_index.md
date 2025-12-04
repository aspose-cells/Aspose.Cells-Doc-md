---
title: Get Warnings while Loading Excel File
type: docs
weight: 60
url: /java/get-warnings-while-loading-excel-file/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes the user tries to load the workbook which is somewhat corrupt but loadable. In such case, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) interface and setting [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setWarningCallback-com.aspose.cells.IWarningCallback-) property.

## **Get Warnings while Loading Excel File**

The following sample code explains how to get warnings while loading excel file. The code loads the [sample excel file](sampleDuplicateDefinedName.xlsx) which throws [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE-DEFINED-NAME) warning on loading. This warning is then caught by [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning-com.aspose.cells.WarningInfo-) method that prints the warning messages on the console. The code then saves the workbook as [output excel file](outputDuplicateDefinedName.xlsx). If you open the sample excel file in Microsoft Excel, it will also display you this warning as shown in this screenshot. Please also check the console output of the code given below for more understanding.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Console Output**

Here is the console output of the above code when executed with the provided [sample excel file](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
