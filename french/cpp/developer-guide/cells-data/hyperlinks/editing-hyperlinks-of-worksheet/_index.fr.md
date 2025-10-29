---
title: Modifier les liens hypertextes de la feuille de calcul avec C++
linktitle: Modification des hyperliens de la feuille de calcul
type: docs
weight: 330
url: /fr/cpp/editing-hyperlinks-of-worksheet/
description: Apprenez comment modifier les liens hypertextes d une feuille de calcul via l API Aspose.Cells for C++.
keywords: Modifier les hyperliens, Modifier les hyperliens de la feuille de calcul, Modifier le lien hypertexte de la cellule, Accéder à tous les hyperliens de la feuille de calcul
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'accéder à tous les hyperliens de la feuille de calcul en utilisant la collection [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Vous pouvez accéder à chaque lien hypertexte de cette collection un par un et modifier ses propriétés.

{{% /alert %}}

Le code exemple suivant accède à tous les liens hypertexte de la feuille de calcul et modifie leur propriété [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) pour le site Web Aspose.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
