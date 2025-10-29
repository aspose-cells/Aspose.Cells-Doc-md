---
title: Добавьте ссылку на библиотеку в проект VBA в рабочей книге с помощью C++
linktitle: Добавить ссылку на библиотеку в проект VBA в книге
type: docs
weight: 80
url: /ru/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Узнайте, как добавлять или регистрировать ссылки на библиотеки в проекте VBA в рабочей книге, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам нужно добавить или зарегистрировать ссылку на библиотеку в проекте VBA через код. Вы можете сделать это с помощью метода Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

{{% /alert %}}

## **Добавить ссылку на библиотеку в проект VBA в Microsoft Excel**

В Microsoft Excel вы можете добавить ссылку на библиотеку в проект VBA, нажав **Инструменты > Ссылки...** вручную.

## **Добавить ссылку на библиотеку в проект VBA в книге с помощью Aspose.Cells**

В следующем примере кода добавляются или регистрируются две ссылки на библиотеку в проекте VBA книги с использованием метода [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

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
