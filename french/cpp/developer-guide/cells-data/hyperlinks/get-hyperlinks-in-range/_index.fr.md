---
title: Obtenir les liens hypertexte dans une plage avec C++
linktitle: Obtenir des hyperliens dans une plage
type: docs
weight: 100
url: /fr/cpp/get-hyperlinks-in-range/
description: Apprenez comment obtenir des liens hypertexte dans une plage via l API Aspose.Cells for C++.
keywords: Obtenir des hyperliens dans la plage, Obtenir tous les hyperliens dans la plage sélectionnée, Supprimer le lien hypertexte dans la plage, Supprimer les liens hypertexte dans la plage sélectionnée
---

## **Obtenir des hyperliens dans la plage**

La classe [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fournit une propriété [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/gethyperlinks/) qui retourne tous les hyperliens dans la plage sélectionnée. Vous pouvez également supprimer le lien hypertexte en appelant la méthode [**Hyperlink.Delete**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/delete/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"HyperlinksSample.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Range range = worksheet.GetCells().CreateRange(u"A2", u"B3");
    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();

    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink& link = hyperlinks[i];
        std::cout << link.GetArea().ToString().ToUtf8() << " : " << link.GetAddress().ToUtf8() << std::endl;
        link.Delete();
    }

    workbook.Save(outDir + u"HyperlinksSample_out.xlsx");
    std::cout << "Hyperlinks processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
