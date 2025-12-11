---  
title: Check if VBA Code is Signed with C++  
linktitle: Check if VBA Code is Signed  
type: docs  
weight: 100  
url: /cpp/check-if-vba-code-is-signed/  
description: Learn how to check if VBA code in Excel files is signed using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Aspose.Cells allows users to check whether the VBA code project is signed. Use the [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) property to determine if the VBA code project is signed.  

{{% /alert %}}  

The following code explains how to check if the VBA code is signed using the [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) property. You can use any of your Excel files to test this code. For testing purposes, you can use [this Excel file used in the code](5115032.xlsm).  

## **Check if VBA Code is Signed in C++**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Console Output  

Below is the console output of the above code using the [sample Excel file](5115032.xlsm) provided in the link.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
