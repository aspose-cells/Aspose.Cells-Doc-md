---
title: Obtenir les points de connexion d une forme avec C++
linktitle: Obtenir les points de connexion d une forme
type: docs
weight: 3500
url: /fr/cpp/get-connection-points-from-shape/
description: Apprenez comment récupérer les points de connexion d une forme en utilisant Aspose.Cells for C++.
---

Aspose.Cells offre de riches fonctionnalités pour gérer les formes dans les feuilles de calcul. Parfois, il est nécessaire d'obtenir les points de connexion d'une forme pour l'alignement ou le placement. Le code suivant peut être utilisé pour obtenir la liste des points de connexion d'une forme en utilisant la méthode [Shape.GetConnectionPoints()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getconnectionpoints/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"sampleGetFonts.xlsx");

    Vector<Font> fonts = workbook.GetFonts();

    for (int i = 0; i < fonts.GetLength(); ++i)
    {
        std::cout << fonts[i].ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

.
{{< app/cells/assistant language="cpp" >}}
