---
title: Fügen Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe mit C++ hinzu
linktitle: Fügen Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe hinzu
type: docs
weight: 80
url: /de/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Erfahren Sie, wie Sie Bibliotheksreferenzen in das VBA Projekt einer Arbeitsmappe mithilfe von Aspose.Cells for C++ hinzufügen oder registrieren.
---

{{% alert color="primary" %}}

Manchmal müssen Sie den Bibliotheksverweis in das VBA-Projekt durch Code hinzufügen oder registrieren. Sie können dies mit der Methode [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) von Aspose.Cells tun.

{{% /alert %}}

## **Fügen Sie einem VBA-Projekt in Microsoft Excel einen Bibliotheksverweis hinzu.**

In Microsoft Excel können Sie manuell durch Klicken auf **Extras > Verweise...** einen Bibliotheksverweis auf das VBA-Projekt hinzufügen.

## **Fügen Sie einem Arbeitsmappen-VBA-Projekt einen Bibliotheksverweis mit Aspose.Cells hinzu.**

Der folgende Beispielcode fügt oder registriert zwei Bibliotheksreferenzen im VBA-Projekt der Arbeitsmappe mithilfe der Methode [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) hinzu.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputPath = outDir + u"Output_out.xlsm";

    // Create a new workbook
    Workbook workbook;

    // Get the VBA project from the workbook
    VbaProject vbaProj = workbook.GetVbaProject();

    // Add registered references to the VBA project
    vbaProj.GetReferences().AddRegisteredReference(u"stdole", u"*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
    vbaProj.GetReferences().AddRegisteredReference(u"Office", u"*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "VBA project references added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
