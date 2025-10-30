---  
title: Scopri se il progetto VBA è protetto con C++  
linktitle: Scopri se il progetto VBA è Protetto  
type: docs  
weight: 20  
url: /it/cpp/find-out-if-vba-project-is-protected/  
description: Verifica se il progetto VBA di un file Excel è protetto utilizzando Aspose.Cells con C++.  
---  

## **Scopri se il progetto VBA è protetto in C++**

Puoi scoprire se il progetto VBA (Visual Basic Applications) del tuo file Excel è protetto o meno con Aspose.Cells utilizzando la proprietà [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/).

## **Codice di Esempio**

Il seguente esempio di codice crea un workbook e poi verifica se il suo progetto VBA è protetto o meno. Successivamente protegge il progetto VBA e di nuovo verifica se è protetto o meno. Consulta l'output della console come riferimento. Prima della protezione, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) restituisce **false**, ma dopo la protezione, restituisce **true**.

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

## **Output della console**

Questo è l'output della console del codice di esempio sopra per un riferimento.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
