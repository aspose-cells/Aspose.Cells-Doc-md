---
title: Agrega una referencia de biblioteca al proyecto VBA en el libro de trabajo con C++
linktitle: Agregar una referencia de biblioteca al proyecto VBA en el libro
type: docs
weight: 80
url: /es/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Aprende cómo agregar o registrar referencias de biblioteca en el proyecto VBA en un libro de trabajo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, es necesario agregar o registrar la referencia de la biblioteca en el proyecto VBA a través del código. Puedes hacerlo usando el método [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/) de Aspose.Cells.

{{% /alert %}}

## **Agrega una referencia de la biblioteca al proyecto VBA en Microsoft Excel**

En Microsoft Excel, puedes agregar una referencia de la biblioteca al proyecto VBA haciendo clic en **Herramientas > Referencias...** manualmente.

## **Agrega una referencia de la biblioteca al proyecto VBA en un libro usando Aspose.Cells**

El siguiente código de muestra agrega o registra dos referencias de biblioteca al proyecto VBA del libro usando el método [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

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
