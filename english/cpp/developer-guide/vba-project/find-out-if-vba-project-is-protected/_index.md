---  
title: Find out if VBA Project is Protected with C++  
linktitle: Find out if VBA Project is Protected  
type: docs  
weight: 20  
url: /cpp/find-out-if-vba-project-is-protected/  
description: Check if the VBA project of an Excel file is protected using Aspose.Cells with C++.  
---  

## **Find out if VBA Project is Protected in C++**

You can find if the VBA (Visual Basic Applications) Project of your Excel file is protected or not with Aspose.Cells using [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) property.

## **Sample Code**

The following sample code creates a workbook and then checks if its VBA project is protected or not. Then it protects the VBA project and again checks if its VBA project is protected or not. Please see its console output for a reference. Before protection, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) returns **false** but after protection, it returns **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Console Output**

This is the console output of the above sample code for a reference.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}