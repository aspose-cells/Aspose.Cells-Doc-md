---
title: Lägg till en bibliotekskälla till VBA projekt i arbetsboken med C++
linktitle: Lägg till en biblioteksreferens till VBA projekt i arbetsbok
type: docs
weight: 80
url: /sv/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Lär dig hur man lägger till eller registrerar bibliotekskällor till VBA projektet i en arbetsbok med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland behöver du lägga till eller registrera biblioteksreferensen till VBA-projektet via kod. Du kan göra det med hjälp av Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) -metoden.

{{% /alert %}}

## **Lägg till en biblioteksreferens till VBA-projekt i Microsoft Excel**

I Microsoft Excel kan du lägga till en biblioteksreferens till VBA-projektet genom att klicka på **Verktyg > Referenser...** manuellt.

## **Lägg till en biblioteksreferens till VBA-projekt i en arbetsbok med Aspose.Cells.**

Följande exempelkod lägger till eller registrerar två biblioteksreferenser till VBA-projektet för arbetsboken med hjälp av [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) -metoden.

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
