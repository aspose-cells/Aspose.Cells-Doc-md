---
title: Get Warnings while Loading Excel File with Golang via C++
linktitle: Get Warnings while Loading Excel File
type: docs
weight: 110
url: /go-cpp/get-warnings-while-loading-excel-file/
description: Learn how to catch and handle warnings while loading Excel files using Aspose.Cells for Go via C++.
---

## **Possible Usage Scenarios**

Sometimes the user tries to load a workbook that is somewhat corrupt but still loadable. In such cases, Aspose.Cells throws warnings while loading the workbook. You can catch these warnings by implementing the [**IWarningCallback**](https://reference.aspose.com/cells/go-cpp/iwarningcallback/) interface and setting the [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getwarningcallback/) property.

## **Get Warnings while Loading Excel File**

The following sample code explains how to get warnings while loading an Excel file. The code loads the [sample Excel file](sampleDuplicateDefinedName.xlsx), which throws a **DuplicateDefinedName** warning on loading. This warning is then caught by the [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/go-cpp/iwarningcallback/warning/) method, which prints the warning messages on the console. The code then saves the workbook as an [output Excel file](outputDuplicateDefinedName.xlsx). If you open the sample Excel file in Microsoft Excel, it will also display this warning, as shown in the screenshot below. Please also check the console output of the code given below for better understanding.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsWhileLoadingExcelFile.go" >}}

## **Console Output**

Here is the console output of the above code when executed with the provided [sample Excel file](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
