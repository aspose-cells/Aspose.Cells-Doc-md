---
title: Vérifier si le projet VBA d un classeur est signé avec C++
linktitle: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Vérifier si le projet VBA d un classeur est signé avec Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande **Tools > Digital Signatures...** menu. De même, vous pouvez le vérifier de manière programmatique avec Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## **Vérifier si le projet VBA d’un classeur est signé en C++**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned). La propriété retournera **true** si le projet est signé, sinon elle retournera **false**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
