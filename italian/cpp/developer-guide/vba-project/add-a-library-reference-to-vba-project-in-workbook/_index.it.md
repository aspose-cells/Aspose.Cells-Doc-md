---
title: Aggiungi un riferimento alla libreria al progetto VBA nel workbook con C++
linktitle: Aggiungi un riferimento di libreria al progetto VBA nel workbook
type: docs
weight: 80
url: /it/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Impara come aggiungere o registrare riferimenti alla libreria nel progetto VBA in un workbook utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte è necessario aggiungere o registrare il riferimento della libreria al progetto VBA tramite codice. Puoi farlo utilizzando il metodo Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

{{% /alert %}}

## **Aggiungi un riferimento della libreria al progetto VBA in Microsoft Excel**

In Microsoft Excel, puoi aggiungere un riferimento della libreria al progetto VBA cliccando manualmente su **Strumenti > Riferimenti...**

## **Aggiungi un riferimento della libreria al progetto VBA in un workbook utilizzando Aspose.Cells**

Il codice di esempio seguente aggiunge o registra due riferimenti di libreria al progetto VBA del workbook utilizzando il metodo [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

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
{{< app/cells/assistant language="cpp" >}}
