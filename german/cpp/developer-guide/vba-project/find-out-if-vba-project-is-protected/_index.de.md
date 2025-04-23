---  
title: Prüfen, ob VBA Projekt geschützt ist mit C++  
linktitle: Herausfinden, ob das VBA Projekt geschützt ist  
type: docs  
weight: 20  
url: /de/cpp/find-out-if-vba-project-is-protected/  
description: Überprüfen Sie, ob das VBA Projekt einer Excel Datei mit Aspose.Cells in C++ geschützt ist.  
---  

## **Erfahren Sie, ob das VBA-Projekt in C++ geschützt ist**

Sie können feststellen, ob das VBA (Visual Basic for Applications) Projekt Ihrer Excel-Datei mit Aspose.Cells mit [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/)-Eigenschaft geschützt ist.

## **Beispielcode**

Der folgende Beispielcode erstellt eine Arbeitsmappe und überprüft, ob ihr VBA-Projekt geschützt ist oder nicht. Dann schützt er das VBA-Projekt und überprüft erneut, ob das VBA-Projekt geschützt ist oder nicht. Bitte sehen Sie sich die Konsolenausgabe zur Referenz an. Vor dem Schutz gibt [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) **false** zurück, nach dem Schutz gibt es **true** zurück.

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

## **Konsolenausgabe**

Dies ist die Konsolenausgabe des obigen Beispielcodes als Referenz.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
