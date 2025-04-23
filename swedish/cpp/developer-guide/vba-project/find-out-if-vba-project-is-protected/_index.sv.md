---  
title: Kontrollera om VBA projekt är skyddat med C++  
linktitle: Ta reda på om VBA projektet är skyddat  
type: docs  
weight: 20  
url: /sv/cpp/find-out-if-vba-project-is-protected/  
description: Kontrollera om VBA projektet i en Excel fil är skyddat med Aspose.Cells och C++.  
---  

## **Ta reda på om VBA-projektet är skyddat i C++**

Du kan avgöra om VBA (Visual Basic Applications) projektet för din Excel-fil är skyddat eller inte med Aspose.Cells med [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)-egenskapen.

## **Exempelkod**

Följande exempel skapar en arbetsbok och kontrollerar om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen. Se dess konsolutdata för referens. Innan skyddet returnerar [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) **false**, men efter skyddet returnerar det **true**.

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

## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
