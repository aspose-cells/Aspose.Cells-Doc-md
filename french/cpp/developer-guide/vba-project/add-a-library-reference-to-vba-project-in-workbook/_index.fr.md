---
title: Ajouter une référence à la bibliothèque dans le projet VBA dans le classeur avec C++
linktitle: Ajoutez une référence de bibliothèque au projet VBA dans le classeur
type: docs
weight: 80
url: /fr/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: Apprenez comment ajouter ou enregistrer des références de bibliothèque dans le projet VBA d’un classeur en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous devez ajouter ou enregistrer la référence de la bibliothèque dans le projet VBA par le biais du code. Vous pouvez le faire en utilisant la méthode Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

{{% /alert %}}

## **Ajouter une référence de bibliothèque au projet VBA dans Microsoft Excel**

Dans Microsoft Excel, vous pouvez ajouter une référence de bibliothèque au projet VBA en cliquant sur **Outils > Références...** manuellement.

## **Ajouter une référence de bibliothèque au projet VBA dans un classeur en utilisant Aspose.Cells**

L'exemple de code suivant ajoute ou enregistre deux références de bibliothèque dans le projet VBA du classeur en utilisant la méthode [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

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
