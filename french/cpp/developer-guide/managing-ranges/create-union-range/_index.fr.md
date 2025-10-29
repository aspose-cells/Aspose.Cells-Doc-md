---
title: Créer une plage d union avec C++
linktitle: Créer une plage union
type: docs
weight: 360
url: /fr/cpp/create-union-range/
description: Créer une plage d union dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Créer l'union de la plage**
Aspose.Cells offre la possibilité de créer une plage d'union en utilisant la méthode [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). La méthode [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) accepte deux paramètres, l'adresse pour créer la plage d'union et l'indice de la feuille. La méthode retourne un objet [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/).

Le morceau de code suivant montre comment créer une plage d'union en utilisant la méthode [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). Le fichier de sortie généré par le code est joint pour référence.

- [Fichier de sortie](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
