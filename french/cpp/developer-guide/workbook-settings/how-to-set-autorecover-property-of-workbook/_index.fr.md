---
title: Comment définir la propriété AutoRecover du classeur avec C++
linktitle: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/cpp/how-to-set-autorecover-property-of-workbook/
description: Apprenez comment activer ou désactiver la propriété AutoRecover d un classeur en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover d'un classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** dans un classeur, Microsoft Excel désactive AutoRecover (Autosave) sur ce fichier Excel.

Aspose.Cells fournit la propriété [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) pour activer ou désactiver cette option.

{{% /alert %}}

Le code suivant explique comment utiliser la propriété [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) du classeur. Le code lit d'abord la valeur par défaut de cette propriété, qui est **true**, puis la définit à **false** et enregistre le classeur. Ensuite, il relit le classeur et lit la valeur de cette propriété, qui est **false** à ce moment.

## Code C++ pour définir la propriété AutoRecover du classeur

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
